"""Shared fixtures and helpers for validator tests."""

import pytest
from pathlib import Path


BENCHMARKS_DIR = Path(__file__).parent.parent / "benchmarks"


MULTILINGUAL_TEXTS = {
    "en": "Playing games has always been thought to be important to the development of well-balanced and creative children. However, we must consider that adults also benefit greatly from play.",
    "ru": "Игры всегда считались важными для развития сбалансированных и творческих детей. Однако мы должны учитывать, что взрослые тоже получают большую пользу от игр.",
    "uk": "Ігри завжди вважалися важливими для розвитку збалансованих і творчих дітей. Однак ми повинні враховувати, що дорослі також отримують велику користь від ігор.",
    "de": "Spiele wurden schon immer als wichtig für die Entwicklung von ausgeglichenen und kreativen Kindern angesehen. Wir müssen jedoch berücksichtigen, dass auch Erwachsene stark von Spielen profitieren.",
    "fr": "Jouer a toujours été considéré comme important pour le développement d'enfants équilibrés et créatifs. Cependant, nous devons considérer que les adultes bénéficient également grandement du jeu.",
    "es": "Jugar siempre se ha considerado importante para el desarrollo de niños equilibrados y creativos. Sin embargo, debemos considerar que los adultos también se benefician enormemente del juego.",
    "pt": "Jogar sempre foi considerado importante para o desenvolvimento de crianças equilibradas e criativas. No entanto, devemos considerar que os adultos também se beneficiam muito do jogo.",
    "it": "Giocare è sempre stato considerato importante per lo sviluppo di bambini equilibrati e creativi. Tuttavia, dobbiamo considerare che anche gli adulti traggono grandi benefici dal gioco.",
    "pl": "Granie zawsze było uważane za ważne dla rozwoju zrównoważonych i kreatywnych dzieci. Musimy jednak wziąć pod uwagę, że dorośli również czerpią ogromne korzyści z grania.",
}


EN_SAMPLE = (
    "Search engine optimization is essential for any website. "
    "Proper keyword research helps you understand what your audience is looking for. "
    "The best content strategies combine SEO with genuine value for readers. "
    "Many sites fail because they focus too much on keywords and too little on quality. "
    "A balanced approach will always outperform a one-dimensional strategy over time."
)


def load_benchmark(name: str) -> str:
    """Load a benchmark text file."""
    path = BENCHMARKS_DIR / name
    if not path.exists():
        pytest.skip(f"Benchmark file not found: {name}")
    return path.read_text(encoding="utf-8")


@pytest.fixture
def en_text():
    return EN_SAMPLE


@pytest.fixture
def multilingual():
    return MULTILINGUAL_TEXTS
