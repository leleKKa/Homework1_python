# Задача 2: Найдите сумму цифр трехзначного числа.

# a = int(input("Введите трехзначное число: "))
# if a < 1000  and a > 99:
#     sum = 0
#     while a > 0:
#         x = a % 10
#         sum = sum + x
#         a = a // 10
#     print(sum)
# else:
#     print("Это не 3х значное число. Введите трехзначное число")

# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. 
# Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок, 
# если известно, что Петя и Сережа сделали одинаковое количество журавликов, 
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
# a + a + 2 (a+a) = 6*a  a = s/6

# s = int(input("Введите общее число журавликов: "))
# if s % 6 == 0:
#     a = s / 6
#     print(f'Петя и Сережа сделали по {a} журавликов. Катя сделала {2*(a+a)} журавликов')
# else:
#     print("Введите другое число")

# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались 
# за проезд и получали билет с номером. Счастливым билетом называют такой билет 
# с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. 
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. 
# Вам требуется написать программу, которая проверяет счастливость билета.

# num = int(input("Введите шестизначный номер билета: "))
# if num < 1000000 and num > 100000:
#     num1 = 0
#     num2 = 0
#     i = 0
#     while i < 3:
#         num1 = num1 + num % 10
#         num = num // 10
#         i +=1
#     j = 0
#     while j < 3:
#         num2 = num2 + num % 10
#         num = num // 10
#         j +=1
#     if num1 == num2:
#         print("Счастливый билет")
#     else:
#         print("Билет обычный")
# else:
#     print("Этот номер не шестизначный. Попробуйте еще раз")
        

# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек 
# отломить k долек, если разрешается сделать один разлом по прямой между дольками 
# (то есть разломить шоколадку на два прямоугольника).

# n = int(input("Введите число долек шоколадки с одной стороны: "))
# m = int(input("Введите число долек шоколадки с другой стороны: "))
# k = int(input("Введите число долек шоколадки, которое хотим съесть: "))

# if k< m *n and k % n == 0 or k % m ==0:
#       print("Ура, вы сделали только один разлом")
# else:
#     print("Вы точно хотите съесть именно столько шоколада?")



    