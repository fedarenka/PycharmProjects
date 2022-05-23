# l = [1,2,3,4,5,6,7,8,9]
# l.append(10)
# print(l)
# l1 = [11,12,13,14,15,16,17,18,19]
# l.extend(l1)
# print(l)
# l.remove(10)
# print(l)
# l.pop(5)
# print(l)
# print(l.index(9,0,10))
# print("1,2,3,4,5,6,7,8,9".count("4",0,10))
# lx = l[0]
# l[0]=l[8]
# l[8]=lx
# print(l)
# l[0],l[8] = l[8],l[1]
# print(l)

# def function (n,k):
#     if n > 20:
#         print("end")
#     elif n <= 20:
#         tot = 0
#         for i in range (1,n+1):
#             if i % 2 == 0:
#                 tot = tot + i**2
#         print(tot)
# function(7,2)

# l = [10,1,3,5,1,0,-1,-2,-3,-4]
# total = 0
# i = 0
# while l[i]>=0:
#     total += l[i]
#     i+=1
# print(total)
# total1=0
# for i1 in l:
#     if i1 < 0:
#         break
#     total1+=i1
# print(total1)
#
# total2 = 0
# i2 = 0
# while total2 < 15 and l[i2] >= 0:
#     total2 += l[i2]
#     i2 += 1
# print(total2)
# total3=0
# for i3 in l:
#     if total3<15 and l[i2] >= 0:
#         total3 += i3
# print(total3)
q = [10,1,3,5,1,0,-1,-2,-3,-4,-5]
total4 = 0
i=-1 # i = len(q)-1
while q[i] < 0:
    total4 += q[i]
    i-=1
print(total4)

total5=0
for i5 in range(len(q) -1,0,-1):
    if q[i5]<0:
        total5+=q[i5]
    if q[i5]>0:
        break
print(total5)

a = ['hello', 'my', 'Dolly']
# i=0
# while a[i] != 'Dolly':
#     print(a[i])
#     i+=1
# i1=0
# for i1 in range(len(a)):
#     if a[i1] == 'Dolly':
#         break
#     print(a[i1])

# d = {1:1, 2:4, 3:9}
# print(d)
# d.pop(2)
# print(d)
# d.values()
# print(d)
# del d[3]
# print(d)

# Напишите программу, которая принимает аргумент в виде списка и возвращает словарь,
# в котором каждый элемент списка является и ключом и значением. Предполагается,
# что элементы списка будут соответствовать правилам задания ключей в словарях.
# Пример: из списка [8, 9, 4, 7, ‘a’] получаем словарь: {8:8, 9:9, 4:4, 7:7, ‘a’:‘a’ }

l = [8, 9, 4, 7, 'a']
d = {e:e for e in l}
print(d)
d1 = dict(zip(l[::1],l[::-1]))
print(d1)
# s = {}
# for i in l:
#     s[i]=s.get(i,i)
# print(s)