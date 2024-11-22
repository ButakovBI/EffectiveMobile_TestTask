from library.repositories import BookRepository
from library.services import LibraryService
from library.helpers import add_book_flow, delete_book_flow, \
    search_books_flow, \
    show_all_books_flow, update_status_flow


def main():
    repository = BookRepository()
    library = LibraryService(repository)

    actions = {
        '1': lambda: add_book_flow(library),
        '2': lambda: delete_book_flow(library),
        '3': lambda: search_books_flow(library),
        '4': lambda: show_all_books_flow(library),
        '5': lambda: update_status_flow(library),
    }

    while True:
        print('\nМеню:')
        print('1. Добавить книгу')
        print('2. Удалить книгу')
        print('3. Найти книгу')
        print('4. Показать все книги')
        print('5. Изменить статус книги')
        print('6. Выйти')

        choice = input('Выберите действие: ').strip()
        if choice == '6':
            print("Выход из программы. До свидания!")
            break

        action = actions.get(choice)
        if action:
            action()
        else:
            print("Ошибка: Выберите корректный пункт меню.")


if __name__ == '__main__':
    main()
