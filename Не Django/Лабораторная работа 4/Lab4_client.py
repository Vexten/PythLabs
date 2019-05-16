import socket

io = socket.socket()
op = ""
while True:
    try:
        host = input("Введите IP адрес сервера: ")
        io.connect((host,322))
        break
    except OSError:
        print("Нет сервера по данному адресу.")
while True:
    while op == "":
        op = input("Введите команду: ")
    op = op.upper()
    io.send(op.encode())
    if op == "EXIT": break
    op = ""
    inp = io.recv(1024).decode()
    print(inp)
io.close()
