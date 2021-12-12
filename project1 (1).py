import requests
import sys
import bs4
from lxml import html
import webbrowser
def resultcount(command):
    headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19582"}
    response = requests.get(command,headers=headers,stream=True)
    response.raw.decode_content = True
    tree = html.parse(response.raw)
    result = tree.xpath('//*[@id="result-stats"]/text()')[0]
    print(result)

def request():
    command=''
    print("Для группировки операторов используйте OR,AND и скобки.\n\nИщете файл или страницу?\n")
    print("1 - файл\n")
    print("2 - страница\n")
    a=int(input())
    if(a==1):
        print("Знаете расширение файла?")
        print("1 - да\n")
        print("2 - нет\n")
        b = int(input())
        if (b == 1):
            print("введите расширение")
            type = input(("тип:"))
            command = command + "filetype:" + type + " "
            print("Введите название файла")
            name = input("Название файла")
            command = command + ('"') + name + ('"')
        if (b == 2):
            print("введите название файла")
            name = input()
            command = command + "файл " + name
    else:
        print("Выберите пункт для уточнения запроса\n")
        print("1 - знаете или представляете возможное название сайта\n")
        print("2 - поиск сайтов с заданным доменом\n")
        print("3 - нужна последняя версия страницы\n")
        print("4 - переход к следующему пункту\n")
        c=0
        while(c!=4):
            c=int(input())
            if(c==1):
                site = input(("Сайт: "))
                command = command + "site:" + site + " "
            if(c==2):
                relate = input(("Домен: "))
                command = command + "related:" + relate + " "
            if (c == 3):
                cache = input()
                command = command + "cache:" + cache + " "
        print("Локальные уточнения\n")
        print("1 - map;  2 - loc;  3 - source;  4 - stocks;  5 - к следующему пункту\n")
        d=0
        while (d != 5):
            d = int(input())
            if (d == 1):
                map=input(("map:"))
                command = command + "map:" + map + " "
            if (d == 2):
                loc = input(("loc:"))
                command = command + "loc:" + loc + " "
            if (d == 3):
                source = input(("source:"))
                command = command + "source:" + source + " "
            if (d == 4):
                stocks= input(("stocks:"))
                command = command + "stocks:" + stocks + " "
        print("1 - слово(а) в заголовке;  2 - слово в url;  3 - поиск по словам; \n")
        print("4 - содержит слова в ссылках на себя; 5 - слова стоящие рядом на расстоянии s;  6 - конец\n")
        e=0
        while (e!= 6):
            e = int(input())
            if (e == 1):
                print("Сколько слов?")
                k=int(input())
                if(k==1):
                    intitle = input(("Слова в заголовке: "))
                    command = command + "intitle:" + intitle + " "
                else:
                    for i in range (1,k,1):
                        intitle = input(("Слова в заголовке: "))
                        if(i==1):
                            command = command + "allintitle:" + intitle+ " "
                        else:
                            command = command + intitle + " "
            if (e == 2):
                print("Сколько слов? ")
                k = int(input())
                if (k == 1):
                    inurl = input(("Слова в заголовке: "))
                    command = command + "inurl:" + inurl + " "
                else:
                    for i in range(1, k,1):
                        inurl = input(("Слова в заголовке: "))
                        if (i == 1):
                            command = command + "allintitle:" + inurl + " "
                        else:
                            command = command + inurl + " "
            if (e == 3):
                print("Сколько слов? ")
                k = int(input())
                if (k == 1):
                    intext = input(("Слова в заголовке: "))
                    command = command + "intext:" + intext + " "
                else:
                    for i in range(1, k,1):
                        intext = input(("Слова в заголовке: "))
                        if (i == 1):
                            command = command + "allintext:" + intext + " "
                        else:
                            command = command + intext + " "
            if (e == 4):
                print("Сколько слов? ")
                k = int(input())
                if (k == 1):
                    inanchor = input(("Слова в заголовке: "))
                    command = command + "inanchor:" + inanchor + " "
                else:
                    for i in range(1, k,1):
                        inanchor = input(("Слова в заголовке: "))
                        if (i == 1):
                            command = command + "allinanchor: " + inanchor + " "
                        else:
                            command = command + inanchor + " "
            if(e==5):
                print("Введите слова и на каком они расстоянии ")
                word1=input(("1 слово: "))
                print("\n")
                word2 = input(("2 слово: "))
                print("\n")
                s=int(input("Расстояние: "))
                command = command + word1 +" "+ "AROUND(" +s+") "+word2+" "
    return command
print("1 - составить запрос;  2 - завершение программы")
i=1
while(i!=2):
    c=int(input())
    command=request()
    resultcount("https://google.com/search?q=" + command)
    print("Устраивает количество полученных страниц в запросе? 1 - Да;  2 - Нет")
    k=int(input())
    if(k==1):
        webbrowser.get().open_new_tab("https://google.com/search?q=" + command)
    else:
        command = request()
    i=c
