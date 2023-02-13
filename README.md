### Описание проекта:
Проект представляет собой социальную сеть для публикации личных дневников. Реализован API для всех моделей приложения. По запросу можно просмотреть все записи автора. Пользователи могут делать запросы к чужим страницам, комментировать записи различных авторов, подписываться на них. API доступен только аутентифицированным пользователям. Реализованы возможность поиска и фильтрации данных. Добавлена пагинация ответов. Модели написаны с использованием вьюсетов.

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
https://github.com/VadimNT/api_final_yatube.git
```

```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

```
source env/bin/activate
```

```
python3 -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```

##### После запуска проекта, документация будет доступна по адресу:
```http://localhost:8000/redoc/```

### Примеры запросов и ответов. 

##### Получение GET запроса .../api/v1/posts/ 

Пример ответа:

```json
{
  "count": 123,
  "next": "http://api.example.org/accounts/?offset=400&limit=100",
  "previous": "http://api.example.org/accounts/?offset=200&limit=100",
  "results": [
    {
      "id": 0,
      "author": "string",
      "text": "string",
      "pub_date": "2021-10-14T20:41:29.648Z",
      "image": "string",
      "group": 0
    }
  ]
}
```
Выполнение POST запроса постов .../api/v1/posts/ 
```json
{
  "text": "string",
  "image": "string",
  "group": 0
}
``` 
Пример ответа: 
```json
{
  "id": 0,
  "author": "string",
  "text": "string",
  "pub_date": "2019-08-24T14:15:22Z",
  "image": "string",
  "group": 0
}
```
##### Получение всех комментариев к публикации через GET запрос .../api/v1/posts/{post_id}/comments/ 

Пример ответа: 
```json
[
  {
    "id": 0,
    "author": "string",
    "text": "string",
    "created": "2019-08-24T14:15:22Z",
    "post": 0
  }
]
```
#####  Добавление нового комментария к публикации через POST .../api/v1/posts/{post_id}/comments/ 

Пример ответа: 

```json
{
  "id": 0,
  "author": "string",
  "text": "string",
  "created": "2019-08-24T14:15:22Z",
  "post": 0
} 
```
##### Получение информации о сообществе по id через GET запрос .../api/v1/groups/id/ 

Пример ответа: 
```json
{
  "id": 0,
  "title": "string",
  "slug": "string",
  "description": "string"
}
```
##### GET-запрос возвращает все подписки пользователя, сделавшего запрос GET .../api/v1/follow/

Пример ответа: 
```json
[
  {
    "user": "string",
    "following": "string"
  }
]
```
##### Подписка пользователя от имени которого сделан запрос на пользователя переданного в теле запроса POST .../api/v1/posts/{post_id}/comments/ 

Пример ответа: 

```json
{
  "user": "string",
  "following": "string"
}
```
