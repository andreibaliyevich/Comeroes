# Comeroes


### Heroes of Comics - интернет-магазин комиксов, игрушек, одежды и других товаров связанных с комиксами (кинокомиксами).


## Описание проекта

Сайт ориентирован на сеть магазинов в нескольких городах. Для этого в приложении "main" определяется модель Store, которая хранит контактную информацию и время работы о конкретном магазине.
В этом же приложении реализована утилита перевода валюты по текущему курсу через API.

Приложение "accounts" через модель OSUser хранит пользователей. Модель пользователей переделана под регистрацию / авторизацию через Email. Поле username удалено. Добавлены новые поля к профилю пользователя.
Регистрация подтверждается переходом по уникальной ссылке из письма отправленного на email пользователя, указанного при регистрации.
У пользователей имеется возможность добавлять несколько адресов, один из которых можно установить, как основной. Пользователи могут изменить пароль, удалить аккаунт, а также сбросить пароль и задать новый.

Приложение "products" позволяет администраторам добавлять производителей товаров и разные типы самих товаров с разными значениями и характеристиками. К товарам можно загружать не ограниченное количество изображений (модель ProductImage), а также добавлять информацию о количестве в определенном магазине (модель Warehouse).
Пользователи имеют возможность оставить один отзыв к одному товару. Сами отзывы можно лайкнуть / дизлайкнуть. При добавлении отзыва обновляется рейтинг товара через сигнал post_save.
Товары можно просматривать сеткой или списком. Реализована сортировка товаров, а также постраничный вывод. Реализована фильтрация товаров, учитывающая разные типы товаров и валюту, установленную у пользователя.

Приложение "cart" хранит по каждому пользователю корзину товаров в сессиях. Для управления корзинами создан класс Cart. Пользователи имеют возможность добавлять / удалять товары из корзины, используя запросы ajax. Также количество товаров можно изменить на странице корзины.

Приложение "coupons" позволяет администраторам добавлять купоны ограниченные сроком действия со скидкой в процентном соотношении. Пользователь может применить купон на странице корзины.

Приложение "orders" сохраняет детали заказов пользователей (информацию о пользователе, адрес доставки или указание на магазин, примененный купон и скидка, итоговая стоимость товаров, каждый товар, количество этого товара и его стоимость). Зарегистрированные пользователи имеют возможность просматривать детали заказов и их продвижение.

Приложение "wishlist" сохраняет в базе данных желаемые товары пользователей. Товары в список желаний могут добавлять только зарегистрированные пользователи.

Приложение "newsletter" реализует подписку и рассылку email-писем. Подписка подтверждается переходом по уникальной ссылке из письма, отправленного на указанный email. Учитываются также и зарегистрированные пользователи с таким email.

Приложение "support" реализует обмен сообщениями между зарегистрированными пользователями и администраторами в случае возникновения вопросов.

На сайте реализован перевод на русский, белорусский и английский языки.


## Установка

Для запуска проекта испльзуется Docker.

##### 1. Клонировать репозиторий

    git clone https://github.com/andreibaliyevich/Comeroes.git

##### 2. Перейти в папку репозитория

    cd Comeroes

##### 3. Создать файл .env с переменными окружения в папке src

Например:

    SECRET_KEY=secret_key
    SQL_NAME=sql_name
    SQL_USER=sql_user
    SQL_PASSWORD=sql_password
    EMAIL_HOST_USER=email_host_user
    EMAIL_HOST_PASSWORD=email_host_password
    EMAIL_HOST_RECEIVER=email_host_receiver
    EXCHANGERATE_API_KEY=exchangerate_api_key

##### 4. Создать файл .env с переменными окружения в папке postgres

Например:

    POSTGRES_DB=sql_name
    POSTGRES_USER=sql_user
    POSTGRES_PASSWORD=sql_password

##### 5. Создать образ

    docker-compose build

##### 6. Запустить bash в сервисе django

    docker-compose run django bash

##### 7. Применить миграции

    python manage.py migrate

##### 8. Скомпилировать файлы переводов

    django-admin compilemessages

##### 9. Создать суперпользователя

    python manage.py createsuperuser

##### 10. Выйти из bash

    exit

##### 11. Запустить контейнер

    docker-compose up


## Bootstrap Theme

В верстке сайта используется тема Bootstrap "[Cartzilla – Multipurpose eCommerce Template](https://themes.getbootstrap.com/product/cartzilla-bootstrap-e-commerce-template-ui-kit/)" по лицензии "[The Full Standard License](https://themes.getbootstrap.com/licenses/)".


## Лицензия

[GNU General Public License version 3](https://opensource.org/licenses/GPL-3.0)

Copyright © 2020 Andrei Baliyevich
