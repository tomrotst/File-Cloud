import socket
import threading
HOST = '0.0.0.0'
PORT = 5000
peers = []
files = []


def notify(dest, addr):
    x = dest[2:]
    holders = []
    count = 0
    for y in x:
        count += 1
        holders.append(y[0])
    start = 0
    chunks = int(int(dest[1]) / count)
    stop = chunks
    i = 1
    for a in holders:
        a.send(("begin " + addr + " " + str(start) + " " + str(stop)).encode())
        start = stop
        if i == count:
            stop = int(dest[1])-1
        else:
            stop += chunks
        i += 1
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
        c, addr = ser.accept()
        peers.append([c, addr[0]])
        threading.Thread(target=getRequest, args=(c, addr[0])).start()


def getRequest(c, addr):
    data = c.recv(1024).decode()
    if data == "u":
        data = c.recv(1024).decode().split("\\")
        name = data[0]
        size = data[1]
        files.append([name, size, [c, addr]])
        print(addr)
    elif data == "d":
        c.send("waiting for more peers".encode())
        while len(files) == 0:
            if len(files) > 0:
                break
        a = []
        while len(a) == 0:
            for x in files:
                bol = True
                for y in x[1:]:
                    if y[1] == addr:
                        bol = False
                        break
                if bol:
                    a.append(x[0])
        chk = '-'.join(a)
        c.send(chk.encode())
        data = c.recv(1024).decode()
        bol, dest = check(data, c)
        print("checking")
        if bol:
            print("done")
            if notify(dest, addr):
                x = dest[2:]
                string = str(len(x))
                for y in x:
                    string += " " + y[1]
                print(string)
                c.send(string.encode())
        for x in files:
            if x[0] == data:
                x.append([c, addr])
    else:
        c.close()
        for x in peers:
            if x[0] == c:
                peers.remove(x)


if __name__ == "__main__":
    main()
