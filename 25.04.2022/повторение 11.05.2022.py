# n = int(input("введите число: "))
# for i in range(0,n+1):
#     print(i**2, end=", ")
# print()

# Пользователь вводит число. Посчитать сумму цифр этого числа. Число может быть любой длины.
i= int(input("введите число: "))
s = 0
while i!=0:
    s+= i%10
    i = i//10
print(s)

n = input('Введите число: ')
l = len(n)
s = 0
for i in range(l):
    s+=int(n[i])
print(s)

# n = input("Введите число - ")
# num = int(n)
# summa = 0
# for i in range(len(n)):
#     summa += (num % 10**(i+1)) // 10**i
# print(summa)