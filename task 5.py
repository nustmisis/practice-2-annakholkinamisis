# -*- coding: utf-8 -*-
"""
Задана строка S и символ С. За один ход можно поменять местами два соседних символа. Сколько потребуется ходов чтобы переместить все символы С в строке в начало строки, не меняя при этом порядок следования между остальным символами.

Например, имеется строка abcabcabc, и задан символ b. После перемещения всех символов b в начало строки, получится строка 
bbbacacac, на это уйдёт 9 ходов, ниже указаны строки получившиеся после кажого хода.
1. bacabcabc

2. bacbacabc

3. batcacabe

4. bbacacabc

5. bbacacbac

6. bbacabcac 

7. bbacbacac

8. bbabcacac 

9. bbbacacac
Входные данные

Задана строка 5, состоящая из прописных бука латинского алфавита, и символ С через пробел. Длина строки не превышает 100 символов. Гарантируется, что символ С встречается в строке 5.

Выходные данные

Выведите единственное числе количество ходов, которое потребуется, чтобы переместить все символы с начало строки

Примеры

входные данные

аbrahcabe b

выходные данные
9


@author: workk
"""

count = 1
s = 'аbrahcabe'
b = 'b'
lst = list(s)
for idx, ch in enumerate(lst):
    if ch == b and idx == 0:
        continue
    if ch == b:
        for i in reversed(range(idx+1)):
            if i-1 >= 0 and lst[i-1] != b:
                lst[i-1], lst[i] = lst[i], lst[i-1]
                count += 1
            else:
                break

print(count)

