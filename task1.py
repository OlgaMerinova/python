# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:
# 6 -> да
# 7 -> да
# 1 -> нет
#*Напишите программу, которая принимает на вход 2 числа: номер месяца и номер дня в месяце, проверяет является ли день выходным.
# Принимаем начало года на понедельник и считая год не високосным. Учитываем только гос праздники (НГ, 9 мая и т.д.)




import calendar
import holidays 
R_holidays = holidays.Russia() 

Month = int(input('Введите номер месяца (до 12): '))
Date = int(input('Введите номер дня в месяце: '))

date1=datetime.date(2021, Month, Date)

#date1=calendar.weekday(2021, Month, Date)

j = date1 in R_holidays 

if j == True: 
    print("Yes: ") 
    print(R_holidays.get(date1)) 
 
else: 
    print("No Holiday") 


#if Date == 1 or Date == 2 or Date == 3 or Date == 4 or Date == 5:



