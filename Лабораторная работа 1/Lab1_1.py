import math
print("|(a^2/b^2 + c^2*a^2)/(a + b + c(k-a/b^3)) + c + c(k/b - k/a)|")
inpl = ["a","b","c","k"]
while True:
    try:
        i = 0
        inp = []
        while True:
            try:
                print("Введите ", inpl[i], ": ", sep="", end="")
                inp.append(float(input()))
                i += 1
                if i == 4:
                    break
            except ValueError:
                print("Необходимо число.")
        out = math.fabs(((inp[0]**2/inp[1]**2) + (inp[2]**2*inp[0]**2))/(inp[0] + inp[1] + inp[2]*(inp[3]-(inp[0]/inp[1]**3))) + inp[3] + inp[3]*((inp[3]/inp[2]) - (inp[3]/inp[0])))
        print("Ответ:",out)
        break
    except ZeroDivisionError:
        print("В выражении есть деление на ноль. Введите другие числа.")
