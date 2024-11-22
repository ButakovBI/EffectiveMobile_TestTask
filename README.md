# Приложение для управления репозиторием книг

Это консольное приложение, которое позволяет управлять хранилищем книг, включая добавление, удаление, поиск, отображение всех книг и изменение их статуса. Приложение использует объектно-ориентированный подход и хранит данные в JSON-файле, в соответствии с требованиями из тестового задания. Оно поддерживает быстрый поиск благодаря индексированию по названию, автору и году выпуска.

---

### **Основные возможности**

Приложение предоставляет следующие функции:

- **Добавление книги**: Введите данные о новой книге, и она будет добавлена в репозиторий.
- **Удаление книги**: Удалите книгу по её ID.
- **Поиск книги**: Найдите книгу по названию, автору и/или году выпуска.
- **Показ всех книг**: Отобразите все книги в репозитории.
- **Изменение статуса книги**: Измените статус книги.

---

### **Как запустить приложение**

1. **Клонирование репозитория**:

   Сначала клонируйте репозиторий с кодом:

   ```bash
   git clone https://github.com/ButakovBI/EffectiveMobile_TestTask.git
   cd EffectiveMobile_TestTask
   ```

2. **Установка зависимостей**:

   Установите необходимые зависимости из файла `requirements.txt`:

   ```bash
   pip install -r requirements.txt
   ```

3. **Запуск приложения**:

   Для того чтобы запустить программу, выполните команду:

   ```bash
   python3 src/main.py
   ```

   или

   ```bash
   make
   ```

4. **Взаимодействие с приложением**:

   После запуска приложения в консоли появится меню с доступными действиями:

   ```text
   Меню:
   1. Добавить книгу
   2. Удалить книгу
   3. Найти книгу
   4. Показать все книги
   5. Изменить статус книги
   6. Выйти
   ```

   Введите номер соответствующего действия для выполнения.

---

### **Доступные действия в консоли**

1. **Добавить книгу**:
   - Введите номер `1` и заполните данные о книге: название, автор, год выпуска.
   
2. **Удалить книгу**:
   - Введите номер `2` и укажите ID книги, которую хотите удалить.
   
3. **Найти книгу**:
   - Введите номер `3` и выберите критерий поиска: название, автор и/или год.
   
4. **Показать все книги**:
   - Введите номер `4`, чтобы увидеть список всех книг в репозитории.

5. **Изменить статус книги**:
   - Введите номер `5` и выберите книгу, чтобы изменить её статус.

6. **Выйти**:
   - Введите номер `6`, чтобы выйти из программы.

---

### **Преимущества реализации**

1. **Использование JSON для хранения данных**:
   - Данные о книгах хранятся в JSON-файле, что делает их легко доступными и позволяет сохранять информацию между сессиями программы.

2. **Быстрый поиск и индексация**:
   - Книги индексируются по названию, автору и году, что позволяет за O(1) находить необходимые записи.

3. **Модульность**:
   - Каждая функциональность (добавление книги, поиск, удаление и т. д.) реализована в отдельных функциях, что упрощает поддержку и расширение приложения.

4. **Легкость в тестировании**:
   - Приложение поддерживает модульные тесты, что помогает гарантировать правильность работы всех функций.

5. **Чистота и читаемость кода**:
   - Код снабжен подробными docstring'ами, а также использует аннотации типов для улучшения понимания и поддерживаемости. Это помогает разработчикам легко ориентироваться в проекте.

6. **Автоматизация с помощью Makefile**:
   - Процесс линтинга, тестирования и покрытия кода автоматизирован через `Makefile`, что позволяет легко запускать все необходимые процессы одной командой и обеспечивать стабильность кода.

7. **Поддержка покрытия кода**:
   - Использование инструмента для анализа покрытия тестами, такого как `coverage`, позволяет отслеживать, какие части кода были протестированы, и повышать качество тестов. В данном приложении на момент сдачи тестового задания 100% покрытие кода тестами.

8. **Линтинг и автоформатирование**:
   - Код проверяется на стиль с использованием `flake8`, а также автоформатируется с помощью `autopep8`, что помогает поддерживать единообразие стиля кода в проекте.

9. **Простота в расширении**:
    - Модульная структура приложения позволяет легко добавлять новые функции, например, новые критерии поиска или дополнительные действия с книгами, без необходимости переписывать существующий код.

---

### **Структура проекта**

```
EffectiveMobile_TestTask/   
├── src/                         # Исходный код приложения     
│   ├── main.py                  # Главный файл для запуска     
│   ├── library/                 # Папка с логикой работы с книгами     
│   │   ├── __init__.py              
│   │   ├── helpers.py           # Вспомогательные функции для работы с книгами     
│   │   ├── repositories.py      # Управление хранилищем книг    
│   │   ├── services.py          # Управление бизнес-логикой библиотеки     
│   │   └── utils.py             # Вспомогательные функции для ввода и вывода     
├── tests/                       # Папка с тестами      
│   ├── __init__.py                    
│   ├── conftest.py              # Файл для фикстур    
│   ├── not_empty_data_json.py   # JSON с данными о книгах для тестирования     
│   ├── test_helpers.py          # Тесты для содержимого helpers.py      
│   ├── test_repositories.py     # Тесты для содержимого repositories.py     
│   ├── test_services.py         # Тесты для содержимого services.py    
│   └── test_utils.py            # Тесты для содержимого utils.py    
│      
├── Makefile                     # Файл для автоматизации задач (линтинг, тесты, покрытие)    
├── pyproject.toml               # Конфигурационный файл для pytest    
├── requirements.txt             # Файл с зависимостями (без лишних доп. библиотек)       
├── .github/                     
│   └── workflows/               # Папка для конфигураций GitHub Actions    
│       └── ci.yml               # Конфигурация CI/CD для GitHub Actions
├── README.md                    # Описание проекта            
└── requirements.txt             # Файл с зависимостями       
```

---

### **Команды Makefile**

Для выполнения стандартных задач, таких как линтинг, тестирование и сборка отчета о покрытии, можно использовать команды Makefile.

- `make all`      — Выполняет линтинг, тесты и проверку покрытия.
- `make test`     — Запускает все тесты и проверяет покрытие.
- `make style`    — Выполняет линтинг с помощью `flake8` и автоформатирование с `autopep8`.
- `make coverage` — Генерирует HTML отчет о покрытии.
- `make clean`    — Очищает временные файлы и отчеты о покрытии.
- `make help`     — Отображает описание доступных команд.

---

### **CI/CD с GitHub Actions**

Проект использует автоматизацию с помощью GitHub Actions. После каждого пуша в репозиторий, автоматически запускается пайплайн CI/CD, который выполняет следующие действия:

1. **Установка зависимостей**.
2. **Запуск линтинга** с использованием `flake8`.
3. **Запуск тестов** с использованием `pytest`.
4. **Генерация отчета о покрытии** с использованием `coverage`.

Конфигурация GitHub Actions для CI/CD находится в файле `.github/workflows/ci.yml`.