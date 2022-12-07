# человек против человека.
"""from pprint import pprint
from random import randint

player1 = input("Введите имя первого игрока: ")
player2 = input("Введите имя второго игрока: ")
value = int(input("Введите количество конфет на столе: "))
flag = randint(0,2)

if flag:
    print(f"Ход игрока {player1}")
else:
    print(f"Ход игрока {player2}")

def input_dat(name):
    x = int(input(f"{name}, Возьмите конфеты, в количестве от 1 до 28: "))
    while x < 1 or x > 28:
        x = int(input(f"{name}, Возьмите конфеты, в количестве от 1 до 28: "))
    return x

counter1 = 0 
counter2 = 0

def p_print(name, k, counter, value):
    print(f"Игрок {name}, взял {k} конфет, теперь у него {counter}.")

while value > 28:
    if flag:
        k = input_dat(player1)
        counter1 += k
        value -= k
        flag = False
        p_print(player1, k, counter1, value)
   

if flag:
    print(f"Победа игрока {player1}")
else:
    print(f"Победа игрока {player2}")"""



# a) Добавьте игру против бота
#from pprint import pprint
#from random import randint

#player1 = input("Введите своё имя: ")
#player2 = "Bot"
#value = int(input("Введите количество конфет на столе: "))
#flag = randint(0,2)

#if flag:
#    print(f"Ход игрока {player1}")
#else:
#    print(f"Ход игрока {player2}")

#def input_dat(name):
#    x = int(input(f"{name}, Возьмите конфеты, в количестве от 1 до 28: "))
#    while x < 1 or x > 28:
#        x = int(input(f"{name}, Возьмите конфеты, в количестве от 1 до 28: "))
#    return x

#counter1 = 0 
#counter2 = 0

#def p_print(name, k, counter, value):
#    print(f"Игрок {name}, взял {k} конфет, теперь у него {counter}.")

#while value > 28:
#    if flag:
#        k = input_dat(player1)
#        counter1 += k
#        value -= k
#        flag = False
#        p_print(player1, k, counter1, value)
#    else:
#        k = randint(1,29)
#        counter2 += k
#        value -= k
#        flag = True
#        p_print(player2, k, counter2, value)

#if flag:
#    print(f"ПОБЕДА!!!")
#else:
#    print(f"Поражение:(")


#b) Подумайте как наделить бота ""интеллектом""

from pprint import pprint
from random import randint

player1 = input("Введите своё имя: ")
player2 = "Bot"
value = int(input("Введите количество конфет на столе: "))
flag = randint(0,2)

if flag:
    print(f"Ход игрока {player1}")
else:
    print(f"Ход игрока {player2}")

def input_dat(name):
    x = int(input(f"{name}, Возьмите конфеты, в количестве от 1 до 28: "))
    while x < 1 or x > 28:
        x = int(input(f"{name}, Возьмите конфеты, в количестве от 1 до 28: "))
    return x

def bot_calc(value):
    k = randint(1,29)
    while value-k <= 28 and value > 29:
        k = randint(1,29)
    return k

counter1 = 0 
counter2 = 0

def p_print(name, k, counter, value):
    print(f"Игрок {name}, взял {k} конфет, теперь у него {counter}.")

while value > 28:
    if flag:
        k = input_dat(player1)
        counter1 += k
        value -= k
        flag = False
        p_print(player1, k, counter1, value)
    else:
        k = bot_calc(value)
        counter2 += k
        value -= k
        flag = True
        p_print(player2, k, counter2, value)

if flag:
    print(f"ПОБЕДА!!!")
else:
    print(f"Поражение:(")