# Задача 26:  Напишите программу, которая на вход принимает два числа A и B,
# и возводит число А в целую степень B с помощью рекурсии.


A = int(input("Введите число: "))
B = int(input("Введите степень: "))

# def DegreeNum(A, B):
#     C = A ** B
#     return C
# print(DegreeNum(A, B))

def Degree(A, B):
    if B == 0:
        return 1
    else:
        return A * Degree(A, B - 1)

print(Degree(A, B))



# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.


def Sum(a, b):
    if b == 0:
        return a
    elif a == 0:
        return b
    else:
        return Sum(a-1, b+1)

print(Sum(4, 5))
