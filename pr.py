"""
n = int(input('Введите кол-во киллометров, за сутки '))
m = int(input('Введите общее расстояние '))
print((m+n-1)//n)

# // - целочисленное деление 5:2 = 2 (остаток 1)
# / - деление с дробной частью 5:2=2.5
# 

i = int(input('Вагон, в который вошел Витя: '))
j = int(input('Вагон на табличке: '))
if i == j:
    print('Нехватает дополнительной информации')
else:
    print(i+j-1)
"""
# i = int(input())
# print(i > 5 and i < 10)

# если i = 7, то первое условие 1 и второе условие 1. 1*1=1 (true)
# true(Boolean) - 1
# false(Boolean) - 0
# and(&&) - умножение
# or(||) - сложение

i = int(input("Введите год "))
if i % 4 == 0 and i % 100 != 0 or i % 400 == 0:
    print('yes')
else:
    print('no')


a = int(input("Введите трехзначное число: "))
if a < 1000  and a > 99:
    sum = 0
    i = 0
    while i < 3:
        sum = sum + a % 10
        a = a // 10
        i += 1
    print(sum)
else:
    print("Это не 3х значное число. Введите трехзначное число")

# Задача No9. Решение в группах
# По данному целому неотрицательному n вычислите значение n!. 
# N! = 1 * 2 * 3 * ... * N (произведение всех чисел от 1 до N) 0! = 1 
# Решить задачу используя цикл while
# Input: 5
# Output: 120