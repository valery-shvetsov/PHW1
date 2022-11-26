# 5- Напишите программу, которая принимает на вход координаты двух точек и 
# находит расстояние между ними в 2D пространстве.

# Пример:

# - A (3,6); B (2,1) -> 5.09
# - A (7,-5); B (1,-1) -> 7.21

import math
print()
print ('Введите через запятую координаты первой точки: ')
coord_x1, coord_y1 = map(float, input().split(','))
print ('Введите через запятую координаты второй точки: ')
coord_x2, coord_y2 = map(float, input().split(','))
spacing_1_2=float (math.sqrt((coord_x1-coord_x2)**2+(coord_y1-coord_y2)**2))
spacing_1_2=int((spacing_1_2*100))/100
print ('Расстояние между точками=', spacing_1_2)

