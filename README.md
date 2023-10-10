# Запуск сервера
1. ## Активируйте виртуальное окружение
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

2. ## Проверьте настройки базы данных в `config/settings.py`: NAME, USER, PASSWORD
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'djangohwdb',  
        'USER': 'ваш_пользователь',  
        'PASSWORD': 'ваш_пароль',  
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

3. ## Создайте базу данных
```bash
psql -U postgres
CREATE DATABASE djangohwdb
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

## Форма обратной связи транслирует данные в файл catalog/form_data.txt
## Форма создание товара транслирует данные в базу данных Postgres
