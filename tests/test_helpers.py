from unittest.mock import patch
from io import StringIO

from library.helpers import (
    add_book_flow,
    delete_book_flow,
    search_books_flow,
    show_all_books_flow,
    update_status_flow,
)


def test_add_book_flow(service, teardown_service, reset_data_file):
    """
    Тест добавления книги с вводом данных.
    """

    with patch("builtins.input",
               side_effect=["Война и мир", "Лев Толстой", "1869"]):
        add_book_flow(service)
        assert len(service.repository.books_dict) == 1


def test_delete_book_flow(service, teardown_service, reset_data_file):
    """
    Тест удаления книги с вводом данных.
    """

    service.add_book("Война и мир", "Лев Толстой", 1869)
    with patch("builtins.input", side_effect=["0"]):
        delete_book_flow(service)
        assert len(service.repository.books_dict) == 0


def test_search_books_flow(service, teardown_service, reset_data_file):
    """
    Тест поиска книги с вводом данных.
    """

    service.add_book("Война и мир", "Лев Толстой", 1869)
    service.add_book("Анна Каренина", "Лев Толстой", 1877)
    service.add_book("Крутая книга для теста", "Лев Толстой", 1877)

    with patch("builtins.input", side_effect=["", "", ""]), \
            patch("sys.stdout", new_callable=StringIO) as mock_stdout:
        search_books_flow(service)

        assert "Книг по заданным параметрам не найдено." \
            in mock_stdout.getvalue()

    with patch("builtins.input", side_effect=["", "Лев Толстой", "1877"]), \
            patch("sys.stdout", new_callable=StringIO) as mock_stdout:
        search_books_flow(service)
        result = mock_stdout.getvalue()
        assert "Лев Толстой" in result
        assert "1877" in result
        assert "1869" not in result
        assert "ID" in result
        assert "Название" in result
        assert "Статус" in result
        assert "Крутая книга для теста" in result


def test_show_all_books_flow(service, teardown_service, reset_data_file):
    """
    Тест отображения книг.
    """

    with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
        show_all_books_flow(service)

        assert "Сейчас в библиотеке нет книг." in mock_stdout.getvalue()

    service.add_book("Война и мир", "Лев Толстой", 1869)
    service.add_book("Анна Каренина", "Лев Толстой", 1877)
    service.add_book("Крутая книга для теста", "Лев Толстой", 1877)

    with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
        show_all_books_flow(service)
        result = mock_stdout.getvalue()
        assert "Война и мир" in result
        assert "+" in result
        assert "Лев Толстой" in result
        assert "1869" in result
        assert "Крутая книга для теста" in result
        assert "ID" in result
        assert "Название" in result
        assert "Статус" in result


def test_update_status_flow(service, teardown_service, reset_data_file):
    """
    Тест обновления статуса с вводом данных.
    """

    service.add_book("Война и мир", "Лев Толстой", 1869)

    with patch("builtins.input", side_effect=["0", "выдана"]), \
            patch("sys.stdout", new_callable=StringIO) as mock_stdout:
        update_status_flow(service)

        assert "Статус книги с идентификатором 0 успешно изменён на 'выдана'."\
            in mock_stdout.getvalue()
