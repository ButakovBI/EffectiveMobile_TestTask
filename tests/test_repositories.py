import json
import os


def test_add_book(empty_data_repository, teardown_service, reset_data_file):
    """
    Тест добавления книги в репозиторий.
    """

    result = empty_data_repository.add_book("Война и мир", "Лев Толстой", 1869)
    assert result == "Книга успешно добавлена!"
    assert len(empty_data_repository.books_dict) == 1
    assert empty_data_repository.books_dict[0]["title"] == "Война и мир"
    assert empty_data_repository.title_index["Война и мир"] == [0]


def test_delete_book(empty_data_repository, teardown_service, reset_data_file):
    """
    Тест удаления книги.
    """

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
    """
    Тест поиска книг по различным параметрам.
    """

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
    assert 'Война и мир' in result
    assert '1877' in result
    assert '+' in result


def test_repository_initialization(
        not_empty_data_repository,
        teardown_service,
        reset_data_file):
    """
    Тест инициализации репозитория: проверка, что данные загружаются корректно.
    """

    data = {"books": {0: {"title": "Война и мир",
                          "author": "Лев Толстой",
                          "year": 1869,
                          "status": "в наличии"},
                      1: {"title": "Анна Каренина",
                          "author": "Лев Толстой",
                          "year": 1877,
                          "status": "в наличии"}},
            "current_id": 2}
    assert not_empty_data_repository.books_dict == data["books"]
    assert not_empty_data_repository.current_id == data["current_id"]
    assert not_empty_data_repository.title_index["Война и мир"] == [0]
    assert not_empty_data_repository.author_index["Лев Толстой"] == [0, 1]
    assert not_empty_data_repository.year_index[1869] == [0]
    assert not_empty_data_repository.year_index[1877] == [1]


def test_load_data(not_empty_data_repository, reset_data_file):
    """
    Тест метода _load_data: проверка загрузки корректных данных из файла.
    """

    data = {"books": {0: {"title": "Война и мир",
                          "author": "Лев Толстой",
                          "year": 1869,
                          "status": "в наличии"},
                      1: {"title": "Анна Каренина",
                          "author": "Лев Толстой",
                          "year": 1877,
                          "status": "в наличии"}},
            "current_id": 2}
    assert not_empty_data_repository.books_dict == data["books"]
    assert not_empty_data_repository.current_id == data["current_id"]
    assert not_empty_data_repository.title_index["Война и мир"] == [0]
    assert not_empty_data_repository.author_index["Лев Толстой"] == [0, 1]
    assert not_empty_data_repository.year_index[1869] == [0]


def test_load_data_file_not_found(
        empty_data_repository,
        teardown_service,
        reset_data_file):
    """
    Тест метода _load_data: проверка поведения при отсутствии файла.
    """

    if os.path.exists("tests/data.json"):
        os.remove("tests/data.json")

    assert empty_data_repository.books_dict == {}
    assert empty_data_repository.current_id == 0


def test_load_data_invalid_json(
        empty_data_repository,
        teardown_service,
        reset_data_file):
    """
    Тест метода _load_data: проверка поведения при повреждённом JSON-файле.
    """

    with open("tests/data.json", "w", encoding="utf-8") as file:
        file.write("{invalid_json}")

    assert empty_data_repository.books_dict == {}
    assert empty_data_repository.current_id == 0

    if os.path.exists("tests/data.json"):
        os.remove("tests/data.json")


def test_save_data(empty_data_repository, teardown_service, reset_data_file):
    """
    Тест метода _save_data: проверка, что данные корректно сохраняются в файл.
    """

    empty_data_repository.add_book("Война и мир", "Лев Толстой", 1869)

    with open("tests/empty_data.json", "r", encoding="utf-8") as file:
        data = json.load(file)

    assert data["books"] == {
        "0": {
            "title": "Война и мир",
            "author": "Лев Толстой",
            "year": 1869,
            "status": "в наличии"}}
    assert data["current_id"] == 1
