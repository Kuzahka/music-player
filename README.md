### Проект: Музыкальный плеер

Музыкальный плеер на Django, предоставляющий функционал регистрации,
авторизации, управления плейлистом и добавления треков. Проект
использует веб-сервер nginx для обработки запросов пользователей
и Gunicorn в качестве WSGI-сервера. Для хранения данных используется 
PostgreSQL. Проект упакован в docker-compose. Кроме того, с помощью
Django REST Framework создано API с аутентификацией по JWT токену.



### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/Kuzahka/voice-text.git
```

```
cd Shum
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



Запустить проект:

```
flask run
```
