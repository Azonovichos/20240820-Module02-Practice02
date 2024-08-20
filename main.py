# Module 2 Practice 2
First = input('Введите первое целое число: ')
Second = input('Введите второе целое число: ')
Third = input('Введите третье целое число: ')
if (First == Second) and (Second == Third):
    print('Введены 3 одинаковых числа')
elif (First == Second or First == Third or Second == Third):
    print('Введены 2 одинаковых числа')
else: print('Введены 3 разных числа')