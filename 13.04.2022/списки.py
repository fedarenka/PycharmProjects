# списки
a = [2,4,6,8,10]
b = []
for c in a:
    b.append(c * 2)
print(b)

d = [c * 3 for c in a]
print(d)
#
range_3 = [i * 5 for i in range(1,6)]
print(range_3)

b = []
for c in range(1,6):
    b.append(c * 5)
print(b)

#
a = [1,2,3,6,9,10,12,15,19]
a_1 = []
for i in a:
    if i <= 10:
       a_1.append(i)
print(a_1)

m = [i for i in a if i <= 10]
print(m)

n = [i ** 2 for i in a if i <= 10]
print(n)

words = ["один", "два", "три", "четыре", "пять"]
word_filer = [word for word in words if len(word) > 5]
print(word_filer)

a = [i*2 for i in range(10,1,-1) if i % 2 == 0]
print(a)

b = [word+"." for word in words if len(word) > 5]
print(b)

