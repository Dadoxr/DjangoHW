# Запуск сервера
1. ## Активируйте виртуальное окружение и настройте переменные окружения .env
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

touch DjangoHW/.env
vim .env
```

```python
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
EMAIL_FILE_PATH = os.path.join(BASE_DIR, 'sent_emails')

EMAIL_HOST_USER = 'YOUR_YANDEX_PASSWD'
EMAIL_HOST_PASSWORD = 'YOUR_MAIL'

DB_NAME = "YOUR_DB_NAME"
DB_USER = "YOUR_DB_USER"
DB_PASSWD = 'YOUR_DB_PASSWD'
```

2. ## Проверьте настройки базы данных в `config/settings.py`: HOST, PORT
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        '...',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

3. ## Создайте базу данных, если ее нет
```bash
psql -U postgres
CREATE DATABASE YOUR_DB_NAME
/q
```

4. ## Добавьте миграции и фикстуры
```bash
python3 manage.py migrate
python3 manage.py loaddata catalog_data.json
```

5. ## Запустите сервис
```bash
python3 manage.py runserver
```

# Ссылки на сайт
- `127.0.0.1:8000/` - **Все продукты**
- `127.0.0.1:8000/contacts` - **Контакты**
- `127.0.0.1:8000/product` - **Вывести первый продукт**
- `127.0.0.1:8000/add_product` - **Добавить продукт**
- `127.0.0.1:8000/blog` - **Страница блога**
- `127.0.0.1:8000/blog/create/` - **Добавить статью**


## Форма обратной связи транслирует данные в файл catalog/form_data.txt
## Форма создание товара транслирует данные в базу данных Postgres
