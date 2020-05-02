import socket
import os
import threading
value = []
HOST = '10.70.235.114'
port = 5000


# TODO
def main_new(s, req, var):
    print('MAIN NEW ENTERED')
    if req == "exit":
        s.send(req.encode())
        exit()
    elif req == "u":
        try:
            s.send(req.encode())
            upload_new(s, var)
        except:
            print("connection aborted")
            exit()
    elif req == "d":
        try:
            new_download(s, var)
        except:
            print("connection aborted")
            exit()


def upload_new(s, file):
    print('UPLOAD NEW ENTERED')
    name = file.split("\\")[-1]
    print(name)
    with open(file, 'rb') as the_file:
        sz = len(the_file.read())
    try:
        s.send((name + ":" + str(sz)).encode())
    except IOError:
        print("connection aborted")
        exit()
    print(file)
    threading.Thread(target=newFile_new, args=(s, file)).start()


def newFile_new(s, file):
    print('NEWFILE NEW ENTERED')
    while True:
        data = ''
        try:
            data = s.recv(1024).decode()
        except IOError:
            print("connection aborted")
            exit()
        print(data + "sdf")
        data = data.split()
        try:
            newServer(data[1], data[2], data[3], file)
        except IOError:
            exit()


def new_download(s, file_sad):
    global value
    data = ''
    dest = ''
    try:
        dest = file_sad
        s.send(dest.encode())
        data = s.recv(1024).decode()
        print(data)
        data = data.split()
    except IOError:
        print("connection aborted")
        exit()
    value = []
    i = 1
    for x in data[1:]:
        print(x)
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
    newpath = "files"
    if not os.path.exists(newpath):
        os.makedirs(newpath)
    s.send(("done "+dest).encode())
    file = open(newpath + "\\" + dest, 'wb')
    file.write(string)
    print("done " + dest)
    threading.Thread(target=newFile_new, args=(s, "files\\"+dest)).start()


def newClient(dest, id):
    global value
    port = 5050
    print("started")
    c = socket.socket()
    try:
        c.connect((dest, port))
        received = c.recv(1024)
    except IOError:
        print("connection aborted")
        exit()
    while received[-4:] != b'done':
        received += c.recv(1024)
    received = received[:-4]
    value.append([received, id])
    c.close()


def newServer(dest, start, stop, file):
    print("newServer " + dest)
    with open(file, 'rb') as the_file:
        my_string = the_file.read()[int(start):int(stop)]
    ser = socket.socket()
    ser.bind(("0.0.0.0", 5050))
    print("started accept")
    ser.listen(5)
    print("accept 1")
    c, addr = ser.accept()
    while addr[0] != dest:
        c, addr = ser.accept()
    print("accept 2")
    try:
        c.send(my_string)
        c.send(b"done")
        c.close()
    except:
        c.close()
    print("done with upload")


def check(files, name):
    for x in files:
        if name == x:
            return name
    print("not in list")
    return check(files, input("insert file name "))
