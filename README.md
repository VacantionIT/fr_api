# Тестовое задание по созданию API для системы опросов пользователей

Описание задания в файле [task_desc.md](task_desc.md)


## Инструкция по разворачиванию приложения
### Установка

```
cd fr_api
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

### Запуск сервера
```
python manage.py runserver
```


## Документация по API
После запуска сервера, документация доступна в следующих форматах:

[swagger](http://127.0.0.1:8000/api/swagger/)

[json swagger](http://127.0.0.1:8000/api/swagger.json)

[yaml swagger](http://127.0.0.1:8000/api/swagger.yaml)

[redoc](http://127.0.0.1:8000/api/redoc/)
