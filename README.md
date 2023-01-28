# infra_sp2

Задание в рамках обучения технологии Docker

## YamDb

<b>YaMDb</b> - сервис, в котором хранится информация по произведениям.</br>
Каждое произведение относится к какой-либо одной какой-либо одной категории ("Фильмы", "Музыка", "Книги") и к нескольким жанрам (например, "Драма", "Фантастика").</br>
Добавлять произведения, категории и жанры может только администратор.</br>
Пользователи могут смотреть отзывы, комментарии и оценки других пользователей, а авторизованниые пользователи могут их еще и добавлять.</br>
Более подробная информация о функционале сервиса и примерах запроса - [на странице проекта](https://github.com/MrSlavencio/api_yamdb)

## Как развернуть проект
Клонировать репозиторий и перейти в него в командной строке:
```
git clone git@github.com:MrSlavencio/infra_sp2.git
```
```
cd infra_sp2
```
Перейти в директорию *infra*:
```
cd infra
```
В директории *infra* создать файл `.env`:
```
nano .env
```
Заполнить `.env`:
```
DB_ENGINE=django.db.backends.postgresql
DB_NAME=postgres
POSTGRES_USER=<логин для подключения к БД>
POSTGRES_PASSWORD=<пароль для подключения к БД>
DB_HOST=db
DB_PORT=5432
```
Соберите контейнер:
```
docker-compose up -d
```
По очереди выполните команды:
```
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser
docker-compose exec web python manage.py collectstatic --no-input
```
<b>Контейнер запущен на `http://127.0.0.1/`!</b></br>
Проверьте работу, перейдя по ссылке: [127.0.0.1/admin/](http://127.0.0.1/admin/)
</br></br>
Для остановки контейнера используйте команду:
```
docker-compose down -v
```

## Об авторе

Автор проекта - **Кобзев Вячеслав**, студент когорты 44 факультета Бэкенд разработки Яндекс-практикума.</br>
Контакты для связи: </br>
[*telegram*](https://t.me/mrslavencio "MrSlavencio")
