# Задание 2
# - Напишите программу для. проверки истинности утверждения
#  ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
# Нужно написать таблицу истинности.
print()
print('Таблица истинности утверждения \n ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z')
print()
print (f'X \t Y \t Z \t Результат')
print()
for x in range(2):
    for y in range (2):
        for z in range (2):
            left_side=not(x or y or z)
            right_side=not x and not y and not z
            if left_side==right_side:
                print (f'{x} \t {y} \t {z} \t {left_side==right_side} ')