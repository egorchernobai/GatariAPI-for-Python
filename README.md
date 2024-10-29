# GatariAPI-for-Python
API of Osu!Gatari for Python
for installing: pip install gatariapi
# Ru FAQ
Это простенькая библеотека, которая парсит json с API сайта gatari.pw.
Я решил сделать это потому что не знал чем себя занять, не ожидайте чего то серьезного.
Также там возможно будут ошибки, соре, ибо я еще только учусь питону
# Ru Guide 
Т.к библеотека еще в бете, то реализовано там не много функций оригинального API.
Но все же я ее когда нибудь доделаю
1) 1 класс что реализован на данный момент - это user_info
Пример:
```python
from GatariAPI import user_info

id = 1000                              #id юзера, который идет после gatari.pw/u/xxxxx. Например 1000
print(user_info(id).user_info())
```
На самом деле можно обьявить класс user_info, а затем использовать его функции.
```python
from GatariAPI import user_info

user = user_info(1000)
print(user.user_info())
```
На вывод в этих случаях идет json код, который можно использовать как словарь и вызывать например так:
```python
from GatariAPI import user_info

user = user_info(1000)
info = user.user_info()
print(info['username']) #mixa_zxc
```
Но в библеотеке уже созданы методы чтобы не парится со словарями(но если вам нужно, то можно юзать и так как в примере выше)
Вызываются эти методы по названиям переменных самого json: abbr, username...
```python
from GatariAPI import user_info

user = user_info(1000)
print(user.username()) #mixa_zxc
```
Если вы заметили сходство, то вы молодец! Все названия функций были скопированы для более простого изучения и использования библеотеки!
2) класс - это user_stats
Пример:
```python
from GatariAPI import user_stats

id = 1000
mode = 0                    #как вы уже заметили, тут введена новая переменная mode, она отвечает за мод осу(standart - 0, taiko - 1, catch - 2, mania - 3)
user = user_stats(id, mode)
print(user.user_stats())
```
на вывод также дается json, каждое название переменной перенесено в функцию.
```python
from GatariAPI import user_stats

id = 1000
mode = 0                    
user = user_stats(id, mode)
print(user.pp()) #8336
```
В общем, я надеюсь вы поняли.
3) класс - user_recent_score
в ней уже 6 переменных, сейчас поясню.
    id - тут все понятно
    mode - разобран в прошлом
    p - страница
    l - длинна страницы(максимум 1000)
    f - показывать ли проигранные скоры(0 и 1)
    ppFilter - показывать скоры от какого-то колл-ва pp
    
```python
from GatariAPI import user_recent_scores
uid = 1000
mode = 0 
p = 1
l = 5
f = 0
ppfilter = 0
user = user_recent_scores(uid, mode, p, l, f, ppfilter)
print(user.beatmap()) # выведет инфу о 5-ти последних картах, т.к l = 5
```    
4) класс - user_best_scores
То же самое что и прошлый класс, только без переменной f

5) класс - users_first_place
теже функции что и у прошлого класса, только нет переменной ppfilter

#Планы
Ведется разработка оставшихся классов, закончу когда будет время! Удачи в разработке!


