from library.services import LibraryService
from library.utils import get_non_empty_input, get_int_input, get_status_input, print_answer, str_is_int


def add_book_flow(library: LibraryService) -> None:

    """
    Логика добавления книги.
    """

    title = get_non_empty_input("Введите название: ")
    author = get_non_empty_input("Введите автора: ")
    year = get_int_input("Введите год издания вида -num(год до н.э.) или num, где num - число, состоящее из римских цифр: ")
    print_answer(library.add_book(title, author, year))


def delete_book_flow(library: LibraryService) -> None:

    """
    Логика удаления книги.
    """
    
    book_id = get_int_input("Введите ID книги: ")
    print_answer(library.delete_book(book_id))


def search_books_flow(library: LibraryService) -> None:

    """
    Логика поиска книг.
    """

    title = input("Введите название (или оставьте пустым): ").strip() or None
    author = input("Введите автора (или оставьте пустым): ").strip() or None
    year = input("Введите год вида -num(год до н.э.) или num, где num - число, состоящее из римских цифр(или оставьте пустым): ").strip()
    year = int(year) if str_is_int(year) else None
    response = library.search_books(title, author, year)

    if response == "Книг по заданным параметрам не найдено.":
        print_answer(response)
    else:
        print(response)


def show_all_books_flow(library: LibraryService) -> None:

    """
    Логика отображения всех книг.
    """

    response = library.repository.get_all_books()
    if response == "Сейчас в библиотеке нет книг.":
        print_answer(response)
    else:
        print(response)


def update_status_flow(library: LibraryService) -> None:

    """
    Логика обновления статуса книги.
    """

    book_id = get_int_input("Введите ID книги: ")
    status = get_status_input()
    print_answer(library.change_status(book_id, status))
