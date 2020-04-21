import socket
import os
import threading
value = []
HOST = '10.70.235.101'

def main(s):
    req = input("upload or download (u/d) or exit ")
    if req == "exit":
        s.send(req.encode())
        exit()
    elif req == "u":
        s.send(req.encode())
        upload(s)
    elif req == "d":
        s.send(req.encode())
        download(s)
    else:
        print("wrong input")
        main(s)
    main(s)


def upload(s):
    file = input("enter file path ")
    if not os.path.isfile(file):
        print("not a file")
        upload(s)
    name = file.split("\\")[-1]
    print(name)
    with open(file, 'rb') as the_file:
        sz = len(the_file.read())
    s.send((name + "\\" + str(sz)).encode())
    threading.Thread(target=newFile, args=(s, file)).start()
    reconect()


def newFile(s, file):
    while True:
        data = s.recv(1024).decode()
        print(data)
        data = data.split()
        newServer(data[1], data[2], data[3], file)


def download(s):
    global value
    data = s.recv(1024).decode()
    if data == "waiting for more peers":
        data = s.recv(2048).decode()
    print(data)
    data = data.split(':')
    dest = input("insert file name ")
    dest = check(data, dest)
    s.send(dest.encode())
    data = s.recv(1024).decode().split()
    value = []
    i = 1
    for x in data[1:]:
        threading.Thread(target=newClient, args=(x, i)).start()
        i += 1
    while True:
        if len(value) == int(data[0]):
            break
    string = b""
    index = 1
    while index <= int(data[0]):
        for i in value:
            if i[1] == index:
                string += i[0]
                value.remove(i)
                break
        index += 1
    file = open(dest, 'wb')
    file.write(string)
    print("done " + dest)
    threading.Thread(target=newFile, args=(s, dest)).start()
    reconect()


def newClient(dest, id):
    global value
    port = 5050
    c = socket.socket()
    c.connect((dest, port))
    received = c.recv(1024)
    while received[-4:] != b'done':
        received += c.recv(1024)
    received = received[:-4]
    value.append([received, id])
    c.close()


def reconect():
    port = 5000
    s = socket.socket()
    s.connect((HOST, port))
    main(s)


def newServer(dest, start, stop, file):
    with open(file, 'rb') as the_file:
        my_string = the_file.read()[int(start):int(stop)]
    port = 5050
    ser = socket.socket()
    ser.bind(("0.0.0.0", port))
    ser.listen(5)
    c, addr = ser.accept()
    while addr[0] != dest:
        c, addr = ser.accept()
    c.send(my_string)
    c.send(b"done")
    c.close()


def check(files, name):
    for x in files:
        if name == x:
            return name
    print("not in list")
    return check(files, input("insert file name "))


if __name__ == '__main__':
    HOST = '10.70.235.101'
    port = 5000
    s = socket.socket()
    s.connect((HOST, port))
    main(s)
