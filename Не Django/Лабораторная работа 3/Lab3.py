import  os

def t1():
    while True:
        try:
            dic = input("Укажите директорию (0 - выход): ")
            if dic == "0":
                break
            print("Кол-во файлов: ", len(os.listdir(dic)))
            break
        except FileNotFoundError:
            print("Директории не существует.")
    print("\n\n")

def t2():
    print("№   Наименование   Цена   Количество")
    for i in range(len(pr)):
        print("{}   {}   {}   {}".format(pr[i][0],pr[i][1],pr[i][2],pr[i][3]))
    print("\n")

def t3():
    add = 0
    iid = -1
    idl = []
    while iid != 0:
        try:
            iid = int(input("Введите номер товара (0 - прекратить): "))
            idl.append(iid)
        except ValueError:
            print("Не может быть номером товара.")
    while True:
        try:
            add = int(input("Введите доп. кол-во: "))
            break
        except ValueError:
            print("Введите число.")
    for i in range(len(pr)):
        if pr[i][0] in idl:
            pr[i][3] += add
    print("Готово!\n\n")

def t4():
    a = True
    b = 0
    nfc = int(input("Записать в новый файл? (0 - нет, 1 - да): "))
    if nfc == 0:
        while a:
            for i in range(len(pr) - 1):
                if pr[i][0] > pr[i + 1][0]:
                    temp = pr[i]
                    pr[i] = pr[i + 1]
                    pr[i + 1] = temp
                else:
                    b += 1
            if b == 3:
                a = False
            b = 0
        f = open("products.txt","w",encoding = "ansi")
        with open("products.txt","a") as outfile:
            for i in range(len(pr)):
                for j in range(len(pr)):
                    f.write(str(pr[i][j]))
                    f.write(";")
                f.write("\n")
        f.close()
        a = True
        b = 0
        while a:
            for i in range(len(pr) - 1):
                if pr[i][1] > pr[i + 1][1]:
                    temp = pr[i]
                    pr[i] = pr[i + 1]
                    pr[i + 1] = temp
                else:
                    b += 1
            if b == 3:
                a = False
            b = 0
        print("Готово!\n\n")
    else:
        f = open("products_new.txt","tw",encoding = "ansi")
        with open("products_new.txt","a") as outfile:
            for i in range(len(pr)):
                for j in range(len(pr)):
                    f.write(str(pr[i][j]))
                    f.write(";")
                f.write("\n")
        f.close()
        print("Готово!\n\n")

# init
ans = ""
exc = False
a = True
b = 0
while True:
    try:
        fn = input("Введите имя файла (с расширением): ")
        if ".txt" not in fn: raise ValueError
        f = open(fn,"r")
        pr = []
        for line in f:
            line = line.split(";")
            pr.append([int(line[0]),line[1],int(line[2]),int(line[3])])
        while a:
            for i in range(len(pr) - 1):
                if pr[i][1] > pr[i + 1][1]:
                    temp = pr[i]
                    pr[i] = pr[i + 1]
                    pr[i + 1] = temp
                else:
                    b += 1
            if b == 3:
                a = False
            b = 0
        break
    except (FileNotFoundError, ValueError):
        print("Файл не найден в папке с программой или заполнен неправильно,\nфункции 2-4 будут недоступны при продолжении\n\n")
        while True:
            ans = input("Продолжить? (Y/N): ")
            ans = ans.upper()
            if (ans == "Y") or (ans == "N"): break
        if ans == "Y":
            exc = True
            break
opt = {1: t1,
       2: t2,
       3: t3,
       4: t4}

# program
ch = -1
while ch != 0:
    while True:
        try:
            ch = int(input("""0 - Выход
1 - Подсчет файлов в заданной директории
2 - Вывод информации о товарах, импортированной из products.txt
3 - Увеличить кол-во товаров указанных номеров
4 - Перезаписать products.txt или вывести список в новый файл
Выберите функцию: """))
            if (ch < 0) or (ch > 4):
                raise ValueError
            break
        except ValueError:
            print("Неверный формат ввода.")
    if ch != 0:
        if exc and (ch > 1):
            print("Функция недоступна")
            ch = 1
        opt[ch]()
print("Завершение программы...")
