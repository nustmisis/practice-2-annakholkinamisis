# -*- coding: utf-8 -*-
"""
Взгляните на показанный ниже
код, в котором используется цикл while и флаг found
для поиска в списке тепеней 2 занания 2, вовзевдённую в пятую степень

@author: workk
"""

L = [1, 2, 4, 8, 16, 32, 64]
X = 5
i = 0
found = False
while not found and i < len(L) :
    if 2 ** X == L[i] :
        found = True
    else:
        i = i + 1

if found:
    print('at index', i)
else:
    print(X, 'not found')
    
"""
a)
# """
while i < len(L):
    if 2 ** X == L[i]:
        print('at index', i)
        break
    elif i == len(L) - 1:
        print(X, 'not found')
        break
    else:
        i += 1

"""
б)
"""
for elem in L:
    if 2 ** X == elem:
        print('at index', L.index(elem))
        break
    elif L.index(elem) == len(L) - 1:
        print(X, 'not found')
        break
    else:
        continue

"""
в)
"""
if 2 ** X in L:
    print('at index', L.index(2 ** X))
else:
    print(X, 'not found')

"""
г) - формулировка задачи не ясна. д) - да, т.к. уменьшится число вызовов функции умножения. е) опять же непонятно, что именно нужно генерировать
"""



'''
Код явно написан с использование альетрнативной логики.
Попоробуйте оптимизировать код c использование рекомендаций, ониявляются не обезатальными, но помогут понять основные ошибки.
а)Сначала перепишите код с конструкцией else цикла while, чтобы избавиться от флага found и финального оператора if.
б) Затем перепишите код для использования цикла for с конструкцией else,
чтобы избавиться от явной логики индексации списка. (Подсказка: для получения индекса элемента применяйте списковый метод index — L. index (X)
возвращает смещение первого элемента X в списке L.)
в) Далее полностью устраните цикл, переписав код с использованием простого
выражения с операцией членства in. (За дополнительными сведениями обращайтесь в главу 8 или наберите для тестирования 2 in [1,2,3].)
г) Наконец примените цикл for и списковый метод append для генерации списка степеней 2 (L) вместо жесткого кодирования спискового литерала.
Ниже приведены более глубокие рассуждения.
д) Как вы думаете, улучшит ли производительность перенос выражения 2 ** X
за пределы циклов? Каким образом вы представили бы это в коде?
е)  Python содержит инструмент тар (функция, список), который также способен генерировать список степеней 2:. Каким образом можно его задать ? 
    
'''