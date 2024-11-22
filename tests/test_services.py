def test_add_book(empty_data_repository, teardown_service, reset_data_file):
    """Тест добавления книги в репозиторий."""
    result = empty_data_repository.add_book("Война и мир", "Лев Толстой", 1869)
    assert result == "Книга успешно добавлена!"
    assert len(empty_data_repository.books_dict) == 1
    assert empty_data_repository.books_dict[0]["title"] == "Война и мир"
    assert empty_data_repository.title_index["Война и мир"] == [0]


def test_delete_book(empty_data_repository, teardown_service, reset_data_file):
    """Тест удаления книги."""
    empty_data_repository.add_book("Война и мир", "Лев Толстой", 1869)
    result = empty_data_repository.delete_book(0)
    assert result == "Книга успешно удалена."
    assert len(empty_data_repository.books_dict) == 0

    result = empty_data_repository.delete_book(1)
    assert result == "Данной книги не существует."


def test_search_books(
        empty_data_repository,
        teardown_service,
        reset_data_file):
    """Тест поиска книг по различным параметрам."""
    empty_data_repository.add_book("Война и мир", "Лев Толстой", 1869)
    empty_data_repository.add_book("Анна Каренина", "Лев Толстой", 1877)

    result = empty_data_repository.search_books(title="Война и мир")
    assert "Война и мир" in result
    assert "Лев Толстой" in result

    result = empty_data_repository.search_books(author="Лев Толстой")
    assert "Анна Каренина" in result

    result = empty_data_repository.search_books(year=1877)
    assert "Анна Каренина" in result

    result = empty_data_repository.search_books(title="Неизвестная книга")
    assert result == "Книг по заданным параметрам не найдено."

    result = empty_data_repository.search_books()
    assert result == "Книг по заданным параметрам не найдено."


def test_change_status(
        empty_data_repository,
        teardown_service,
        reset_data_file):
    """
    Тест изменения статуса книги.
    """

    empty_data_repository.add_book("Война и мир", "Лев Толстой", 1869)
    result = empty_data_repository.change_status(0, "выдана")
    assert result == \
        "Статус книги с идентификатором 0 успешно изменён на 'выдана'."
    assert empty_data_repository.books_dict[0]["status"] == "выдана"

    result = empty_data_repository.change_status(1, "выдана")
    assert result == "Книги с идентификатором 1 нет в библиотеке."


def test_get_all_books(
        empty_data_repository,
        teardown_service,
        reset_data_file):
    """
    Тест вывода всех книг.
    """

    result = empty_data_repository.get_all_books()
    assert result == "Сейчас в библиотеке нет книг."
    empty_data_repository.add_book("Война и мир", "Лев Толстой", 1869)
    empty_data_repository.add_book("Анна Каренина", "Лев Толстой", 1877)
    result = empty_data_repository.get_all_books()
    assert "Война и мир" in result
    assert "1877" in result
    assert "+" in result
