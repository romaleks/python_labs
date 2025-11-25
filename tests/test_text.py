import pytest
from src.lib.text import normalize, tokenize, count_freq, top_n


# ------------------------
# TEST normalize
# ------------------------


@pytest.mark.parametrize(
    "text, expected",
    [
        ("Привет  мир", "привет мир"),
        ("  Текст   с   пробелами   ", "текст с пробелами"),
        ("Ёжик ёлку нашёл", "ежик елку нашел"),
        ("", ""),
    ],
)
def test_normalize_basic(text, expected):
    assert normalize(text) == expected


def test_normalize_casefold_off():
    assert normalize("ПрИвЕт", casefold=False) == "ПрИвЕт"


def test_normalize_yo2e_off():
    assert normalize("ёж", yo2e=False) == "ёж"


# ------------------------
# TEST tokenize
# ------------------------


@pytest.mark.parametrize(
    "text, expected",
    [
        ("hello world", ["hello", "world"]),
        ("тест-токенизации слов", ["тест-токенизации", "слов"]),
        ("слово1 слово2", ["слово1", "слово2"]),
        ("!!!", []),
        ("", []),
    ],
)
def test_tokenize(text, expected):
    assert tokenize(text) == expected


# ------------------------
# TEST count_freq
# ------------------------


def test_count_freq_basic():
    tokens = ["a", "b", "a", "a", "c", "b"]
    assert count_freq(tokens) == {"a": 3, "b": 2, "c": 1}


def test_count_freq_empty():
    assert count_freq([]) == {}


# ------------------------
# TEST top_n
# ------------------------


def test_top_n_basic():
    freq = {"a": 3, "b": 1, "c": 2}
    assert top_n(freq, 2) == [("a", 3), ("c", 2)]


def test_top_n_equal_freq_sorted_alphabetically():
    freq = {"beta": 1, "alpha": 1, "gamma": 1}
    # одинаковая частота → сортировка по алфавиту
    assert top_n(freq, 3) == [
        ("alpha", 1),
        ("beta", 1),
        ("gamma", 1),
    ]


def test_top_n_more_than_size():
    freq = {"one": 2, "two": 1}
    # просим топ-10, но слов всего 2
    assert top_n(freq, 10) == [("one", 2), ("two", 1)]


def test_top_n_zero():
    freq = {"a": 1, "b": 2}
    assert top_n(freq, 0) == []
