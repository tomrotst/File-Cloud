import socket
import threading
HOST = '0.0.0.0'
PORT = 5000
files = []


def notify(dest, addr):
    #notifiting holders of the file to accept the download request from the peer returns list of ips of active holders
    holders = []
    return_list = []
    count = 0
    for x in dest[2:]:
        try:
            x[0].send("checking".encode())
            holders.append(x[0])
            return_list.append(x[1])
            count += 1
        except:
            continue
    start = 0
    chunks = int(int(dest[1]) / count)
    stop = chunks
    i = 1
    for a in holders:
        try:
            print("AAAA")
            #sends begin ip startBit endBit
            a.send(("begin " + addr + " " + str(start) + " " + str(stop)).encode())
            start = stop
            if i == count:
                stop = int(dest[1])-1
            else:
                stop += chunks
            i += 1
        except:
            continue
    return return_list


def check(data, c):
    #checks if peer already has the file and returns the appropriate cell in the files list
    for i in files:
        if data == i[0] and i[2][0] != c:
            return True, i
    return False, ""


def main():
    #main function for accepting new peers
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
    #recieving request from peer
    try:
        data = c.recv(1).decode()
        print(data)
    except:
        c.close()
        remove(addr)
        return
    if data == "u":
        #received upload
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
        #received download
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
                data = c.recv(1024).decode()
        except:
            print("wrong")
            remove(addr)
            return
        bol, dest = check(data, c)
        print("checking")
        if bol:
            print("done")
            temp = notify(dest, addr)
            string = str(len(temp))
            string += " " + ' '.join(temp)
            print(string)
            #sends list of ips of holders to peer requesting download
            try:
                c.send(string.encode())
            except:
                print("error")
                remove(addr)
                return
            try:
                message = c.recv(1024).decode()
                print(message)
            except:
                print("error")
                remove(addr)
                return
        message = message.split()
        if message[0] == "done":
            #adds peer to list of file holders
            for x in files:
                if x[0] == data:
                    print("appended" + data)
                    x.append([c, addr])
        elif message[0] == "error":
            print("error occured with download of" + message[1])
    else:
        c.close()
        remove(addr)


def remove(addr):
    #removing peer from all instances in files list
    for x in files:
        for y in x[2:]:
            if y[1] == addr:
                x.remove(y)


if __name__ == "__main__":
    print('STARTED')
    main()
