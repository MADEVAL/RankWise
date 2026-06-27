"""
RankWise Validator — computable SEO metrics for text content.
Uses ReadSightPy (readsight) for readability — TeX/Liang syllable counting,
17 formulas, all 9 RankWise languages supported (incl. UK and PT).
Supports all 9 RankWise languages: EN, RU, UK, DE, FR, ES, PT, IT, PL.
"""

import re
import statistics
from dataclasses import dataclass, field

from readsight import ReadSight


# ═══════════════════════════════════════════════════════════════════════════════
# LANGUAGE SUPPORT MATRIX (ReadSightPy)
# ═══════════════════════════════════════════════════════════════════════════════
#
# Lang | RS code  | FRE | FKGL | universal (GF/SMOG/CL/ARI/LIX) | headline formula
# EN   | en-us    | ✔   | ✔    | ✔                              | Flesch Reading Ease
# DE   | de-1996  | ✔   | ✔    | ✔                              | Wiener Sachtextformel
# ES   | es       | ✔   | ✔    | ✔                              | Fernández-Huerta
# FR   | fr       | ✔   | ✔    | ✔                              | Flesch Reading Ease
# IT   | it       | ✔   | ✔    | ✔                              | Gulpease
# PT   | pt       | ✔   | ✔    | ✔                              | Flesch Reading Ease
# RU   | ru       | ✔   | ✔    | ✔                              | Flesch Reading Ease
# UK   | uk       | ✗   | ✗    | ✔                              | LIX
# PL   | pl       | ✗   | ✗    | ✔ (+ FOG-PL)                   | FOG-PL
#
# Every RankWise language now has deterministic readability (no LLM fallback).

# Mapping from RankWise lang codes to ReadSightPy language codes
READSIGHT_LANG_MAP = {
    "en": "en-us",
    "ru": "ru",
    "uk": "uk",
    "de": "de-1996",
    "fr": "fr",
    "es": "es",
    "pt": "pt",
    "it": "it",
    "pl": "pl",
}

# All 9 languages now carry computable readability via ReadSightPy
READABILITY_LANGS = set(READSIGHT_LANG_MAP.keys())

# ── ReadSightPy engine cache (engine init parses .tex patterns — cache per code) ──
_ENGINE_CACHE: dict = {}


def _get_engine(lang: str) -> ReadSight:
    code = READSIGHT_LANG_MAP[lang]
    if code not in _ENGINE_CACHE:
        _ENGINE_CACHE[code] = ReadSight(code)
    return _ENGINE_CACHE[code]


# Registry key (from get_supported_formulas) → ReadSight method name
_FORMULA_METHOD = {
    "flesch_reading_ease": "flesch_reading_ease",
    "flesch_kincaid_grade_level": "flesch_kincaid_grade_level",
    "gunning_fog": "gunning_fog",
    "smog": "smog_index",
    "ari": "automated_readability_index",
    "coleman_liau": "coleman_liau",
    "lix": "lix",
    "wiener_sachtextformel": "wiener_sachtextformel",
    "gulpease": "gulpease",
    "fernandez_huerta": "fernandez_huerta",
    "fog_pl": "fog_pl",
}


def _formula_score(rs: ReadSight, supported: set, key: str, text: str):
    """Return a formula's float score, or None if unsupported/errored."""
    if key not in supported:
        return None
    method = _FORMULA_METHOD.get(key)
    if method is None:
        return None
    try:
        result = getattr(rs, method)(text)
        return float(result.score)
    except Exception:
        return None


def _nz(value) -> float:
    """None → -1.0 sentinel (matches legacy 'unavailable' convention)."""
    return value if value is not None else -1.0

# ═══════════════════════════════════════════════════════════════════════════════
# LANGUAGE RESOURCES — all 9 languages
# ═══════════════════════════════════════════════════════════════════════════════

# ── Word tokenization patterns ──────────────────────────────────────────────
WORD_PATTERNS = {
    "en": re.compile(r"[A-Za-zÀ-ÖØ-öø-ÿ0-9]+", re.IGNORECASE),
    "ru": re.compile(r"[А-Яа-яЁёA-Za-z0-9]+"),
    "uk": re.compile(r"[А-Яа-яЇїІіЄєҐґA-Za-z0-9]+"),
    "de": re.compile(r"[A-Za-zÄäÖöÜüß0-9]+"),
    "fr": re.compile(r"[A-Za-zÀ-ÿ0-9]+"),
    "es": re.compile(r"[A-Za-zÁáÉéÍíÓóÚúÜüÑñ0-9]+"),
    "pt": re.compile(r"[A-Za-zÀ-ü0-9]+"),
    "it": re.compile(r"[A-Za-zÀ-ü0-9]+"),
    "pl": re.compile(r"[A-Za-zĄąĆćĘęŁłŃńÓóŚśŹźŻż0-9]+"),
}

# ── Transition words per language ───────────────────────────────────────────
TRANSITION_WORDS = {
    "en": {
        "however", "therefore", "because", "although", "specifically",
        "for example", "for instance", "in contrast", "similarly", "consequently",
        "notably", "meanwhile", "furthermore", "moreover", "additionally",
        "nevertheless", "nonetheless", "otherwise", "instead", "accordingly",
        "hence", "thus", "in addition", "on the other hand", "as a result",
        "in particular", "in conclusion", "to summarize", "first", "second",
        "third", "finally", "next", "then", "also", "besides", "indeed",
        "in fact", "of course", "certainly", "surely", "undoubtedly",
        "regardless", "despite", "even though", "while", "whereas",
    },
    "ru": {
        "однако", "поэтому", "так как", "хотя", "например", "в частности",
        "в то же время", "кроме того", "следовательно", "тем не менее",
        "в отличие от", "в результате", "также", "потому что", "несмотря на",
        "вместо", "в первую очередь", "во-первых", "во-вторых", "наконец",
        "прежде всего", "в целом", "в связи с", "благодаря", "вследствие",
    },
    "uk": {
        "однак", "тому", "через те що", "хоча", "наприклад", "зокрема",
        "водночас", "крім того", "отже", "тим не менш", "на відміну від",
        "у результаті", "також", "бо", "тому що", "попри", "замість",
        "по-перше", "по-друге", "нарешті", "передусім", "загалом",
        "у зв'язку з", "завдяки", "внаслідок",
    },
    "de": {
        "jedoch", "deshalb", "weil", "obwohl", "zum Beispiel", "insbesondere",
        "darüber hinaus", "daher", "dennoch", "im Gegensatz dazu", "infolgedessen",
        "außerdem", "schließlich", "zuerst", "zweitens", "drittens", "trotzdem",
        "stattdessen", "auch", "zudem", "allerdings", "sowohl", "weder",
    },
    "fr": {
        "cependant", "donc", "parce que", "bien que", "par exemple",
        "en particulier", "de plus", "par conséquent", "néanmoins",
        "en revanche", "ainsi", "également", "malgré", "au lieu de",
        "d'abord", "ensuite", "enfin", "pourtant", "toutefois", "en effet",
        "d'une part", "d'autre part", "en outre",
    },
    "es": {
        "sin embargo", "por lo tanto", "porque", "aunque", "por ejemplo",
        "en particular", "además", "por consiguiente", "no obstante",
        "en contraste", "asimismo", "también", "a pesar de", "en lugar de",
        "primero", "segundo", "tercero", "finalmente", "entonces", "pues",
        "en cambio", "en resumen", "es decir",
    },
    "pt": {
        "no entanto", "portanto", "porque", "embora", "por exemplo",
        "em particular", "além disso", "consequentemente", "apesar disso",
        "por outro lado", "também", "primeiro", "segundo", "finalmente",
        "então", "assim", "dessa forma", "em vez de", "apesar de", "pois",
        "em contrapartida", "em resumo", "ou seja",
    },
    "it": {
        "tuttavia", "quindi", "perché", "sebbene", "per esempio",
        "in particolare", "inoltre", "di conseguenza", "nonostante",
        "al contrario", "anche", "primo", "secondo", "infine", "dunque",
        "pertanto", "invece", "malgrado", "cioè", "ovvero", "infatti",
        "d'altra parte", "in sintesi",
    },
    "pl": {
        "jednak", "dlatego", "ponieważ", "chociaż", "na przykład",
        "w szczególności", "ponadto", "w rezultacie", "niemniej jednak",
        "natomiast", "również", "po pierwsze", "po drugie", "wreszcie",
        "zatem", "więc", "mimo", "zamiast", "czyli", "to znaczy",
        "w przeciwieństwie", "podsumowując", "przede wszystkim",
    },
}

# ── Passive voice patterns per language ─────────────────────────────────────
PASSIVE_PATTERNS = {
    "en": [
        re.compile(r"\b(?:am|is|are|was|were|be|been|being)\s+(?:\w+ly\s+)?(?:\w+ed|built|done|made|found|known|seen|taken|given|said|set|shown|told|written)\b", re.IGNORECASE),
        re.compile(r"\b(?:has|have|had|will have)\s+been\s+\w+(?:ed|d|t|en)\b", re.IGNORECASE),
    ],
    "ru": [
        re.compile(r"\b(?:был|была|было|были|будет|будут)\s+\w+(?:н|на|но|ны|т|та|то|ты|ен|ена|ено|ены|ан|ана|ано|аны)\b", re.IGNORECASE),
    ],
    "uk": [
        re.compile(r"\b(?:був|була|було|були|буде|будуть)\s+\w+(?:н|на|но|ні|т|та|то|ті|ен|ена|ено|ені|ан|ана|ано|ані)\b", re.IGNORECASE),
    ],
    "de": [
        re.compile(r"\b(?:wird|wurde|wurden|werden|ist|war|waren)\s+\w+(?:t|en|iert)\b", re.IGNORECASE),
    ],
    "fr": [
        re.compile(r"\b(?:est|sont|était|étaient|a été|ont été|sera|seront)\s+\w+(?:é|ée|és|ées|u|ue|us|ues|i|ie|is|ies)\b", re.IGNORECASE),
    ],
    "es": [
        re.compile(r"\b(?:es|son|era|eran|fue|fueron|ha sido|han sido|será|serán)\s+\w+(?:ado|ada|ados|adas|ido|ida|idos|idas)\b", re.IGNORECASE),
    ],
    "pt": [
        re.compile(r"\b(?:é|são|era|eram|foi|foram|tem sido|será|serão)\s+\w+(?:ado|ada|ados|adas|ido|ida|idos|idas)\b", re.IGNORECASE),
    ],
    "it": [
        re.compile(r"\b(?:è|sono|era|erano|fu|furono|è stato|sono stati|sarà|saranno)\s+\w+(?:ato|ata|ati|ate|uto|uta|uti|ute|ito|ita|iti|ite)\b", re.IGNORECASE),
    ],
    "pl": [
        re.compile(r"\b(?:jest|są|był|była|było|byli|były|został|została|zostało|zostali|zostały|będzie|będą)\s+\w+(?:owany|ana|ane|ani|ony|ona|one|ęty|ęta|ęte|ty|ta|te)\b", re.IGNORECASE),
    ],
}

# ── Power words per language ────────────────────────────────────────────────
POWER_WORDS = {
    "en": {
        "proven", "secret", "stop", "simple", "exclusive", "limited", "hidden",
        "surprising", "shocking", "unexpected", "amazing", "incredible", "ultimate",
        "essential", "critical", "guaranteed", "instant", "immediate", "automatic",
        "effortless", "breakthrough", "insider", "revealed", "mistake", "warning",
        "never", "avoid", "dangerous", "risk", "urgent", "little-known", "unknown",
        "unconventional", "tested", "research-backed", "data-driven", "expert",
        "science-based", "actual", "real", "exact", "specific", "step-by-step",
        "definitive", "powerful", "effective",
    },
    "ru": {
        "доказано", "секрет", "просто", "эксклюзив", "скрытый", "неожиданный",
        "удивительный", "шокирующий", "гарантировано", "мгновенно", "автоматически",
        "без усилий", "прорыв", "инсайдер", "раскрыто", "ошибка", "предупреждение",
        "никогда", "избегайте", "опасный", "риск", "срочно", "малоизвестный",
        "нестандартный", "протестировано", "эксперт", "реальный", "точный",
        "конкретный", "пошаговый", "мощный", "эффективный", "бесплатно",
        "проверенный", "научно", "исследование", "данные",
    },
    "uk": {
        "доведено", "секрет", "просто", "ексклюзив", "прихований", "несподіваний",
        "дивовижний", "шокуючий", "гарантовано", "миттєво", "автоматично",
        "без зусиль", "прорив", "інсайдер", "розкрито", "помилка", "попередження",
        "ніколи", "уникайте", "небезпечний", "ризик", "терміново", "маловідомий",
        "нестандартний", "протестовано", "експерт", "реальний", "точний",
        "конкретний", "покроковий", "потужний", "ефективний", "безкоштовно",
        "перевірений", "науково", "дослідження", "дані",
    },
    "de": {
        "bewährt", "geheim", "einfach", "exklusiv", "versteckt", "überraschend",
        "schockierend", "erstaunlich", "garantiert", "sofort", "automatisch",
        "mühelos", "durchbruch", "insider", "enthüllt", "fehler", "warnung",
        "niemals", "vermeiden", "gefährlich", "risiko", "dringend", "unbekannt",
        "getestet", "experte", "wissenschaftlich", "datengestützt", "echt",
        "genau", "spezifisch", "schrittweise", "kraftvoll", "effektiv",
    },
    "fr": {
        "prouvé", "secret", "simple", "exclusif", "caché", "surprenant",
        "choquant", "incroyable", "garanti", "instant", "automatique",
        "sans effort", "percée", "initié", "révélé", "erreur", "avertissement",
        "jamais", "éviter", "dangereux", "risque", "urgent", "inconnu",
        "testé", "expert", "scientifique", "réel", "exact", "spécifique",
        "étape par étape", "puissant", "efficace",
    },
    "es": {
        "probado", "secreto", "simple", "exclusivo", "oculto", "sorprendente",
        "impactante", "increíble", "garantizado", "instantáneo", "automático",
        "sin esfuerzo", "revelación", "insider", "revelado", "error", "advertencia",
        "nunca", "evitar", "peligroso", "riesgo", "urgente", "desconocido",
        "probado", "experto", "científico", "real", "exacto", "específico",
        "paso a paso", "poderoso", "eficaz",
    },
    "pt": {
        "comprovado", "segredo", "simples", "exclusivo", "escondido", "surpreendente",
        "chocante", "incrível", "garantido", "instantâneo", "automático",
        "sem esforço", "revelação", "revelado", "erro", "aviso", "nunca",
        "evitar", "perigoso", "arriscado", "urgente", "desconhecido",
        "testado", "especialista", "científico", "real", "exato", "específico",
        "passo a passo", "poderoso", "eficaz",
    },
    "it": {
        "provato", "segreto", "semplice", "esclusivo", "nascosto", "sorprendente",
        "scioccante", "incredibile", "garantito", "istantaneo", "automatico",
        "senza sforzo", "svolta", "rivelato", "errore", "avvertimento",
        "mai", "evitare", "pericoloso", "rischioso", "urgente", "sconosciuto",
        "testato", "esperto", "scientifico", "reale", "esatto", "specifico",
        "passo dopo passo", "potente", "efficace",
    },
    "pl": {
        "sprawdzony", "sekret", "prosty", "ekskluzywny", "ukryty", "zaskakujący",
        "szokujący", "niesamowity", "gwarantowany", "natychmiast", "automatyczny",
        "bez wysiłku", "przełom", "ujawniony", "błąd", "ostrzeżenie",
        "nigdy", "unikaj", "niebezpieczny", "ryzykowny", "pilne", "nieznany",
        "przetestowany", "ekspert", "naukowy", "prawdziwy", "dokładny",
        "konkretny", "krok po kroku", "skuteczny",
    },
}

# ── Stop words per language ─────────────────────────────────────────────────
STOP_WORDS = {
    "en": {"the", "a", "an", "and", "or", "but", "in", "on", "at", "to", "for",
           "of", "with", "by", "from", "up", "about", "into", "through",
           "is", "are", "was", "were", "be", "been", "being", "have", "has",
           "do", "does", "did", "will", "would", "can", "could", "may", "might",
           "must", "shall", "should", "not", "no"},
    "ru": {"и", "в", "на", "с", "по", "к", "от", "из", "о", "об", "за", "до",
           "для", "без", "над", "под", "при", "про", "у", "через", "или", "но",
           "а", "не", "ни", "бы", "ли", "же", "то", "что", "как", "так", "это"},
    "uk": {"і", "й", "та", "в", "у", "на", "з", "до", "для", "без", "над",
           "під", "при", "про", "через", "або", "але", "не", "ні", "би", "ж",
           "що", "як", "це", "від", "по", "за", "перед"},
    "de": {"der", "die", "das", "den", "dem", "des", "ein", "eine", "einer",
           "in", "auf", "mit", "von", "zu", "für", "an", "bei", "aus", "nach",
           "über", "vor", "durch", "um", "gegen", "zwischen", "oder", "und",
           "aber", "nicht", "auch", "noch", "nur", "schon", "so", "wie", "als",
           "am", "im", "ins", "zum", "zur"},
    "fr": {"le", "la", "les", "un", "une", "des", "de", "du", "à", "au", "aux",
           "en", "sur", "dans", "par", "pour", "avec", "sans", "sous", "entre",
           "et", "ou", "mais", "ne", "pas", "plus", "moins", "très", "tout",
           "comme", "que", "qui", "quoi", "dont", "où"},
    "es": {"el", "la", "los", "las", "un", "una", "unos", "unas", "de", "del",
           "a", "al", "en", "por", "para", "con", "sin", "sobre", "entre",
           "y", "e", "o", "u", "pero", "no", "ni", "que", "cual", "como",
           "más", "muy", "tan", "todo", "esta", "este", "esto"},
    "pt": {"o", "a", "os", "as", "um", "uma", "uns", "umas", "de", "do", "da",
           "dos", "das", "em", "no", "na", "nos", "nas", "por", "para", "com",
           "sem", "sobre", "entre", "e", "ou", "mas", "não", "nem", "que",
           "qual", "como", "mais", "muito", "tão", "todo", "todos"},
    "it": {"il", "lo", "la", "i", "gli", "le", "un", "uno", "una", "di", "a",
           "da", "in", "con", "su", "per", "tra", "fra", "e", "o", "ma",
           "non", "né", "che", "chi", "cui", "come", "più", "molto", "tanto"},
    "pl": {"w", "na", "z", "do", "po", "za", "przez", "dla", "przy", "nad",
           "pod", "przed", "między", "i", "oraz", "lub", "albo", "ale",
           "nie", "tak", "jak", "to", "ten", "ta", "te", "się", "już",
           "jeszcze", "tylko", "bardzo"},
}

# ── C8 readability scoring: which metric + target band per language ─────────
# mode selects the metric used to score C8; (lo, hi) is the "pass" band.
#   fkgl  → Flesch-Kincaid grade (lower=easier), pass band is target grade
#   wstf  → Wiener Sachtextformel grade (DE)
#   fh    → Fernández-Huerta (ES, 0-100, higher=easier)
#   gulpease → Gulpease (IT, higher=easier)
#   fre   → Flesch Reading Ease (0-100, higher=easier)
#   lix   → LIX (lower=easier)           — UK (no Flesch available)
#   fogpl → FOG-PL grade (lower=easier)  — PL (no Flesch available)
READABILITY_TARGETS = {
    "en": {"mode": "fkgl",     "range": (7.0, 9.0)},
    "de": {"mode": "wstf",     "range": (4.0, 10.0)},
    "es": {"mode": "fh",       "range": (50.0, 70.0)},
    "it": {"mode": "gulpease", "range": (40.0, 80.0)},
    "fr": {"mode": "fre",      "range": (50.0, 70.0)},
    "ru": {"mode": "fre",      "range": (50.0, 70.0)},
    "pt": {"mode": "fre",      "range": (50.0, 70.0)},
    "uk": {"mode": "lix",      "range": (30.0, 45.0)},
    "pl": {"mode": "fogpl",    "range": (7.0, 12.0)},
}

# ── Headline "language-specific" formula shown in reports (display only) ─────
# (registry_key, display_name). For EN/FR/RU/PT this is plain Flesch Reading Ease.
LANG_SPECIFIC = {
    "en": ("flesch_reading_ease",   "Flesch Reading Ease"),
    "de": ("wiener_sachtextformel", "Wiener Sachtextformel"),
    "es": ("fernandez_huerta",      "Fernández-Huerta"),
    "it": ("gulpease",              "Gulpease"),
    "fr": ("flesch_reading_ease",   "Flesch Reading Ease"),
    "ru": ("flesch_reading_ease",   "Flesch Reading Ease"),
    "pt": ("flesch_reading_ease",   "Flesch Reading Ease"),
    "uk": ("lix",                   "LIX"),
    "pl": ("fog_pl",                "FOG-PL"),
}

# ── Sentence-ending abbreviations (periods that don't end sentences) ────────
# Only abbreviations that are NEVER sentence-final in practice
_NON_SENTENCE_END_ABBREV = {
    "dr", "mr", "mrs", "ms", "prof", "sr", "jr",
    "inc", "ltd", "corp",
    "a.m", "p.m",
    "approx", "est", "dept", "univ", "vol", "ed", "no",
}

# Abbreviations that can end sentences — period IS a boundary when uppercase follows
_MID_OR_END_ABBREV = {
    "etc", "vs", "e.g", "i.e",
    "st", "ave", "blvd",  # Can be sentence-final in addresses
}


def _is_sentence_end(text: str, pos: int) -> bool:
    """Check if a period/exclamation/question at position pos is a sentence boundary."""
    if pos < 0 or pos >= len(text):
        return False
    ch = text[pos]
    if ch not in ".!?…":
        return False

    before = text[:pos].rstrip()
    before_lower = before.lower()
    after = text[pos + 1:]
    after_stripped = after.lstrip()

    # Name-title abbreviations: NEVER a sentence boundary (e.g. "Dr. Smith went.")
    for abbr in sorted(_NON_SENTENCE_END_ABBREV, key=len, reverse=True):
        if before_lower.endswith(abbr):
            prefix_len = len(before) - len(abbr)
            if prefix_len <= 0 or not before[prefix_len - 1].isalpha():
                return False

    # Mid-or-end abbreviations: not a boundary when followed by lowercase ("etc. and more")
    for abbr in sorted(_MID_OR_END_ABBREV, key=len, reverse=True):
        if before_lower.endswith(abbr):
            prefix_len = len(before) - len(abbr)
            if prefix_len <= 0 or not before[prefix_len - 1].isalpha():
                if after_stripped and after_stripped[0].islower():
                    return False
                break

    # Standard boundary: end-of-text, space+uppercase, or space+digit
    if not after_stripped:
        return True
    if after_stripped[0].isupper() or after_stripped[0].isdigit():
        return True
    if after and after[0] == "\n":
        return True
    return False


def _split_sentences(text: str) -> list[str]:
    """Split text into sentences, respecting common abbreviations."""
    result: list[str] = []
    start = 0
    length = len(text)

    for i, ch in enumerate(text):
        if ch in ".!?…":
            if _is_sentence_end(text, i):
                sent = text[start:i + 1].strip()
                if sent:
                    result.append(sent)
                start = i + 1

    # Remainder
    remaining = text[start:].strip()
    if remaining:
        result.append(remaining)

    return result or [text.strip()] if text.strip() else []


# ═══════════════════════════════════════════════════════════════════════════════
# DATA STRUCTURES
# ═══════════════════════════════════════════════════════════════════════════════

@dataclass
class SentenceInfo:
    text: str
    word_count: int
    first_word: str
    has_transition: bool
    is_passive: bool


@dataclass
class ParagraphInfo:
    sentence_count: int
    word_count: int
    text: str


@dataclass
class TextMetrics:
    lang: str
    word_count: int
    sentence_count: int
    char_count: int
    char_count_no_spaces: int
    avg_sentence_length: float
    avg_syllables_per_word: float
    avg_words_per_sentence: float

    # Readability — supported languages
    readability_supported: bool

    # Common readability scores. -1.0 = not available for this language.
    flesch_reading_ease: float
    gunning_fog: float

    # Grade-level / index suite (universal formulas available for all 9 langs;
    # flesch_kincaid_grade is -1.0 for UK/PL which lack a Flesch model)
    flesch_kincaid_grade: float
    smog_index: float
    automated_readability_index: float
    coleman_liau_index: float
    lix: float
    aggregate_grade: str

    # Language-specific formulas
    lang_specific_score: float
    lang_specific_name: str

    # Passive voice
    passive_sentence_count: int
    passive_ratio_pct: float

    # Transition words
    transition_sentence_count: int
    transition_ratio_pct: float

    # Sentence variety
    sentences: list[SentenceInfo] = field(default_factory=list)
    monotony_violations: int = 0
    starter_violations: int = 0

    # Paragraphs
    paragraphs: list[ParagraphInfo] = field(default_factory=list)
    paragraphs_too_long: int = 0
    avg_words_per_paragraph: float = 0.0

    # Keyword
    keyword: str = ""
    keyword_occurrences: int = 0
    keyword_density_pct: float = 0.0
    keyword_in_first_150: bool = False
    keyword_in_title: bool = False

    # Title / Meta
    title_text: str = ""
    title_char_count: int = 0
    title_has_number: bool = False
    title_power_word_count: int = 0
    meta_description: str = ""
    meta_description_char_count: int = 0


# ═══════════════════════════════════════════════════════════════════════════════
# TOKENIZATION
# ═══════════════════════════════════════════════════════════════════════════════

def _word_pattern(lang: str) -> re.Pattern:
    return WORD_PATTERNS.get(lang, WORD_PATTERNS["en"])


def _tokenize_words(text: str, lang: str = "en") -> list[str]:
    return _word_pattern(lang).findall(text.lower())


def _first_word(sentence: str, lang: str = "en") -> str:
    words = _tokenize_words(sentence, lang)
    return words[0] if words else ""


# ═══════════════════════════════════════════════════════════════════════════════
# CORE ANALYSIS
# ═══════════════════════════════════════════════════════════════════════════════

def analyze(
    text: str,
    keyword: str = "",
    title: str = "",
    meta_description: str = "",
    lang: str = "en",
) -> TextMetrics:
    """
    Compute all measurable SEO metrics for a text.

    Args:
        text: Body content (headings + paragraphs).
        keyword: Focus keyword (case-insensitive exact match).
        title: SEO title (H1 or <title>).
        meta_description: Meta description text.
        lang: Language code (en, ru, uk, de, fr, es, pt, it, pl).

    Returns:
        TextMetrics dataclass with all computed values.
    """
    lang = lang.lower()
    if lang not in WORD_PATTERNS:
        print(f"[WARN] Unknown language '{lang}', falling back to 'en'")
        lang = "en"

    # ── Basic counts (deterministic, library-independent) ──────────────
    raw_sentences = _split_sentences(text)
    sentence_count = len(raw_sentences)
    word_count = len(_tokenize_words(text, lang))
    char_count = len(text)
    char_count_no_spaces = len(re.sub(r"\s", "", text))
    avg_sentence_length = (word_count / sentence_count) if sentence_count else 0.0
    avg_syllables_per_word = 0.0

    # ── Readability via ReadSightPy (deterministic, all 9 languages) ────
    readability_supported = lang in READABILITY_LANGS
    fre = gf = fkg = smog = ari = cli = lix_score = -1.0
    lang_score = -1.0
    lang_name = "N/A"
    agg = "N/A"

    if readability_supported and word_count > 0 and sentence_count > 0:
        rs = _get_engine(lang)
        supported = set(rs.get_supported_formulas())

        fre = _nz(_formula_score(rs, supported, "flesch_reading_ease", text))
        gf = _nz(_formula_score(rs, supported, "gunning_fog", text))
        fkg = _nz(_formula_score(rs, supported, "flesch_kincaid_grade_level", text))
        smog = _nz(_formula_score(rs, supported, "smog", text))
        ari = _nz(_formula_score(rs, supported, "ari", text))
        cli = _nz(_formula_score(rs, supported, "coleman_liau", text))
        lix_score = _nz(_formula_score(rs, supported, "lix", text))

        try:
            avg_syllables_per_word = float(rs.average_syllables_per_word(text))
        except Exception:
            avg_syllables_per_word = 0.0

        # Headline language-specific formula (for display/report)
        ls_key, lang_name = LANG_SPECIFIC.get(lang, ("flesch_reading_ease", "Flesch Reading Ease"))
        lang_score = _nz(_formula_score(rs, supported, ls_key, text))

        # Aggregate grade from numeric grade-level formulas
        grades = [g for g in (fkg, gf, smog, cli, ari) if g > 0]
        if grades:
            agg = f"~Grade {round(statistics.median(grades))}"

    # ── Sentence-level analysis ────────────────────────────────────────
    tw_set = TRANSITION_WORDS.get(lang, TRANSITION_WORDS["en"])
    passive_res = PASSIVE_PATTERNS.get(lang, PASSIVE_PATTERNS["en"])

    sentences: list[SentenceInfo] = []
    passive_count = 0
    transition_count = 0

    for s in raw_sentences:
        words = _tokenize_words(s, lang)
        if not words:
            continue
        wc = len(words)
        fw = words[0] if words else ""

        s_lower = s.lower()
        has_transition = any(tw in s_lower for tw in tw_set)
        is_passive = any(pat.search(s) for pat in passive_res)

        if is_passive:
            passive_count += 1
        if has_transition:
            transition_count += 1

        sentences.append(SentenceInfo(
            text=s.strip(),
            word_count=wc,
            first_word=fw,
            has_transition=has_transition,
            is_passive=is_passive,
        ))

    total_sent = len(sentences)
    passive_ratio = (passive_count / total_sent * 100) if total_sent else 0.0
    transition_ratio = (transition_count / total_sent * 100) if total_sent else 0.0

    # ── Sentence monotony ──────────────────────────────────────────────
    monotony_violations = 0
    for i in range(len(sentences) - 2):
        a, b, c = sentences[i].word_count, sentences[i + 1].word_count, sentences[i + 2].word_count
        if abs(a - b) <= 2 and abs(b - c) <= 2:
            monotony_violations += 1

    starter_violations = 0
    for i in range(len(sentences) - 2):
        a = sentences[i].first_word
        b = sentences[i + 1].first_word
        c = sentences[i + 2].first_word
        if a and a == b == c:
            starter_violations += 1

    # ── Paragraph analysis ─────────────────────────────────────────────
    paragraphs_raw = re.split(r"\n\s*\n", text)
    too_long_count = 0
    para_list: list[ParagraphInfo] = []
    total_para_words = 0

    max_para_words = 150 if lang == "en" else 120
    max_para_sents = 3 if lang == "en" else 4

    for p in paragraphs_raw:
        p = p.strip()
        if not p:
            continue
        p_words = len(_tokenize_words(p, lang))
        p_sents = len(_split_sentences(p))
        para_list.append(ParagraphInfo(sentence_count=p_sents, word_count=p_words, text=p))
        total_para_words += p_words
        if p_words > max_para_words or p_sents > max_para_sents:
            too_long_count += 1

    avg_para_words = total_para_words / len(para_list) if para_list else 0.0

    # ── Keyword analysis ───────────────────────────────────────────────
    kw = keyword.lower().strip()
    kw_occurrences = 0
    kw_in_first_150 = False
    kw_in_title = False

    if kw:
        text_lower = text.lower()
        kw_occurrences = len(re.findall(re.escape(kw), text_lower))
        if kw_occurrences > 0 and word_count > 0:
            kw_density = (kw_occurrences * 100) / word_count
        else:
            kw_density = 0.0

        words_list = text_lower.split()[:150]
        first_150 = " ".join(words_list)
        kw_in_first_150 = kw in first_150
        kw_in_title = kw in title.lower() if title else False
    else:
        kw_density = 0.0

    # ── Title / Meta ───────────────────────────────────────────────────
    title_chars = len(title) if title else 0
    title_has_num = bool(re.search(r"\d", title)) if title else False

    pw_set = POWER_WORDS.get(lang, POWER_WORDS["en"])
    title_pw_count = 0
    if title:
        title_lower = title.lower()
        title_pw_count = sum(1 for pw in pw_set if pw in title_lower)

    meta_chars = len(meta_description) if meta_description else 0

    return TextMetrics(
        lang=lang,
        word_count=word_count,
        sentence_count=sentence_count,
        char_count=char_count,
        char_count_no_spaces=char_count_no_spaces,
        avg_sentence_length=avg_sentence_length,
        avg_syllables_per_word=avg_syllables_per_word,
        avg_words_per_sentence=avg_sentence_length,

        readability_supported=readability_supported,
        flesch_reading_ease=fre,
        gunning_fog=gf,
        flesch_kincaid_grade=fkg,
        smog_index=smog,
        automated_readability_index=ari,
        coleman_liau_index=cli,
        lix=lix_score,
        aggregate_grade=agg,
        lang_specific_score=lang_score,
        lang_specific_name=lang_name,

        passive_sentence_count=passive_count,
        passive_ratio_pct=round(passive_ratio, 1),
        transition_sentence_count=transition_count,
        transition_ratio_pct=round(transition_ratio, 1),

        sentences=sentences,
        monotony_violations=monotony_violations,
        starter_violations=starter_violations,

        paragraphs=para_list,
        paragraphs_too_long=too_long_count,
        avg_words_per_paragraph=round(avg_para_words, 1),

        keyword=keyword,
        keyword_occurrences=kw_occurrences,
        keyword_density_pct=round(kw_density, 2),
        keyword_in_first_150=kw_in_first_150,
        keyword_in_title=kw_in_title,

        title_text=title,
        title_char_count=title_chars,
        title_has_number=title_has_num,
        title_power_word_count=title_pw_count,
        meta_description=meta_description,
        meta_description_char_count=meta_chars,
    )


# ═══════════════════════════════════════════════════════════════════════════════
# CHECKLIST SCORING
# ═══════════════════════════════════════════════════════════════════════════════

def score_checklist(m: TextMetrics) -> dict:
    """Map computed metrics to RankWise 49-factor checklist. Returns dict of factor_id → {status, detail, value}."""
    result = {}

    # Title/meta length ranges per language (from readability-params.md)
    title_ranges = {
        "en": (50, 60), "de": (50, 65), "fr": (50, 63), "es": (50, 63),
        "pt": (50, 63), "it": (50, 63), "pl": (50, 65), "ru": (55, 70), "uk": (55, 70),
    }
    meta_ranges = {
        "en": (145, 158), "de": (145, 158), "fr": (145, 158), "es": (145, 158),
        "pt": (145, 158), "it": (145, 158), "pl": (145, 158), "ru": (140, 160), "uk": (140, 160),
    }
    tw_targets = {"en": 30, "ru": 25, "uk": 25, "de": 25, "fr": 25, "es": 25, "pt": 25, "it": 25, "pl": 25}

    # ── K: Keyword ──────────────────────────────────────────────────────
    if m.keyword:
        result["K1"] = {"status": "pass", "detail": f"Keyword set: '{m.keyword}'", "value": m.keyword}
    else:
        result["K1"] = {"status": "fail", "detail": "No focus keyword provided", "value": ""}

    result["K2"] = {"status": "pass" if m.keyword_in_title else "fail",
                    "detail": "Keyword in title" if m.keyword_in_title else "Keyword missing from title",
                    "value": "yes" if m.keyword_in_title else "no"}

    result["K6"] = {"status": "pass" if m.keyword_in_first_150 else "fail",
                    "detail": "Keyword in first 150 words" if m.keyword_in_first_150 else "Keyword not in first 150",
                    "value": "yes" if m.keyword_in_first_150 else "no"}

    if m.keyword_occurrences > 0:
        result["K7"] = {"status": "pass", "detail": f"Keyword in body ({m.keyword_occurrences} occurrences)",
                        "value": str(m.keyword_occurrences)}
    else:
        result["K7"] = {"status": "fail", "detail": "Keyword not found in body", "value": "0"}

    density = m.keyword_density_pct
    if density == 0:
        result["K10"] = {"status": "fail", "detail": "Keyword density: 0%", "value": "0%"}
    elif density < 0.8:
        result["K10"] = {"status": "warning", "detail": f"Keyword density too low: {density:.2f}% (target 0.8–1.5%)",
                         "value": f"{density:.2f}%"}
    elif 0.8 <= density <= 1.5:
        result["K10"] = {"status": "pass", "detail": f"Keyword density: {density:.2f}% (target 0.8–1.5%)",
                         "value": f"{density:.2f}%"}
    elif density <= 3.0:
        result["K10"] = {"status": "warning", "detail": f"Keyword density elevated: {density:.2f}% (target 0.8–1.5%)",
                         "value": f"{density:.2f}%"}
    else:
        result["K10"] = {"status": "fail", "detail": f"Keyword stuffing: {density:.2f}% (target 0.8–1.5%)",
                         "value": f"{density:.2f}%"}

    # ── C: Content Quality ──────────────────────────────────────────────
    if m.word_count >= 1500:
        result["C1"] = {"status": "pass", "detail": f"Word count: {m.word_count} (competitive)", "value": str(m.word_count)}
    elif m.word_count >= 600:
        result["C1"] = {"status": "pass", "detail": f"Word count: {m.word_count} (meets minimum)", "value": str(m.word_count)}
    else:
        result["C1"] = {"status": "fail", "detail": f"Word count: {m.word_count} (min 600)", "value": str(m.word_count)}

    max_para_w = 150 if m.lang == "en" else 120
    result["C2"] = {"status": "fail" if m.paragraphs_too_long > 0 else "pass",
                    "detail": f"Paragraphs too long: {m.paragraphs_too_long} of {len(m.paragraphs)} (>{max_para_w}w)" if m.paragraphs_too_long > 0 else "All paragraphs within limits",
                    "value": f"{m.paragraphs_too_long}/{len(m.paragraphs)}"}

    result["C5"] = {"status": "pass" if m.title_has_number else "fail",
                    "detail": "Number in title" if m.title_has_number else "No number in title",
                    "value": "yes" if m.title_has_number else "no"}

    result["C6"] = {"status": "pass" if m.title_power_word_count >= 2 else "warning",
                    "detail": f"Power words in title: {m.title_power_word_count} (target >=2, lang={m.lang})",
                    "value": str(m.title_power_word_count)}

    # ── Readability (C8) — language-aware via ReadSightPy ──────────────
    if m.readability_supported:
        result["C8"] = _score_readability(m)
    else:
        result["C8"] = {
            "status": "na",
            "detail": f"Readability [N/A]: no ReadSightPy model for lang={m.lang}.",
            "value": "N/A",
        }

    # Passive voice (C9)
    if m.passive_ratio_pct <= 10:
        result["C9"] = {"status": "pass", "detail": f"Passive voice: {m.passive_ratio_pct}% (target <=10%)", "value": f"{m.passive_ratio_pct}%"}
    else:
        result["C9"] = {"status": "fail", "detail": f"Passive voice: {m.passive_ratio_pct}% (target <=10%)", "value": f"{m.passive_ratio_pct}%"}

    # Transition words (C10)
    target_tw = tw_targets.get(m.lang, 30)
    if m.transition_ratio_pct >= target_tw:
        result["C10"] = {"status": "pass", "detail": f"Transition words: {m.transition_ratio_pct}% (target >={target_tw}%)", "value": f"{m.transition_ratio_pct}%"}
    else:
        result["C10"] = {"status": "fail", "detail": f"Transition words: {m.transition_ratio_pct}% (target >={target_tw}%)", "value": f"{m.transition_ratio_pct}%"}

    # Sentence variety (C11)
    result["C11"] = {"status": "pass" if m.monotony_violations == 0 else "fail",
                     "detail": f"Sentence length variety: {'OK' if m.monotony_violations == 0 else f'{m.monotony_violations} monotony violation(s)'}",
                     "value": str(m.monotony_violations)}

    # Sentence starts (C12)
    result["C12"] = {"status": "pass" if m.starter_violations == 0 else "fail",
                     "detail": f"Sentence starts: {'varied' if m.starter_violations == 0 else f'{m.starter_violations} repeated-start violation(s)'}",
                     "value": str(m.starter_violations)}

    # ── T: Title / Meta ─────────────────────────────────────────────────
    t_lo, t_hi = title_ranges.get(m.lang, (50, 60))
    if m.title_char_count == 0:
        result["T3"] = {"status": "fail", "detail": "No title provided", "value": "0 chars"}
    elif t_lo <= m.title_char_count <= t_hi:
        result["T3"] = {"status": "pass", "detail": f"Title length: {m.title_char_count} chars (target {t_lo}-{t_hi})", "value": f"{m.title_char_count} chars"}
    else:
        result["T3"] = {"status": "warning", "detail": f"Title length: {m.title_char_count} chars (target {t_lo}-{t_hi})", "value": f"{m.title_char_count} chars"}

    m_lo, m_hi = meta_ranges.get(m.lang, (145, 158))
    if m.meta_description_char_count == 0:
        result["T4"] = {"status": "fail", "detail": "No meta description provided", "value": "0 chars"}
    elif m_lo <= m.meta_description_char_count <= m_hi:
        result["T4"] = {"status": "pass", "detail": f"Meta length: {m.meta_description_char_count} chars (target {m_lo}-{m_hi})", "value": f"{m.meta_description_char_count} chars"}
    else:
        result["T4"] = {"status": "warning", "detail": f"Meta length: {m.meta_description_char_count} chars (target {m_lo}-{m_hi})", "value": f"{m.meta_description_char_count} chars"}

    return result


def _score_readability(m: TextMetrics) -> dict:
    """Score C8 readability using the language-appropriate metric (ReadSightPy).

    Metric per language (see READABILITY_TARGETS):
      en → FK Grade · de → WSTF · es → Fernández-Huerta · it → Gulpease
      fr/ru/pt → Flesch Reading Ease · uk → LIX · pl → FOG-PL
    """
    target = READABILITY_TARGETS.get(m.lang, READABILITY_TARGETS["en"])
    mode = target["mode"]
    lo, hi = target["range"]

    def band(value: float, value_str: str, *, lower_is_easier: bool) -> dict:
        if value < 0:
            return {"status": "warning", "detail": f"Readability: {value_str} (could not compute)", "value": value_str}
        if lower_is_easier:
            # Below the band (easier) is fine; only the harder side is penalized.
            warn_margin = 3 if mode in ("fkgl", "fogpl") else 10
            if value <= hi:
                return {"status": "pass", "detail": f"Readability: {value_str} (target {lo}-{hi})", "value": value_str}
            if value <= hi + warn_margin:
                return {"status": "warning", "detail": f"Readability: {value_str} (target {lo}-{hi})", "value": value_str}
            return {"status": "fail", "detail": f"Readability too hard: {value_str} (target {lo}-{hi})", "value": value_str}
        # Higher is easier (FRE / FH / Gulpease): in-band pass, near-band warning.
        if lo <= value <= hi:
            return {"status": "pass", "detail": f"Readability: {value_str} (target {lo}-{hi})", "value": value_str}
        if value >= lo - 15:
            return {"status": "warning", "detail": f"Readability: {value_str} (target {lo}-{hi})", "value": value_str}
        return {"status": "fail", "detail": f"Readability: {value_str} (target {lo}-{hi})", "value": value_str}

    if mode == "fkgl":
        v = round(m.flesch_kincaid_grade, 1)
        return band(v, f"FK Grade {v}", lower_is_easier=True)
    if mode == "fogpl":
        v = round(m.lang_specific_score, 1)
        return band(v, f"FOG-PL {v}", lower_is_easier=True)
    if mode == "lix":
        v = round(m.lang_specific_score, 1)
        return band(v, f"LIX {v}", lower_is_easier=True)
    if mode == "wstf":
        v = round(m.lang_specific_score, 1)
        return band(v, f"WSTF {v}", lower_is_easier=True)
    if mode == "fh":
        v = round(m.lang_specific_score, 1)
        return band(v, f"FH {v}", lower_is_easier=False)
    if mode == "gulpease":
        v = round(m.lang_specific_score, 1)
        return band(v, f"Gulpease {v}", lower_is_easier=False)

    # fre (fr / ru / pt and generic fallback)
    v = round(m.flesch_reading_ease, 1)
    return band(v, f"FRE {v}", lower_is_easier=False)


# ═══════════════════════════════════════════════════════════════════════════════
# REPORT GENERATOR
# ═══════════════════════════════════════════════════════════════════════════════

def report(m: TextMetrics) -> str:
    lines = [
        "=" * 60,
        f"  RankWise Validator — Text Metrics Report ({m.lang.upper()})",
        "=" * 60,
        "",
        f"  Language:            {m.lang} {'(readability: supported)' if m.readability_supported else '(readability: N/A)'}",
        f"  Keyword:             {m.keyword or '(not set)'}",
        "",
        "── COUNTS ──",
        f"  Words:               {m.word_count}",
        f"  Sentences:           {m.sentence_count}",
        f"  Characters:          {m.char_count} ({m.char_count_no_spaces} no spaces)",
        f"  Avg sentence length: {m.avg_sentence_length:.1f} words",
        f"  Avg syllables/word:  {m.avg_syllables_per_word:.2f}",
        "",
    ]

    def _fmt(v, suffix=""):
        return f"{v:.1f}{suffix}" if v is not None and v >= 0 else "n/a"

    if m.readability_supported:
        lines += [
            "── READABILITY (ReadSightPy) ──",
            f"  Flesch Reading Ease: {_fmt(m.flesch_reading_ease)} (0-100, higher=easier)",
            f"  Gunning Fog:         {_fmt(m.gunning_fog)}",
            f"  Flesch-Kincaid Grade:{_fmt(m.flesch_kincaid_grade)} (target 7-9 for EN)",
            f"  SMOG Index:          {_fmt(m.smog_index)}",
            f"  ARI:                 {_fmt(m.automated_readability_index)}",
            f"  Coleman-Liau:        {_fmt(m.coleman_liau_index)}",
            f"  LIX:                 {_fmt(m.lix)}",
            f"  Aggregate:           {m.aggregate_grade}",
            f"  Headline ({m.lang_specific_name}): {_fmt(m.lang_specific_score)}",
        ]
    else:
        lines += [
            "── READABILITY ──",
            f"  [N/A] No ReadSightPy model for '{m.lang}'.",
        ]

    lines += [
        "",
        "── LINGUISTIC ──",
        f"  Passive voice:       {m.passive_ratio_pct}% ({m.passive_sentence_count}/{m.sentence_count} sentences, target <=10%)",
        f"  Transition words:    {m.transition_ratio_pct}% ({m.transition_sentence_count}/{m.sentence_count} sentences)",
        f"  Length monotony:     {m.monotony_violations} violation(s)",
        f"  Starter monotony:    {m.starter_violations} violation(s)",
        "",
        "── PARAGRAPHS ──",
        f"  Total paragraphs:    {len(m.paragraphs)}",
        f"  Too long:            {m.paragraphs_too_long}",
        f"  Avg words/paragraph: {m.avg_words_per_paragraph:.1f}",
        "",
        "── KEYWORD ──",
        f"  Occurrences:         {m.keyword_occurrences}",
        f"  Density:             {m.keyword_density_pct}% (target 0.8-1.5%)",
        f"  In first 150 words:  {'yes' if m.keyword_in_first_150 else 'NO'}",
        f"  In title:            {'yes' if m.keyword_in_title else 'NO'}",
        "",
        "── TITLE / META ──",
        f"  Title:               \"{m.title_text}\"",
        f"  Title length:        {m.title_char_count} chars",
        f"  Title has number:    {'yes' if m.title_has_number else 'NO'}",
        f"  Title power words:   {m.title_power_word_count} (target >=2)",
        f"  Meta description:    {m.meta_description_char_count} chars",
        "",
        "── CHECKLIST SCORING ──",
    ]

    scores = score_checklist(m)
    for fid, info in sorted(scores.items()):
        icon = {"pass": "[PASS]", "fail": "[FAIL]", "warning": "[WARN]", "na": "[N/A]"}.get(info["status"], "[???]")
        lines.append(f"  {icon} {fid}: {info['detail']}")

    return "\n".join(lines)
