
#1-------------------------------

file_1 = open("file_1.txt", "w", encoding="utf-8")
file_1.write("Введите в первом задании\n")
file_1.write("построчно\n")
file_1.write("данные\n")
file_1.write("от нерадивого\n")
file_1.write("пользователя\n")
file_1.write("\n")
file_1.close()

#2--------------------------------------------
with open('file_1.txt') as file_1:
    content = file_1.readlines()
    print(len(content))

with open('file_1.txt') as file_1:
    content = file_1.readline()
    word_count = 0
    for word in content.split():
        word_count += 1
    print(word_count)

    content = file_1.readline()
    word_count = 0
    for word in content.split():
        word_count += 1
    print(word_count)

    content = file_1.readline()
    word_count = 0
    for word in content.split():
        word_count += 1
    print(word_count)

    content = file_1.readline()
    word_count = 0
    for word in content.split():
        word_count += 1
    print(word_count)

    content = file_1.readline()
    word_count = 0
    for word in content.split():
        word_count += 1
    print(word_count)

    content = file_1.readline()
    word_count = 0
    for word in content.split():
        word_count += 1
    print(word_count)

    content = file_1.readline()
    word_count = 0
    for word in content.split():
        word_count += 1
    print(word_count)

    content = file_1.readlines()
    print(len(content))

#4------------------------------------------------
from googletrans import Translator
translator = Translator()

text_4 = open('text_4.txt', "r+")
for line in text_4:
    result = translator.translate(line, src='en', dest='ru')
    print(result.text)

with open('file_5.txt', "a") as file_5:
    text_4.seek(0)
    for line in text_4:
        result = translator.translate(line, src='en', dest='ru')
        file_5.writelines(f"{result.text}\n")

text_4.close()

#3-------------------------------------------
with open('text_3.txt', "r+") as text_3:
    content = text_3.read()
    print(content.split())
    a = content.split()
    b = a[1::2]
    print(b)
    b1 = list(map(float, b))
    print(b1)
    x = sum(b1)
    print(x)
    c = a[0::2]
    print(c)
    z = dict(zip(c, b1))
    print(z)
    #далее я доработаю вывод только тех значений, ключ которых более 20000
    #for key in z:
     #   if key < 20000:
      #      print(key)

#5---------------------------------------

with open('text_5.txt', "w") as text_5:
    text_5.write('1 2 3 4 5 6 7')

with open('text_5.txt', "r") as text_5:
    text_5.seek(0)
    content = text_5.read()
    content_1 = list(map(int, content.split()))
    result = sum(content_1)
    print(result)
