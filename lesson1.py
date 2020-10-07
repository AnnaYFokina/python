who = input("Как тебя зовут?")
print("Привет, ", who)
age = int(input("Сколько тебе лет?"))
place = input("Ты - сама юность! Откуда ты?")
print("Неужели?! Я тоже!")

z = int(input('Введите число: '))
v = str(z)
v1 = v + v
v2 = v + v + v
v3 = z + int(v1) + int(v2)
print(v3)

revenue = int(input("Какова выручка? "))
cost = int(input("Каковы издержки? "))
if revenue != cost:
    if revenue > cost:
        print("Поздравляю, вы - прибыльны!")
        profit = int(revenue - cost)
        print("Прибыль составила ", profit)
        rent = int(revenue / profit)
        print("Рентабельность составила ", rent)
        emploee_number = int(input("Сколько сотрудников? "))
        each_empl = float(profit / emploee_number)
        print("Прибыль в расчете на каждого сотрудника ", each_empl)
    elif revenue < cost:
        print("Увы, вы - убыточны!")
elif revenue == cost:
    print("Самоокупаемость - тоже хорошо.")

time = int(input("Введите время в секундах: "))
hours = int(time // 3600)
minutes_1 = int(time % 3600)
minutes_2 = int(minutes_1 // 60)
seconds = int(minutes_1 % 60)
print(f"Время {hours:02}:{minutes_2:02}:{seconds:02}.")

a = int(input("Введите результат в первый день: "))
b = int(input("Введите желаемый результат: "))
day = 1
while a < b:
    a = a + a * 0.1
    day += 1
print(day)

t = int(input("Введите число: "))
t_max = t % 10
t = t // 10
while t > 0:
    if t % 10 > t_max:
        t_max = t % 10
    t = t // 10
print(t_max)
