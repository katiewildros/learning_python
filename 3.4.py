# 3.4.1
# Напишите программу, которая считывает из файла строку, соответствующую тексту, сжатому с помощью кодирования повторов, 
# и производит обратную операцию, получая исходный текст.
# Запишите полученный текст в файл и прикрепите его, как ответ на это задание.
# В исходном тексте не встречаются цифры, так что код однозначно интерпретируем.

# Примечание. Это первое задание типа Dataset Quiz. В таких заданиях после нажатия "Start Quiz" у вас появляется ссылка 
# "download your dataset". Используйте эту ссылку для того, чтобы загрузить файл со входными данными к себе на компьютер. 
# Запустите вашу программу, используя этот файл в качестве входных данных. Выходной файл, который при этом у вас получится, 
# надо отправить в качестве ответа на эту задачу. 

# Sample Input: a3b4c2e10b1
# Sample Output: aaabbbbcceeeeeeeeeeb


a = 'L8X14I5Y20H9B19O4w9Q1y10U11N11K18j7J5L9I5g2s18G4L11U19M10D16k7'
b = []
for i in range(len(a)):
    if a[i].lower() in 'qwertyuiopasdfghjklzxcvbnm':
        b+=a[i]
        a=a[:i]+"!"+a[i+1:]
c=a.split('!')[1:]
for i in range(len(b)):
    print(b[i]*int(c[i]), end="")
    
# 3.4.2
#Недавно мы считали для каждого слова количество его вхождений в строку. Но на все слова может быть не так интересно смотреть, 
# как, например, на наиболее часто используемые.
# Напишите программу, которая считывает текст из файла (в файле может быть больше одной строки) и выводит самое частое слово в 
# этом тексте и через пробел то, сколько раз оно встретилось. Если таких слов несколько, вывести лексикографически первое (можно использовать оператор < для строк).

# В качестве ответа укажите вывод программы, а не саму программу.
# Слова, написанные в разных регистрах, считаются одинаковыми.


x='TbbTZX aUY TbbTZX TbbTZX abbZXppXY aTUbaUUpX T TbbTZX T Ydc aUaU T aYa UZbc YU XTb pXZX Yb ZXXbdbadZ XpXdTZa YXUpZ T cUc pYXYcXTY ZTdTcTYcZ pYXYcXTY YdTYXpX baXcdbTXp pYXYcXTY Xc YdTYXpX bbabbaa bcYc baXcdbTXp bdUUbpbp Xc bdUUbpbp bY bdUUbpbp cUc YdTYXpX bdUUbpbp bbabbaa d daYX bbX dbZTTXcp cYbYcZYd pYXYcXTY bdUUbpbp dd TUcc T dd bbabbaa bbabbaa dd TYYTaTaXc cUc Z cUc pcXUbT daYX dbZdXZYbX Zd bTUdcd YaZpXa YaZpXa cXbTYUapp cbb abTbXZ dZ TXppXXc dZ Z TXYZZ T Xd TZb cXbTYUapp TZb bTUdcd X dU a aYZcUZ Z UTabTdTY YaYpZTYTY YdTdZYTp Z ppTUZaaUY dY pTpXYY baY ZcTdd baY bcXZbdaY bZY cUTa cdUbaaYd UYTZcpd XTUc aYcdTd bYpT ZcZpZdc TZdcXaUbd ZTTdYZd YdZTdTU ZTTdYZd abXYp abXYp aXacpT XdbaYYdbd bcXZbdaY ddbXbcdXd cdYX TZZpppYbd XU TcpUcXp ppcUXac ddaUTYUZp TZZpppYbd apaX TcpUcXp TZZpppYbd bcZpb TacYpbaXU TZZpppYbd TZZpppYbd Ucb adTppacpZ babdcUZa ac bcZpb p bcZpb bcZpb ad ddaUTYUZp TZZpppYbd p ZcTT pXdccpa paU UdbXZpp apaX TZa TZZpppYbd Y abdcTYZ TcpUcXp pTdUaZaUa TcpUcXp cdYdZY TZZpppYbd pZUTbcbp pb TZZpppYbd adTppacpZ YZcad aXYpdcaUd XpTYXTZap XU bcZpb XdYYc XdYYc ddaXbd dZ ZadY abUYaYY XXXY XdYYc XcTbTX TdZdUpbc TdZdUpbc ccTTXZaXc TdZdUpbc XdYYc ppcpYca ZXpX ZXpX Ub Ub Ub Zb Zb XUXZ ddYdb Ub badbaTZb dZ aYacUX Ub XXU aXdZ TZUcc XYcZY XZpZ bTbTZX c X X XaYcZXTU XaYcZXTU Ub aaZ aZbU YUZZpb XTUYc Ub Ub cXXZYTpZT YTa aXdZ TXZ U b baXYaT baXYaT TabpXUbp TX aU YbTbaUdUb b YZa Zdcc Zdcc Y d TUcpUZa YUcada Y cacbYb cac YYbYT d YYbYT ba c YYbYT TTab ba YYbYT YYbYT cacbYb bZX YZ aZYbZbX baUZb YYbYT YYU da ZZZ ddXZd YZ baUZb XTacT YYbYT ZaZcda UY dcUcddYp YbZ aX TUYUaZT TcXb TUYUaZT dTZTUb baUZb XdYaYTZ X XXba YaYpTa bXTad ZZ dTbcTpb pXadTb X X YaYpTa ZZ UUY ZXUUdbbUT X UUY cTcTbapbT XbT TpcXbbd dTbcTpb dTbcTpb X pXadTb ZddXbUXT cZU YddUp X YXTUac Xpbba p d UdbTUbaa UcYda ZpTZX UbbaTTbYT XbUY UUY dcTYcpadb a aZaa UY a X aZaa UT adUTZbZ XdbUcZcZ d adUTZbZ YUpaZYYp a ZZpcZ YTZcb UcpZbd a XpUpbZTp a YdpYZXTT YTZcb UpcbaTbXd UcpZbd ZZpcZ a adYT YYaYU TYpXTXd adpUUYU TXYUcb adYT cTbpaZYbp UX TZaXdadb pad UbUZpbZ c YT ZZpcZ bT UpcbaTbXd a dbpTcZZ bYpYbXZ dp bpdXddX pYXbcZY bpdXddX bpdXddX XU XU Tb Zdd cYcpcpb XU XU TUYbdYX bpdXddX bpdXddX ddYXdc cYcpcpb cdadbTU pYXbcZY TUYbdYX Tb YZZYpY YZZYpY cZYapYa cZYapYa cZYapYa cZYapYa bpXaZ TXbp ZYa cdTdccbXd bUbYXUpc bpXaZ cZYapYa ccpYZdZ pbXcUUd ccpYZdZ pbpacYaU bpXaZ UYpbZTd XbcapZU TbcZUXUbT bpXaZ YcacUT UYZpUTadb pcpZXdX dY UTUUbZd a XUXbXcbXX UUcYbY UYpbZTd cZYapYa YZYZaYXcp cZYapYa aZTT cb YTY Z UYZpUTadb cZYapYa bbp bpXaZ UYpbZTd bpXaZ Zdp ZTbZpcdZ cbXaZ TXbp ZTbZpcdZ dY pcpbYYXcc TbcZUXUbT cZYapYa pZaUTYTTa bXc TUaU bXc bXc TcUa aXTTTZUY Udcd cTapTpU aXTTTZUY Udcd cTapTpU bXc bUZXcUp XTdYb cTapTpU acYbUap aUUYadZcZ pcd pbX ZaTYbTb cdaXUUUbX YpXb bUUX TYYT ZTYTZ p TYYT ZpdaTTY p YpXb bpZccTTpZ cdaXUUUbX bYacppaYc p TXadbcXTZ UYdUXp TYpUU TYYT dpTpUp d apYZZc dpTpUp cTbTZdd cZcX c dZbddcXTY Y pbX YZdUTcb pbX TaTcaYZ TZT pUZXcUXX ddUcc p p XYZZXYba ZZ YZppc dpTpUp p YUbZaU Uc pddTZ cUXcZZYYd XcbTdac XbaYbXbY XZbacp Z bpcZZUZ XZbacp Z bpcZZUZ YUdZU bpcZZUZ bT aaTpdZZT Tda UZa UZa Z abUp Z YcaadapXp XYXbpbYX TaTpXcUaZ XZXapacUX ppbXYZaa pYUX pdZcaT YpdUbc pYUX XaTd ZXa TdTYp UUbU dXd bdUdZX TbTd dZb XY paaapcY Tda bbT daZZb abUp XY aZpb ZXa daaaTapdU XTTZdXUXZ dXd c dYaZXTpZZ Z pYpd bUppT XTTZdXUXZ XcapcZZ baa XTTZdXUXZ bUUXdbY YbTUbZUbb cZcc T ZXa pdZcaT adYdbbdY'
x=x.lower().split(' ')
d={}
for key in x:
    d[key] = d.get(key, 0) + 1
for i in sorted(d.items(), key=lambda x: (x[0])): #(i[0]-->keys, i[1]-->values)    
    if i[1] == max(d.values()):
        print(i[0],i[1])
        break

        
