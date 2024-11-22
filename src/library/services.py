from library.repositories import BookRepository


class LibraryService:

    """
    Управляет бизнес-логикой библиотеки: добавление, удаление, изменение статуса, поиск.
    """

    def __init__(self, repository: BookRepository) -> None:
        self.repository = repository


    def add_book(self, title: str, author: str, year: int) -> str:

        '''
        Добавляет книгу через репозиторий.
        
        :param title: Название книги.
        :param author: Автор книги.
        :param year: Год написания книги.
        :return: Сообщение об успешности добавления книги.
        '''

        return self.repository.add_book(title, author, year)


    def delete_book(self, id: int) -> str:

        """
        Удаляет книгу через репозиторий.

        :param book_id: Идентификатор книги.
        :return: Сообщение об успешности удаления книги.
        """

        return self.repository.delete_book(id)


    def search_books(self, title: str = None, author: str = None, year: int = None) -> str:
        
        """
        Ищет книги через репозиторий.

        :param title: Название книги.
        :param author: Автор книги.
        :param year: Год написания книги.
        :return: Список найденных книг в табличном формате.
        """

        return self.repository.search_books(title, author, year)


    def change_status(self, id: int, status: str) -> str:

        '''
        Изменяет статус книги по идентификатору.

        :param id: Идентификатор книги.
        :param status: Статус книги.
        :return: Сообщение с результатом операции.
        '''

        return self.repository.change_status(id, status)
        
