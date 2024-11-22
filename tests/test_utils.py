from unittest.mock import patch

from library.utils import print_books, get_non_empty_input, \
    get_int_input, get_status_input


def test_print_books():
    """
    Тест форматирования списка книг.
    """

    books = {0: {"title": "Война и мир",
                 "author": "Лев Толстой",
                 "year": 1869,
                 "status": "в наличии"}}
    result = print_books(books)
    assert "Война и мир" in result
    assert "Лев Толстой" in result


def test_get_int_input():
    """
    Тест получения целого числа от пользователя.
    """

    with patch("builtins.input", side_effect=["", "abc", "123"]):
        result = get_int_input("Введите число: ")
        assert result == 123

    with patch("builtins.input", return_value=""):
        result = get_int_input("Введите число: ", allow_empty=True)
        assert result is None

    with patch("builtins.input", return_value="-456"):
        result = get_int_input("Введите число: ")
        assert result == -456

    with patch("builtins.input", return_value="456"):
        result = get_int_input("Введите число: ")
        assert result == 456


def test_get_non_empty_input():
    """
    Тест получения непустой строки.
    """

    with patch("builtins.input", side_effect=["  ", "Тест"]):
        result = get_non_empty_input("Введите строку: ")
        assert result == "Тест"


def test_get_status_input():
    """
    Тест получения статуса из входных данных.
    """

    with patch("builtins.input", side_effect=["  ", "статус", "выдана"]):
        result = get_status_input()
        assert result == "выдана"
