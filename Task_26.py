# Задача 26.
# Напишите программу, которая на вход принимает два числа A и B, 
# и возводит число A в целую степень B с помощью рекурсии.
# Пример:
# A=3; В=5 -> 243 (3**5)
# А=2; В=3 -> 8

def exponentiation (first_number, second_number):
    
    if second_number == 0:
        return  1
    return first_number* exponentiation(first_number, second_number-1)


A = int(input("Введите число A: "))
B = int(input("Введите число B: "))
print(int(exponentiation(A,B)))