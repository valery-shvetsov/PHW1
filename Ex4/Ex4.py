# Задание 4
# Напишите программу, которая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в этой четверти (x и y).

# Пример:
# - quarter = 1 = x∈(0, ∞) u y∈(0,∞)

print()
print ('Введите номер четверти в интервале от 1 до 4')
quatr_number=input ('Номер четверти:')
try:
    quatr_number=int(quatr_number)
    print('')
    if (quatr_number<1 or quatr_number>4):
        print ('Будьте внимательнее.\n Номер четверти должен быть в интервале от 1 до 4')
    if (quatr_number==1):
        print ('Диапазон возможных координат точек в четверти №1: x∈(0, +∞) u y∈(0,+∞)')
    if (quatr_number==2):
        print ('Диапазон возможных координат точек в четверти №2: x∈(0, -∞) u y∈(0,+∞)')
    if (quatr_number==3):
        print ('Диапазон возможных координат точек в четверти №3: x∈(0, -∞) u y∈(0,-∞)')
    if (quatr_number==4):
        print ('Диапазон возможных координат точек в четверти №4: x∈(0, +∞) u y∈(0,-∞)')        
except ValueError:
    print('Вы ввели не число. Давайте попробуем еще раз')

