# 3.7.2
# В какой-то момент в Институте биоинформатики биологи перестали понимать, что говорят информатики: они говорили каким-то 
# странным набором звуков.

# В какой-то момент один из биологов раскрыл секрет информатиков: они использовали при общении подстановочный шифр, т.е. заменяли 
# каждый символ исходного сообщения на соответствующий ему другой символ. Биологи раздобыли ключ к шифру и теперь нуждаются в помощи:

# Напишите программу, которая умеет шифровать и расшифровывать шифр подстановки. Программа принимает на вход две строки одинаковой длины, 
# на первой строке записаны символы исходного алфавита, на второй строке — символы конечного алфавита, после чего идёт строка, 
# которую нужно зашифровать переданным ключом, и ещё одна строка, которую нужно расшифровать.

# Пусть, например, на вход программе передано:
# abcd
# *d%#
# abacabadaba
# #*%*d*%

# Это значит, что символ a исходного сообщения заменяется на символ * в шифре, b заменяется на d, c — на % и d — на #.
# Нужно зашифровать строку abacabadaba и расшифровать строку #*%*d*% с помощью этого шифра. Получаем следующие строки, 
# которые и передаём на вывод программы:
# *d*%*d*#*d*
# dacabac

# Sample Input 2:

# dcba
# badc
# dcba
# badc

# Sample Output 2:

# badc
# dcba


#1 строка
x = str(input())
a = []
for i in range(len(x)):
    a.append(x[i])

#2 строка
y = str(input())
b = []
for i in range(len(y)):
    b.append(y[i])

#запись в словарь
d = dict(zip(a,b))

#3 строка, зашифровать
x1 = str(input())
a1 = []
a11 = []
for i in range(len(x1)):
    a1.append(x1[i])

for i in a1:
    for key in d.keys():
        if i == key:
            a11.append(d[key])

#4 строка, расшифровать
y1 = str(input())
b1 = []
b11 = []
for i in range(len(y1)):
    b1.append(y1[i])
    
for i in b1:
    for key, value in d.items():
        if i == value:
            b11.append(key)

print(''.join(a11))
print(''.join(b11))


# 3.7.3

# Простейшая система проверки орфографии основана на использовании списка известных слов. Каждое слово в проверяемом тексте 
# ищется в этом списке и, если такое слово не найдено, оно помечается, как ошибочное.
# Напишем подобную систему.

# Через стандартный ввод подаётся следующая структура: первой строкой — количество d записей в списке известных слов, 
# после передаётся  d строк с одним словарным словом на строку, затем — количество l строк текста, после чего — l строк текста.

# Напишите программу, которая выводит слова из текста, которые не встречаются в словаре. Регистр слов не учитывается. 
# Порядок вывода слов произвольный. Слова, не встречающиеся в словаре, не должны повторяться в выводе программы.

# Sample Input:
# 3
# a
# bb
# cCc
# 2
# a bb aab aba ccc
# c bb aaa

x = int(input()) #ввод количества записей известных слов
#запись списка слов
a = []
for i in range(x):
    a.append(str.lower(input()))
a = set(a)
y = int(input()) #ввод количества записей с одним словарным словом на строку
#запись списка списков
b = []
for j in range(y):
    b.append(list(map(str, input().split(' '))))

#запись списка списков в один список
c = []
for jj in b: 
    for jjj in jj:
        c.append(jjj)

#запись списка в .lower()
d = []
for ii in c:
    d.append(ii.lower())
dd = dict(zip(c,d)) #запись в словарь с значениями в .lower()

#вычитание одного множества из другого
s = set(d) - set(a)

z = []
for key, value in dd.items():
    for i in s:
        if i == value:
            z.append(key)

print('\n'.join(z))