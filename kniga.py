# программа переименовывает названия книг
# названия начинающиеся с цифр или английких букв 
# на русские названия

import os

puth = 'Y:\\p2p\\книги скачаные\\маме книги'
os.chdir(puth) # изменить рабочую папку на другую

old_name = ''
name = ''

def nam(i):
    old_name = i #+ '.fb2'#'kniga.txt'
    with open(old_name, 'r', encoding= 'utf-8') as text:
        text1 = text.readlines(1000)
#        print(text1)
    text2 = str(text1)
    f = text2.split('last-name>')[1].split('<')[0] # фамилия
    i = text2.split('first-name>')[1].split('<')[0] # имя
    naz = text2.split('book-title>')[1].split('<')[0] # название книги
    #print(text2.split('book-title>')[1].split('<')[0])
    name = f + ' ' + i + ' ' + naz + '.fb2' # полное наименование 
    os.rename(old_name, name) # переименовать книгу
    return

directory = puth
files = os.listdir(directory)
print(files)  # покажет список файлов
Spisok = '1234567890qwertyuiopasdfghjklzxcvbnm,.+-/QWERTYUIOPASDFGHJKLZXCVBNM'
for i in files:
    i[0]
    if i[0] in Spisok:
        print(i)
        nam(i)
