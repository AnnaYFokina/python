my_list = [1, 1.56, 'str', [18, 11, 12], {1, 5, 9}, (1, 34, 56)]
for i in my_list:
    print(type(i))

#Решение этой задачи я честно загуглила.
# Почему-то мне казалось, что мне нужно получить от пользователя
#строку, преобразовать ее в спиок, отбросив пробелы, а уже после этого работать со списком и реаливовать
#замену элементов прямо в списке.. здесь же реализация через последовательный запрос
#new_list = input("Введите произвольный список элементов через пробел")
#new_list2 = print(list(new_list))
#и что-то делать дальше... возможно ее решить без последовательного запроса значений у пользователя?

el_count = int(input("Введите количество элементов списка "))
my_list = []
i = 0
el = 0
while i < el_count:
    my_list.append(input("Введите следующее значение списка "))
    i += 1
for elem in range(int(len(my_list)/2)):
        my_list[el], my_list[el + 1] = my_list [el + 1], my_list[el]
        el += 2
print(my_list)

season_list = ['Зима', 'Весна', 'Лето', 'Осень']
month = int(input("Введите номер месяца: "))
if month ==1 or month == 12 or month == 2:
    print(season_list[0])
elif month ==3 or month == 4 or month == 5:
    print(season_list[1])
elif month == 6 or month == 7 or month == 8:
    print(season_list[2])
elif month == 9 or month == 10 or month == 11:
    print(season_list[3])
else:
    print("Нужно ввести значение от 1 до 12")

season_dict = {1 : 'Зима', 2 : 'Весна', 3 : 'Лето', 4 : 'Осень'}
month = int(input("Введите номер месяца: "))
if month ==1 or month == 12 or month == 2:
    print(season_dict.get(1))
elif month ==3 or month == 4 or month == 5:
    print(season_dict.get(2))
elif month == 6 or month == 7 or month == 8:
    print(season_dict.get(3))
elif month == 9 or month == 10 or month == 11:
    print(season_dict.get(4))
else:
    print("Нужно ввести значение от 1 до 12")

new_str = input("Введите несколько слов, разделенных пробелами: ")
new_str
new_word = []
num = 1
for el in range(new_str.count(' ') + 1):
    new_word = new_str.split()
    if len(str(new_word)) <= 10:
        print(f" {num} {new_word [el]}")
        num += 1
    else:
        print(f" {num} {new_word [el] [0:10]}")
        num += 1
