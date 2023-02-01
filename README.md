# infra_sp2

Задание в рамках обучения технологии Docker

## YamDb

<b>YaMDb</b> - сервис, в котором хранится информация по произведениям.</br>
Каждое произведение относится к какой-либо одной какой-либо одной категории ("Фильмы", "Музыка", "Книги") и к нескольким жанрам (например, "Драма", "Фантастика").</br>
Добавлять произведения, категории и жанры может только администратор.</br>
Пользователи могут смотреть отзывы, комментарии и оценки других пользователей, а авторизованниые пользователи могут их еще и добавлять.</br>
Более подробная информация о функционале сервиса и примерах запроса - [на странице проекта](https://github.com/MrSlavencio/api_yamdb)

## Стек

* requests==2.26.0
* django==2.2.16
* djangorestframework==3.12.4
* PyJWT==2.1.0
* pytest==6.2.4
* pytest-django==4.4.0
* pytest-pythonpath==0.7.3
* pandas==1.3.5
* djangorestframework-simplejwt==4.7.2
* django-filter==2.4.0
* gunicorn==20.0.4
* psycopg2-binary==2.8.6
* [Docker](https://docs.docker.com/)
* [NGINX](https://nginx.org/ru/)

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
docker-compose exec web python manage.py loaddata fixtures.json
```
<b>Контейнер запущен на `http://127.0.0.1/`!</b></br>
Проверьте работу, перейдя по ссылке: [127.0.0.1/admin/](http://127.0.0.1/admin/)
</br></br>
Для остановки контейнера используйте команду:
```
docker-compose down -v
```

## Пример запросов к API
#### GET-запрос на `/api/v1/titles/{title_id}/reviews/`
Получение списка всех отзывов
#### POST-запрос на `/api/v1/titles/{title_id}/reviews/`
Добавление нового отзыва (доступно авторизированным пользователям)
```json
{
    "text": "perfecto!",
    "score": 1
}
```
#### PATCH-запрос на `/api/v1/titles/{title_id}/reviews/{review_id}/comments/{comment_id}/`
Частичное обновление комментария к отзыву по id (доступно только автору комментария, администратору или модератору)
```json
{
    "text": "это просто прекрасно!"
}
```
#### GET-запрос на `/api/v1/titles/`
Получение списка всех произведений
```response (json)
{
    "count": 32,
    "next": "http://127.0.0.1:8000/api/v1/titles/?limit=5&offset=5",
    "previous": null,
    "results": [
        {
            "id": 1,
            "name": "Побег из Шоушенка",
            "year": 1994,
            "rating": 10,
            "description": null,
            "genre": [
                {
                    "name": "Драма",
                    "slug": "drama"
                }
            ],
            "category": {
                "name": "Фильм",
                "slug": "movie"
            }
        },
        ...
        ]
}
```


## Rest-API

Документацию по API Вы можете прочитать, запустив проект по ссылке ```/redoc/```

## Об авторе

Автор проекта - **Кобзев Вячеслав**, студент когорты 44 факультета Бэкенд разработки Яндекс-практикума.</br>
Контакты для связи: </br>
[*telegram*](https://t.me/mrslavencio "MrSlavencio")
