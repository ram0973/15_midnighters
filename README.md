# Решение задачи [№15](https://devman.org/challenges/15/) с сайта [devman.org](https://devman.org)

## Условие задачи:

В базе devman хранится информация о том кто и когда отправил задачу 
на проверку. 
Получить её можно с помощью [АПИ](http://devman.org/api/challenges/solution_attempts/?page=2)

Давай выясним кто отправлял задачи на проверку после 24:00.

Рекомендуемые библиотеки: requests и pytz.

## Системные требования

```
Python 3.5.2+
win-unicode-console
requests
pendulum
```

## Установка

Windows

```    
git clone https://github.com/ram0973/15_midnighters.git
cd 15_midnighters
(Windows) pip install -r requirements.txt
(Linux) pip3 install -r requirements.txt
```
    
## Описание работы

```
Скрипт выводит список всех пользователей, которые сдавали задания с 
0 до 05:59:59 часов 
```

## Запуск

```
(Windows) python seek_dev_midnighters.py
(Linux) python3 seek_dev_midnighters.py
```
 
## Лицензия

[MIT](http://opensource.org/licenses/MIT)