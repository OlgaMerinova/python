#Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

a = int(input('Введите номер четверти:  '))

if   a == 1: 
    print(' Координаты 1 четверти: x от 0 до + ∞, y от 0 до + ∞') 
elif a == 2: 
    print(' Координаты 2 четверти: x от 0 до  - ∞, y от 0  до + ∞ ')  
elif a == 3: 
    print(' Координаты 3 четверти: x от 0 до  - ∞, y от 0  до - ∞ ')
elif a == 4: 
    print(' Координаты 4 четверти: x от 0 до  + ∞, y от 0  до - ∞ ')
else:        
    print('Ошибка, введите четверть от 1 до 4') 