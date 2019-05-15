import random
e = 0
loc = 0
tries = 1
num = 0
unum = 0
ans = 0
dif = -1
dset = [10, 100, 1000]
while e == 0:
    print("Угадай число.")
    print("Легко (1-10) - 0\nСредне (1-100) - 1\nСложно (1-1000) - 2\nПользовательская - 3")
    while dif == -1:
        try:
            dif = int(input("Выберите сложность: "))
            if (dif > 3) or (dif < 0):
                raise ValueError
        except ValueError:
            print("Такой сложности нет.")
    if dif != 3:
        unum = dset[dif]
        num = random.randint(1, unum)
    else:
        while True:
            try:
                unum = int(input("Введите верхнюю границу (От 1 до ...): "))
                if unum < 1:
                    raise ValueError
                num = random.randint(1, unum)
                break
            except ValueError:
                print("Это не может быть верхней границей.")
    print("\nЧисло загадано.\n")
    while ans != num:
        try:
            ans = int(input("Ваша догадка: "))
            if (ans < 1) or (ans > unum):
                raise ValueError
            if ans < num:
                tries += 1
                loc = -1
                raise Exception
            elif ans > num:
                tries += 1
                loc = 1
                raise Exception
            else:
                loc = 0
            break
        except ValueError:
            print("Это не может быть ответом")
        except Exception:
            if loc < 0:
                print("Ответ больше.")
            else:
                print("Ответ меньше.")
    print("\nВерно! Ответ - ",num,sep="")
    print("Вам понадобилось",tries,"попыток")
    loc = 0
    tries = 1
    num = 0
    unum = 0
    ans = 0
    dif = -1
    while True:
        try:
            e = int(input("Еще раз? (0 - да, 1 - нет): "))
            if (e < 0) and (e > 1):
                raise ValueError
            print("\n")
            break
        except ValueError:
            print("",end="")

