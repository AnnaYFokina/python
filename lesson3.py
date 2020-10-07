#1--------------------------------------


def f_1(arg_1, arg_2):
    try:
        arg_1 = float(arg_1)
        arg_2 = float(arg_2)
        return arg_1 / arg_2
    except ValueError:
        print("It is not a number")
    except ZeroDivisionError:
        print("You cannot devide by zero")

print(f_1(2, 1))

#2------------------------------------------------

name = input("Введите имя: ")
surname = input("Введите фамилию: ")
date_of_birth = input("Введите дату рождения: ")
city = input("Введите город проживания: ")
email = input("Введите email: ")
phone = input("Введите номер телефона: ")

def f_2(name, surname, date_of_birth, city, email, phone):
    print(f"name={name}, surname={surname}, date_of_birth={date_of_birth}, city={city}, email={email}, phone={phone}")

f_2(name, surname, date_of_birth, city, email, phone)

#3---------------------------------------------------

def f_3(num_first, num_second, num_third):
    return (num_first + num_second + num_third) - min(num_first, num_second, num_third)

print (f_3(24, 56, 77))

#4------------------------------------------------------

def f_4(x,y):
    if x<0 and y>0:
        print("Значения переменных не отвечают условию задачи")
    else:
        return (1 / x ** abs(y))
print (round((f_4(6,3)),4))

#5----------------------------------------------------

def sum_total():
    sum_step = 0
    sum_total = 0
    while True:
        for i in input("Введите любое количество чисел через пробел: ").split():
            if i != 'q':
                sum_step += int(i)
                sum_total += sum_step
            else:
                return f"Общая сумма: {sum_total}"
        print("Текущая сумма: ", sum_step)

print(sum_total())

#6-----------------------------------------------------

def latin(s):
    return s.capitalize()

print(latin(input("Введите слово из строчных латичнских букв: ")))

string = input("Введите несколько слово из строчных латичнских букв, разделенных пробелами: ").split()
for s in string:
    print(latin(s))


