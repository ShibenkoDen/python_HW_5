# Задача 28.
# Напишите рекурсивную функцию sum(a,b), возвращающую сумму двух целых 
# неотрицательных чисел. Из всех арифметических операций допускаются только +1 и -1.
# Также нельзя использовать циклы.
# Пример:
# 2 2
# 4

def summa(first_number,second_number):
    
    if first_number ==0 and second_number == 0:
        return 0
    if first_number == 0:
        return 1+ summa(first_number, second_number - 1)
    if second_number == 0:
        return 1+ summa(first_number-1, second_number)
    return 1+1+summa(first_number-1,second_number-1)

A = int(input("Введите число A: "))
B = int(input("Введите число B: "))
print (summa(A,B))