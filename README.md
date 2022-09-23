# Сервис уведомлений
Cервис по созданию платежных форм для товаров. Интегрируется с API платежной системой stripe.

## Описание задания

- Django Модель Item с полями (name, description, price) 
API с двумя методами:
- GET /buy/{id}, c помощью которого можно получить Stripe Session Id для оплаты выбранного Item. При выполнении этого метода c бэкенда с помощью python библиотеки stripe должен выполняться запрос stripe.checkout.Session.create(...) и полученный session.id выдаваться в результате запроса
- GET /item/{id}, c помощью которого можно получить простейшую HTML страницу, на которой будет информация о выбранном Item и кнопка Buy. По нажатию на кнопку Buy должен происходить запрос на /buy/{id}, получение session_id и далее  с помощью JS библиотеки Stripe происходить редирект на Checkout форму stripe.redirectToCheckout(sessionId=session_id)
- Залить решение на Github, описать запуск в Readme.md
- Опубликовать свое решение чтобы его можно было быстро и легко протестировать. Решения доступные только в виде кода на Github получат низкий приоритет при проверке.

### Как запустить dev-версию 
Скачайте код:
```sh
git clone https://github.com/ZusmanOne/payment_stripe.git
```

Перейдите в каталог проекта:
```sh
cd payment_stripe
```
[Установите Python](https://www.python.org/), если этого ещё не сделали.

Проверьте, что `python` установлен и корректно настроен. Запустите его в командной строке:
```sh
python --version
```

В каталоге проекта создайте виртуальное окружение:
```sh
python -m venv venv
```
Активируйте его. На разных операционных системах это делается разными командами:

- Windows: `.\venv\Scripts\activate`
- MacOS/Linux: `source venv/bin/activate`

Установите зависимости в виртуальное окружение:
```sh
pip install -r requirements.txt
```
Настройка: создать файл `.env` в каталоге `payment_project/` со следующими настройками:

- `DEBUG` — дебаг-режим. Поставьте `True`.
- `SECRET_KEY` — секретный ключ проекта. Он отвечает за шифрование на сайте. 
- `ALLOWED_HOSTS` — [см. документацию Django](https://docs.djangoproject.com/en/3.1/ref/settings/#allowed-hosts)
- `DB_NAME` - имя бд
- `DB_USER`- имя юзера
- `DB_PASSWORD`- пароль юзера
- `DB_PORT`=5432
- `DB_HOST` - localhost(для запуска в докере замените значение на 'db')
- `PUBLIC_STRIPE_KEY` - зарегистрируйетсь в [Stripe](https://stripe.com/) и получите соответствующий API ключ в разделе developers
- `SECRET_STRIPE_KEY` - зарегистрируйетсь в [Stripe](https://stripe.com/) и получите соответствующий API ключ в разделе developers

Применить миграции

```sh
python manage.py migrate
```

Запустить сервер
```sh
python manage.py runserver
```

Сервис имеют следующую маршрутизацию

```http://127.0.0.1:8000/``` - список всех товаров

```http://127.0.0.1:8000/buy/<pk>/``` - получить Stripe Session Id товара

```http://127.0.0.1:8000/item/<pk>``` - получить простейшую HTML страницу c детальной информацией выбранного товара и кнопка Buy по нажатию которой , сформируется платежная форма из stripe


***
## Запуск тестов
``` 
python manage.py test
```
### Сервис так же обернут в докер, что бы запустить проект в докере наберите команду:

``` 
docker-compose -f docker-compose.yml up  --build
```


