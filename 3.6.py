#3.6.2
# Имеется набор файлов, каждый из которых, кроме последнего, содержит имя следующего файла.
# Первое слово в тексте последнего файла: "We".

# Скачайте предложенный файл. В нём содержится ссылка на первый файл из этого набора.
# Все файлы располагаются в каталоге по адресу: https://stepic.org/media/attachments/course67/3.6.3/
#Загрузите содержимое последнего файла из набора, как ответ на это задание.


import requests

url = "https://stepic.org/media/attachments/course67/3.6.3/"
r = requests.get(url + "699991.txt")
while not r.text.startswith("We"):
    r = requests.get(url + r.text)
print(r.text)
