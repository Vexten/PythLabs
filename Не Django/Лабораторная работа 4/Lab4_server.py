import socket, datetime, locale

locale.setlocale(locale.LC_ALL, "ru_RU")

io = socket.socket()
io.bind(("",322))
io.listen(1)

while True:
    try:
        cl, addr = io.accept()
        print(addr,"подключился")
        while True:
            inp = cl.recv(1024).decode()
            try:
                inp = inp.upper()
                if inp == "DATE TIME":
                    op = datetime.datetime.now().strftime("%c")
                elif inp == "EXIT":
                    print(addr,"отключился")
                    cl.close()
                elif inp == "0":
                    op = "Выключение сервера..."
                    print(op)
                else:
                    raise ValueError
                if inp != "EXIT": cl.send(op.encode())
                if inp == "0":
                    break
            except ValueError:
                cl.send("Такой команды нет.".encode())
        if inp == "0":
            break
    except ConnectionResetError:
        print(addr,"разорвал соединение.")
cl.close()
