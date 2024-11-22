import json
from collections import defaultdict

from library.utils import print_books


class BookRepository:

    """
    Отвечает за управление хранилищем книг, включая добавление, удаление и поиск.
    """

    def __init__(self, data_file: str ="src/data.json") -> None:

        """
        Инициализирует словарь для хранения книг и индексы для быстрого поиска.
        Загружает данные из файла при запуске.

        :param data_file: Файл, из которого загружаются данные книг.
        """

        self.data_file = data_file
        self.books_dict = {}
        self.title_index = defaultdict(list)
        self.author_index = defaultdict(list)
        self.year_index = defaultdict(list)
        self.current_id = 0

        self._load_data()


    def _load_data(self) -> None:

        """
        Загружает данные из файла data.json и восстанавливает индексы.
        """

        try:
            with open(self.data_file, "r", encoding="utf-8") as file:
                data = json.load(file)
                self.books_dict = {int(book_id): book for book_id, book in data.get("books", {}).items()}
                self.current_id = int(data.get("current_id", 0))

                for book_id, book in self.books_dict.items():
                    book_id = int(book_id) 
                    self.title_index[book["title"]].append(book_id)
                    self.author_index[book["author"]].append(book_id)
                    self.year_index[book["year"]].append(book_id)
            
        except (FileNotFoundError, json.JSONDecodeError):
            self.books_dict = {}
            self.current_id = 0


    def _save_data(self) -> None:

        """
        Сохраняет текущие данные books_dict и current_id в файл data.json.
        """

        data = {
            "books": self.books_dict,
            "current_id": self.current_id,
        }
        with open(self.data_file, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)


    def add_book(self, title: str, author: str, year: int) -> str:
    
        '''
        Добавляет книгу в библиотеку.

        :param title: Название книги.
        :param author: Автор книги.
        :param year: Год написания книги.
        :return: Сообщение об успешности добавления книги.
        '''

        self.books_dict[self.current_id] = {"title": title, "author": author, "year": year, "status": "в наличии"}
        self.title_index[title].append(self.current_id)
        self.author_index[author].append(self.current_id)
        self.year_index[year].append(self.current_id)

        self.current_id += 1

        self._save_data()
        return "Книга успешно добавлена!"


    def delete_book(self, id: int) -> str:

        '''
        Удаляет книгу из библиотеки.

        :param id: Идентификатор книги, подлежащей удалению.
        :return: Сообщение об успешности удаления книги.
        '''

        message = "Книга успешно удалена."
        if id in self.books_dict:
            book = self.books_dict[id]
            self.title_index[book["title"]].remove(id)
            if not self.title_index[book["title"]]:
                del self.title_index[book["title"]]

            self.author_index[book["author"]].remove(id)
            if not self.author_index[book["author"]]:
                del self.author_index[book["author"]]

            self.year_index[book["year"]].remove(id)
            if not self.year_index[book["year"]]:
                del self.year_index[book["year"]]

            del self.books_dict[id]
            self._save_data()
        else:
            message = "Данной книги не существует."

        return message


    def get_all_books(self) -> str:

        """
        Возвращает список всех книг. 

        :return: Список всех книг в удобночитаемом формате.
        """

        message = "Сейчас в библиотеке нет книг."
        if self.books_dict:
            message = print_books(self.books_dict)
        
        return message


    def search_books(self, title: str = None, author: str = None, year: int = None) -> str:
    
        '''
        Ищет книги в библиотеке по названию, автору и году. 

        :param title: Название книги.
        :param author: Автор книги.
        :param year: Год написания книги.
        :return: Сообщение с результатами поиска.
        '''

        book_ids_title = set(self.title_index[title]) if title and title in self.title_index else set()
        book_ids_author = set(self.author_index[author]) if author and author in self.author_index else set()
        book_ids_year = set(self.year_index[year]) if year and year in self.year_index else set()

        if title or author or year:
            book_ids = book_ids_title or book_ids_author or book_ids_year
            if title:
                book_ids &= book_ids_title
            if author:
                book_ids &= book_ids_author
            if year:
                book_ids &= book_ids_year
        else:
            book_ids = set()

        message = "Книг по заданным параметрам не найдено."
        if book_ids:
            books = {book_id: self.books_dict[book_id] for book_id in book_ids}
            message = f"Список книг по заданным параметрам:\n{print_books(books)}"

        return message
    

    def change_status(self, id: int, status: str) -> str:

        '''
        Изменяет статус книги по идентификатору.

        :param id: Идентификатор книги.
        :param status: Статус книги.
        :return: Сообщение с результатом операции.
        '''
        
        message = ""
        if id not in self.books_dict:
            message = f"Книги с идентификатором {id} нет в библиотеке."
        else:
            self.books_dict[id]["status"] = status
            self._save_data()
            message = f"Статус книги с идентификатором {id} успешно изменён на '{status}'."
        
        return message
        