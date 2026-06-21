# Readability Parameters — Per Language

> Readability scoring, passive voice rules, sentence/paragraph length targets.

---

## META LENGTH PARAMETERS — All Languages

| Language | Title (chars) | Description (chars) | Notes |
|----------|--------------|---------------------|-------|
| EN | 50–60 | 145–158 | Search engines typically display first 60 chars of title, 155–160 of description |
| RU | 55–70 | 140–160 | Cyrillic characters are wider; some regional search engines show longer titles |
| DE | 50–65 | 145–158 | Compound words can inflate character count; count carefully |
| FR | 50–63 | 145–158 | Accented characters count as 1 char in SERP rendering |
| ES | 50–63 | 145–158 | Similar to EN; slightly more tolerance for longer words |
| PT | 50–63 | 145–158 | Brazilian vs European Portuguese: same SERP limits |
| IT | 50–63 | 145–158 | Relatively compact — stick to lower end of range |
| PL | 50–65 | 145–158 | Polish declensions can create longer words; count carefully |
| UK | 55–70 | 140–160 | Same as RU — Cyrillic width considerations |
| **All others** | 50–60 | 145–158 | Default to EN limits when language not listed |

### OG tag character limits (all languages)
| Tag | Min | Max |
|-----|-----|-----|
| og:title | 40 | 60 |
| og:description | 100 | 200 |
| twitter:title | 40 | 60 |
| twitter:description | 100 | 200 |

---

## ENGLISH

### Flesch-Kincaid Grade Level
- **Target:** Grade 7–9 (general audience), Grade 10–12 (technical/professional)
- **Formula:** 0.39 × (words/sentences) + 11.8 × (syllables/words) - 15.59
- **Translate to:** "Easy to read", "Fairly easy", "Standard"

### Flesch Reading Ease
- **Target:** 60–70 (standard), 50–60 (fairly difficult for technical)
- **Formula:** 206.835 - 1.015 × (words/sentences) - 84.6 × (syllables/words)

### Passive Voice
- **Target:** ≤10% of sentences
- **Count:** Any form of "to be" + past participle where subject is acted upon
- **Fix:** Convert to active: "The form was submitted by the user" → "The user submitted the form"

### Sentence Length
- **Short:** 2–8 words (use for emphasis, hooks, transitions)
- **Medium:** 9–17 words (workhorse — most sentences)
- **Long:** 18–25 words (explanation, context, reasoning)
- **Max:** 25 words (split at 26+)
- **Exception:** 1 sentence of 30+ per 500 words allowed for complex explanation

### Paragraph Length
- **Max:** 150 words or 3 sentences
- **Ideal:** 2–4 sentences, 40–80 words
- **Mobile:** No paragraph wider than 5 lines on mobile (approx 80 words)

### Transition Words
- **Target:** ≥30% of sentences contain transitions
- **Examples:** however, therefore, because, although, specifically, for example, in contrast, similarly, consequently, notably

### Subheading Distribution
- **Frequency:** Every 200–350 words
- **Format:** H2 for major sections, H3 for sub-sections

---

## RUSSIAN / РУССКИЙ

### Адаптированная читаемость
- **Цель:** Уровень 7–9 класса школы (широкая аудитория)
- **Аналог Flesch:** Индекс удобочитаемости (формула Оборневой)
- **Ориентир:** средняя длина предложения 10–15 слов

### Пассивный залог
- **Цель:** ≤8% предложений (русский использует пассив реже английского)
- **Маркеры:** «был сделан», «будет проведён», «является выполненным», возвратные глаголы (-ся)
- **Исправление:** Замена на активный залог: «документ был подписан» → «мы подписали документ»

### Длина предложений
- **Короткие:** 3–8 слов
- **Средние:** 9–18 слов
- **Длинные:** 19–30 слов (русский допускает длиннее английского)
- **Максимум:** 30 слов

### Длина абзаца
- **Максимум:** 120 слов или 4 предложения
- **Идеал:** 2–4 предложения

### Переходные слова (≥25% предложений)
однако, поэтому, так как, хотя, например, в частности, в то же время, кроме того, следовательно, тем не менее, в отличие от, в результате, также

### Частота подзаголовков
- Каждые 250–400 слов

### Особые маркеры ИИ
- ✓ Писать живо, без канцеляризмов
- ✗ Избегать: «осуществлять», «являться», «данный», «посредством», «в рамках», «в целях»
- ✓ Использовать конкретные глаголы: «сделали», «запустили», «посчитали»
- ✓ Естественный порядок слов — не копировать английский

---

## UKRAINIAN / УКРАЇНСЬКА

### Адаптована читабельність
- **Ціль:** Рівень 7–9 класу (широка аудиторія)
- **Орієнтир:** середня довжина речення 10–18 слів
- Українські тексти природно довші за англійські — допускається довжина до 32 слів

### Пасивний стан
- **Ціль:** ≤8% речень
- **Маркери:** «було зроблено», «буде проведено», «є виконаним»
- **Виправлення:** «документ було підписано» → «ми підписали документ»

### Довжина речень
- **Короткі:** 3–8 слів | **Середні:** 9–18 | **Довгі:** 19–32 | **Максимум:** 32

### Довжина абзацу
- **Максимум:** 120 слів або 4 речення

### Перехідні слова (≥25%)
однак, тому, через те що, хоча, наприклад, зокрема, водночас, крім того, отже, тим не менш, на відміну від, у результаті, також

### Частота підзаголовків
- Кожні 250–400 слів

### Особливі маркери
- ✓ Писати живо, без канцеляризмів
- ✗ Уникати русизмів: «із-за» → «через», «так як» → «бо»/«тому що», «приймати участь» → «брати участь»
- ✗ Уникати: «являтися», «даний», «здійснювати», «посередництвом»
- ✓ Використовувати конкретні дієслова: «зробили», «запустили», «порахували»
- ✓ Природний порядок слів
- ✓ Українська базова теплота — використовуйте розмовні зв'язки: «А», «І», «Тобто», «Ну», «До речі», «Чесно кажучи»

---

## GERMAN / DEUTSCH

### Lesbarkeitsindex (LIX)
- **Ziel:** 40–50 (mittelschwer — Zeitungstext)
- **Formel:** (Wörter/Sätze) + (lange Wörter × 100 / Wörter)
- **Lange Wörter:** >6 Buchstaben

### Passiv
- **Ziel:** ≤10% der Sätze
- **Marker:** «wird gemacht», «wurde durchgeführt», «ist optimiert worden»
- **Korrektur:** Aktiv formulieren. «Der Prozess wird optimiert» → «Wir optimieren den Prozess»

### Satzlänge
- **Kurz:** 4–10 Wörter
- **Mittel:** 11–20 Wörter
- **Lang:** 21–30 Wörter (Deutsch toleriert längere Sätze)
- **Maximum:** 30 Wörter

### Absatzlänge
- **Maximum:** 120 Wörter oder 4 Sätze

### Übergangswörter (≥25% der Sätze)
jedoch, deshalb, weil, obwohl, zum Beispiel, insbesondere, darüber hinaus, daher, dennoch, im Gegensatz dazu, infolgedessen, außerdem

### Besondere Marker
- ✗ Nominalstil vermeiden: «Durchführung einer Optimierung» → «optimieren»
- ✗ «Man sollte» → direkt formulieren
- ✓ Modalpartikel natürlich einsetzen: «doch», «ja», «halt», «eben»

---

## FRENCH / FRANÇAIS

### Lisibilité
- **Cible:** Niveau B1–B2 (grand public), C1 (technique)
- **Indice Gunning Fog adapté:** viser 10–14

### Voix passive
- **Cible:** ≤10% des phrases
- **Correction:** «Le rapport a été rédigé» → «Nous avons rédigé le rapport»

### Longueur de phrase
- **Courte:** 5–10 mots
- **Moyenne:** 11–20 mots
- **Longue:** 21–28 mots
- **Maximum:** 28 mots

### Longueur de paragraphe
- **Maximum:** 120 mots ou 4 phrases

### Mots de transition (≥25% des phrases)
cependant, donc, parce que, bien que, par exemple, en particulier, de plus, par conséquent, néanmoins, en revanche, ainsi, également

---

## SPANISH / ESPAÑOL

### Legibilidad (Fernández Huerta)
- **Objetivo:** 60–70 (normal — prensa general)

### Voz pasiva
- **Objetivo:** ≤10%

### Longitud de frase
- **Corta:** 5–10 palabras | **Media:** 11–22 | **Larga:** 23–30 | **Máximo:** 30

### Palabras de transición (≥25%)
sin embargo, por lo tanto, porque, aunque, por ejemplo, en particular, además, por consiguiente, no obstante, en contraste, asimismo, también

---

## PORTUGUESE / PORTUGUÊS

### Legibilidade
- **Objetivo:** Frases de 12–20 palavras (média)

### Voz passiva
- **Objetivo:** ≤10%

### Comprimento de frase
- **Curta:** 5–10 | **Média:** 11–22 | **Longa:** 23–30 | **Máximo:** 30

### Palavras de transição
no entanto, portanto, porque, embora, por exemplo, em particular, além disso, consequentemente, apesar disso, por outro lado

---

## ITALIAN / ITALIANO

### Leggibilità (Indice Gulpease)
- **Obiettivo:** 50–60 (leggibilità media — giornali)

### Voce passiva
- **Obiettivo:** ≤10%
- **Correzione:** «È stato fatto» → «Abbiamo fatto»

### Lunghezza frase
- **Corta:** 5–10 | **Media:** 11–22 | **Lunga:** 23–30 | **Massimo:** 30

### Parole di transizione
tuttavia, quindi, perché, sebbene, per esempio, in particolare, inoltre, di conseguenza, nonostante, al contrario, anche

---

## POLISH / POLSKI

### Czytelność (Indeks Jasnopisu)
- **Cel:** 40–50 (tekst średnio trudny)

### Strona bierna
- **Cel:** ≤10%

### Długość zdania
- **Krótkie:** 5–10 | **Średnie:** 11–20 | **Długie:** 21–28 | **Maksimum:** 28

### Słowa przejścia
jednak, dlatego, ponieważ, chociaż, na przykład, w szczególności, ponadto, w rezultacie, niemniej jednak, natomiast, również

---

## QUICK READABILITY CHECKLIST (ALL LANGUAGES)

1. ☐ Average sentence ≤ 20 words
2. ☐ Maximum sentence ≤ 25 words (EN), ≤ 28 (FR, PL), ≤ 30 (RU, DE, ES, PT, IT), ≤ 32 (UK) — see per-language sections above
3. ☐ Passive voice ≤ 10% of sentences
4. ☐ Paragraphs ≤ 150 words (120 for non-EN)
5. ☐ Transition words ≥ 25% of sentences (30% for EN)
6. ☐ No 3+ consecutive sentences of same structure
7. ☐ No paragraph >5 lines on mobile screen
