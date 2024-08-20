# Module 2 Practice 2
First = int(input('Введите первое целое число: '))
Second = int(input('Введите второе целое число: '))
Third = int(input('Введите третье целое число: '))
if (First == Second) and (Second == Third):
    print('Введены 3 одинаковых числа')
elif (First == Second or First == Third or Second == Third):
    print('Введены 2 одинаковых числа')
else: print('Введены 3 разных числа')