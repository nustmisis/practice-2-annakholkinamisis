# -*- coding: utf-8 -*-
"""
Взгляните на показанный ниже
код, в котором используется цикл while и флаг found
для поиска в списке тепеней 2 занания 2, вовзевдённую в пятую степень

@author: workk
"""

L = [1, 2, 4, 8, 16, 32, 64]
X = 5

num = 2 ** X
if num in L:
    print('at index', L.index(num))
else:
    print(X, 'not found')
