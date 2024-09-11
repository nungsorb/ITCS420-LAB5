import time, socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((socket.gethostname(), 41111))
print("Waiting for connection...")
server.listen(5)

while True:
    client , clientAddr = server.accept()
    print("Received connection from %s" % str(clientAddr))
    clientMsg = client.recv(1024)
    clientMsg = clientMsg.decode("ascii")
    list_temp = list(map(int, clientMsg.split(' ')))
    total = sum(list_temp)
    print("6388118: server received: {}".format(clientMsg))
    msg_client = "6388118: " + time.asctime() + " " + str(total)
    client.send(msg_client.encode('ascii'))
    client.close()
server.close()