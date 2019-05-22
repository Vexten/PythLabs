import socket, datetime, locale

locale.setlocale(locale.LC_ALL, "")

io = socket.socket()
io.bind(("",5025))
io.listen(1)

while True:
    try:
        cl, addr = io.accept()
        print(addr,"подключился")
        while True:
            inp = cl.recv(1024).decode()
            try:
                inp = inp.upper()
                if inp == "HELP":
                    op = """date time - возвращает дату и время сервера
es - выключение сервера
exit - отключиться от сервера и закрыть клиент"""
                elif inp == "DATE TIME":
                    op = datetime.datetime.now().strftime("%c")
                elif inp == "EXIT":
                    print(addr,"отключился")
                    cl.close()
                elif inp == "ES":
                    op = "Выключение сервера..."
                    print(op)
                else:
                    raise ValueError
                if inp != "EXIT": cl.send(op.encode())
                else: break
                if inp == "ES": break
            except ValueError:
                cl.send("Такой команды нет.".encode())
        if inp == "ES": break
    except ConnectionResetError:
        print(addr,"разорвал соединение.")
cl.close()
