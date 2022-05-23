# Задача №1. Создайте кортеж с цифрами от 0 до 9 и посчитайте сумму
a = (range(10))
print(sum(a))
print(0+1+2+3+4+5+6+7+8+9) # проверка

# Задача №2 Выведите статистику частности букв в кортеже
long_word = ( 'т', 'т', 'а', 'и', 'и', 'а', 'и', 'и', 'и', 'т', 'т', 'а', 'и', 'и',  'и', 'и', 'и', 'т', 'и')
print("количество 'т' -", long_word.count('т'), ";", "количество 'а' -",
      long_word.count('а'),";", "количество 'и' -", long_word.count('и',))
print(len(long_word)) # проверка

# Задача №3. найти самое длинное слово
string = "Paythan java c c++ javascript paskal php"
print(string)
words = string.split()
print(words)
id_long = 0
c = 0
for i in words:
      if len(words)<len(words[c]):
            id_long = c
      c +=1
print(id_long)
