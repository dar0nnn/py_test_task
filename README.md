# Тестовое

## Как развернуть
```shell script
docker-compose up --build -d
```
Джанго будет жить на стандартном порту 8000, бд на 5434
Дефолтный админ root pw test

## Комментарии и недоработки
Оно все реализовано на стандартных классах джанги, которые не требуют тестов. 
Можно конечно написать что то типо assert True, но это перебор.
ДжангоРест на ModelSerializer просто не заведется без миграций нормальных :D

Когда делаешь логаут перекидывает на страницу admin/logout. Не стал с этим парится,
знаю что легко пофиксить, но глаз уже стал замыливаться.

Юзер может прилепить рута куда нибудь, да и они вообще по дефолту не разнесены на группы.
Тоже решил оставить до лучших времен. Сфокусировался чисто на решение тестового задания.

Шаблоны html нагло взяты из интернета и немного допилены. Но опять же - почему нет?)

Бд решил юзануть Postgresql, потому что вроде из разговора услышал, что она используется.
Хотя sqlite более чем справилось бы с задачей :D

Подумывал попарится чутка с nginx чтобы в settings.py DEBUG = False поставить,
чтобы темплейты не отваливась, но показалось, что в рамках тестового это будет лишнее.

Названия классов - в жизни бы такое не вставил, но сейчас было тупо лень под
тестовое придумывать каждый класс отдельно. Решил сделать это тупо в лоб в стиле Java :D:D:D