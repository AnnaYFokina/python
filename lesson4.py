#1--------------------------------------------
from sys import argv
print(argv)

name, s_1, s_2, s_3 = argv

def money(s_1, s_2, s_3):
    money_total = int(s_1) * int(s_2) + int(s_3)
    return money_total
print(money(s_1, s_2, s_3))

#2-------------------------------------------

list_2 = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

list_2_new = [el for i, el in enumerate(list_2) if list_2[i - 1] < list_2[i] and i > 0]
print(f"Новый список: {list_2_new}")


#3-----------------------------

my_new_list = [el for el in range(20, 241) if el % 21 == 0 or el % 20 == 0]
print(f"Новый список: {my_new_list}")

#4--------------------------------------

my_list_4 = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
my_new_list_4 = [el for el in my_list_4 if my_list_4.count(el) < 2]
print(f"Элементы списка, не имеющие повторений: {my_new_list_4}")

#5______________________________________

from functools import reduce

list_4 = [el for el in range(100, 1001) if el % 2 == 0]

def function_4(prev_w, w):
    return prev_w * w

print(reduce(function_4, list_4))


#6_-------------------------------------

from itertools import count

for x in count(3):
    if x > 10:
        break
    else:
        print(x)

from itertools import cycle

y = 0
for u in cycle([1, 2, 3, "abc", True]):
    if y > 4:
        break
    print(u)
    y += 1
#7---------------------------------------



def fact(n):
    f = 1
    for el in range(1, n, 1):
        f = el * f
        yield f

n = int(input("Введите число, для которого считаем факториал: "))

print(fact(n))

for i in fact(n):
    print(i)
