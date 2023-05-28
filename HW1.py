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
