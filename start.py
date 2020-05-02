import socket
import threading
import time
HOST = '0.0.0.0'
PORT = 5000
files = []


def notify(dest, addr):
    holders = []
    count = 0
    for x in dest[2:]:
        count += 1
        holders.append(x[0])
    start = 0
    chunks = int(int(dest[1]) / count)
    stop = chunks
    i = 1
    for a in holders:
        try:
            print("AAAA")
            a.send(("begin " + addr + " " + str(start) + " " + str(stop)).encode())
            start = stop
            if i == count:
                stop = int(dest[1])-1
            else:
                stop += chunks
            i += 1
        except:
            continue
    return True


def check(data, c):
    for i in files:
        if data == i[0] and i[2][0] != c:
            return True, i
    return False, ""


def main():
    ser = socket.socket()
    ser.bind((HOST, PORT))
    ser.listen(5)
    while True:
        try:
            c, addr = ser.accept()
            threading.Thread(target=getRequest, args=(c, addr[0])).start()
        except:
            continue


def getRequest(c, addr):
    print("a")
    try:
        data = c.recv(1).decode()
        print(data)
    except:
        c.close()
        remove(addr)
        return
    if data == "u":
        print("b")
        try:
            data = c.recv(1024).decode()
            print(data)
            data = data.split(":")
            print(data)
        except:
            print("error")
            remove(addr)
            return
        name = data[0]
        size = data[1]
        files.append([name, size, [c, addr]])
        print(addr)
    elif data == "d":
        print("got in")
        a = []
        for x in files:
            bol = True
            for y in x[2:]:
                if y[1] == addr:
                    bol = False
                    break
            if bol:
                a.append(x[0])
        chk = ':'.join(a)
        try:
            print(chk)
            if chk == "":
                print("send empty")
                c.send("empty".encode())
                print("exiting")
                return
            else:
                c.send(chk.encode())
                print("e")
                data = c.recv(1024).decode()
                print("f")
        except:
            print("wrong")
            remove(addr)
            return
        bol, dest = check(data, c)
        print("checking")
        if bol:
            print("done")
            if notify(dest, addr):
                string = str(len(dest[2:]))
                for x in dest[2:]:
                    string += " " + x[1]
                print(string)
                try:
                    c.send(string.encode())
                except:
                    remove(addr)
                    return
                try:
                    data = c.recv(1024).decode()
                    print(data)
                except:
                    print("error")
                    remove(addr)
                    return
        for x in files:
            if x[0] == data:
                print("appended" + data)
                x.append([c, addr])
    else:
        c.close()
        remove(addr)


def remove(addr):
    for x in files:
        for y in x[2:]:
            if y[1] == addr:
                x.remove(y)


if __name__ == "__main__":
    print('STARTED')
    main()

