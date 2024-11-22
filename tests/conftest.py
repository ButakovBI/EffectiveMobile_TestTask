import json
import os
import pytest
from library.repositories import BookRepository
from library.services import LibraryService


@pytest.fixture
def empty_data_repository():
    """
    Фикстура для создания BookRepository
    с пустой библиотекой перед тестом.
    """
    return BookRepository("tests/empty_data.json")


@pytest.fixture
def not_empty_data_repository():
    """
    Фикстура для создания BookRepository
    с непустой библиотекой перед тестом.
    """

    return BookRepository("tests/not_empty_data.json")


@pytest.fixture
def service(empty_data_repository):
    """
    Фикстура для создания LibraryService перед тестом.
    """

    return LibraryService(empty_data_repository)


@pytest.fixture
def reset_data_file():
    """
    Фикстура для очистки файла data.json перед тестом.
    """

    def reset():
        with open("tests/empty_data.json", "w", encoding="utf-8") as file:
            json.dump({"books": {}, "current_id": 0}, file)

    reset()
    yield reset


@pytest.fixture
def teardown_service():
    """
    Фикстура для удаления файла data.json после теста.
    """

    yield
    if os.path.exists("tests/empty_data.json"):
        os.remove("tests/empty_data.json")
