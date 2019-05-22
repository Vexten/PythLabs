import socket

io = socket.socket()
op = ""
while True:
    while True:
        try:
            host = input("Введите IP адрес сервера (0 - выход): ")
            if host != "0": io.connect((host,5025))
            else: op = "0"
            break
        except OSError:
            print("Нет сервера по данному адресу.")
    while True:
        try:
            while op == "":
                op = input("Введите команду (help - помощь): ")
            op = op.upper()
            if op != "0": io.send(op.encode())
            else: op = "EXIT"
            if op == "EXIT": break
            op = ""
            inp = io.recv(1024).decode()
            print(inp)
        except ConnectionAbortedError:
            print("Соединение с сервером разорвано.")
            break
    if op == "EXIT": break
io.close()
