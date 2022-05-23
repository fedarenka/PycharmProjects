a = ['hello', 'my', 'Dolly']
print(a)
a[0], a[1], a[2] = a[1], a[2], a[0]
print(a)

q,w,e,r = 1,2,3,4
print(q,e,w,q)

b = [10,20,30,40,50,60]
t_s = 0
for c in b:
    t_s = t_s + c
print(t_s)

sum = 0
for h in range(1,5):
    sum += h
print(sum)

print (list(range(1,100)))
j = 0
for i in range(1, 100):
    if i % 3 == 0:
        j = j + i
print(j)

for a in range(4):
    print(a)
for d in range(5,10):
    print(d)
print(list(range(5,10)))

for g in range(15,0,-1):
    print(g)


s = 'я учу программирование'# начальная фраза
b = 'р' # символ, поддежащий замене
d = '' # символ, на который заменяем
for c in s:
    if c != b:
        d += c
print(d)

def m_f(m,k):
    if m > 20:
        return 0
    if m <= 20:
        print(list(range(1, m)))
        total = 0
        for x in range(1,m):
            if x % 2 == 0:
                total += x ** k
                return total
print(m_f(18,3))


