import random

class Head:
    eyes = 2 # статические свойства
    ears = 2 # статические свойства
    mouth = 1 # статические свойства
    def eat(self): # метод
        taste = "вкусно" if random.randint(0,1) else "не вкусно"
        print(taste)

nick = Head()
nick.eat()
# print(dir(Head))

class Body:
    heart = 1

    def sweat(self):
        sweat_ml = random.randint(10, 100)
        print(f'выделилось {sweat_ml} мл пота')

    def __init__(self, height=180, weight=80, sex = "f"):
        self.height=height
        self.weight=weight
        self.sex =sex
        self.childern = 0

    def make_childern(self, childern_numer):
        if self.sex =="f":
            self.gain_weight()
            self.childern+=1
        else:
            print("вы не женщина")

    def gain_weight(self):
        self.weight+=random.randint(1, 10)
        print("вес -", self.weight)





dudy = Body(height=160, weight=60)
print(dudy.height)
print(dudy.weight)
dudy.gain_weight()
dudy.make_childern(4)
print(dudy.childern)

class Human(Head, Body):
    pass
nick = Human()
nick.sweat()
nick.eat()
print(nick.eyes)
print(nick.heart)

class hand:
    fingers = 5
    def grab(self):
        print("Золотые руки на серебро не купишь" if random.randint(0,1) else "руки — крюки: не тем концом воткнуты")

nick = hand()
nick.grab()

class eyes:
    eye_s = 2
    def see(self):
        print("Глаза — зеркало души" if random.randint(0,1) else
              "в глазу чужом - соринку видим, в своём - бревна не разглядим")

nick = eyes()
nick.see()

class ears:
    ear_s = 2
    def listen(self):
        print("В одно ухо влетело, в другое вылетело" if random.randint(0,1) else
              "Слушающий что-то да узнает, а говорящий — ничего")

nick = ears()
nick.listen()

# динамические свойства

class Head:
    eyes = 2  # статические свойства
    ears = 2  # статические свойства
    mouth = 1  # статические свойства
    def __init__(self, eye_color, teeth_number): # динамические свойства
        self.eye_color = eye_color
        self.teeth_number = teeth_number
    def eat(self):  # метод
        taste = 'вкусно' if random.randint(0,1) else 'не вкусно'
        print(taste)
professor = Head('green', 25)
print(professor.eye_color)
print(professor.teeth_number)

class Head:
    eyes = 2  # статические свойства
    ears = 2  # статические свойства
    mouth = 1  # статические свойства
    def __init__(self, eye_color='blue', teeth_number=32): # динамические свойства
        self.eye_color = eye_color
        self.teeth_number = teeth_number
    def eat(self):  # метод
        taste = 'вкусно' if random.randint(0,1) else 'не вкусно'
        print(taste)
    def delete_tooth(self):  # метод
        if self.teeth_number >= 1:
            self.teeth_number -= 1
            print(f'Зуб удален. Осталось {self.teeth_number} зубов')
        else:
            print('Зубов нет!')
    def become_van_goh(self):  # метод
        if self.ears == 2:
            self.ears -= 1
            print(f'Ухо удалено. Теперь вы почти Ван Гог!')
        elif self.ears == 1:
            print(f'Вы и так почти Ван Гог! Ухо последнее не трогайте.')

class Body:
    hand = 2
