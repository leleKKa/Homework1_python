"""
n = 'dfdf\'jhhhj'
# print(n)

a = 5
b = 5.89
c = 'hello'

print (a,'-', b,c)
print(f"{a} - {b} - {c}")
print("{} - {} - {}".format(a,b,c))
"""

#print("Введите первое число: ")
#a = input()
#print(a)
# b = input("Введите второе число: ")
#print(a, ' + ', b, ' = ', a+b)

# c = 5.89
# print(c)
#print(type(c))
# c = bool(c)
# print(type(c))

# a = 5.8994
# b = 6.584
# print(round(a*b, 3))

# iter = 2
# iter += 3 # iter = iter + 3
# iter -= 4 # iter = iter - 4
# iter *= 5 # iter = iter * 5
# iter /= 5 # iter = iter / 5
# iter //= 5 # iter = iter // 5
# iter %= 5 # iter = iter % 5
# iter **= 5 # iter = iter ** 5

text = 'СъЕШЬ ещё этих МяГкИх французских булок'
print(len(text)) # 39
print('ещё' in text) # True
print(text.lower()) # съешь ещё этих мягких французских булок  lower делает все буквы маленькими
print(text.upper()) # СЪЕШЬ ЕЩЁ ЭТИХ МЯГКИХ ФРАНЦУЗСКИХ БУЛОК upper делает все буквы большими
print(text.replace('ещё','ЕЩЁ'))# СъЕШЬ ЕЩЁ этих МяГкИх французских булок  replace замена

 