import random

class Head:
    eyes = 2
    ears = 2
    mouth = 1
    def eat(self):
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