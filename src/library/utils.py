def print_books(books: dict[int, dict]) -> str:

    '''
    Формирует табличное представление списка книг в стиле PostgreSQL.

    :param books: Словарь, где ключ — ID книги, а значение — словарь с данными книги.
    :return: Строка, содержащая табличное представление книг.
    '''

    headers = [("ID", "id"), ("Название", "title"), ("Автор", "author"), ("Год", "year"), ("Статус", "status")]

    book_list = [
        {"id": book_id, **book_data} for book_id, book_data in books.items()
    ]

    column_widths = []
    for header, key in headers:
        max_data_length = max(
            len(str(book[key])) for book in book_list
        ) if book_list else 0
        column_widths.append(max(len(header), max_data_length))

    row_separator = "+" + "+".join("-" * (w + 2) for w in column_widths) + "+"
    header_row = "|" + "|".join(
        f" {header.ljust(column_widths[i])} " for i, (header, _) in enumerate(headers)
    ) + "|"

    data_rows = []
    for book in book_list:
        row = "|" + "|".join(
            f" {str(book[key]).ljust(column_widths[i])} " for i, (_, key) in enumerate(headers)
        ) + "|"
        data_rows.append(row)

    table = [row_separator, header_row, row_separator] + data_rows + [row_separator]

    return "\n".join(table)



def print_answer(message: str) -> None:

    """
    Возвращает ответ пользователю в удобночитаемом формате.

    :param message: Сообщение пользователю.
    """

    border = '+' + '-' * (len(message) + 4) + '+'
    framed_message = f"{border}\n|  {message}  |\n{border}"
    print(framed_message)


def str_is_int(value: str) -> bool:
    return value.isdigit() or (len(value) > 1 and value[0] == '-' and value[1:].isdigit())


def get_int_input(prompt: str, allow_empty: bool = False) -> int:

    """
    Получает целое число от пользователя.

    :param prompt: Текст для ввода.
    :param allow_empty: Если True, разрешает пустой ввод (возвращает None).
    :return: Целое число или None.
    """

    break_flag = False
    while not break_flag:
        user_input = input(prompt).strip()
        if allow_empty and not user_input:
            return None
        if str_is_int(user_input):
            return int(user_input)
        
        print("Ошибка: Введите корректное число.")


def get_non_empty_input(prompt: str) -> str:

    """
    Получает непустую строку от пользователя.
    
    :param prompt: Текст для ввода.
    :return: Непустая строка.
    """
    
    break_flag = False
    while not break_flag:
        user_input = input(prompt).strip()
        if user_input:
            return user_input
        print("Ошибка: Поле не может быть пустым. Попробуйте снова.")


def get_status_input() -> str:

    """
    Получает корректный статус книги от пользователя.

    :return: Строка с корректным статусом.
    """

    valid_statuses = ["в наличии", "выдана"]
    break_flag = False
    while not break_flag:
        status = input(f"Введите новый статус ({'/'.join(valid_statuses)}): ").strip()
        if status in valid_statuses:
            return status
        print(f"Ошибка: Введен некорректный статус. Доступные статусы: {', '.join(valid_statuses)}.")
