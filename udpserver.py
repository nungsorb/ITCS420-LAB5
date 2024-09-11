import time, socket

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server.bind((socket.gethostname(), 2233))
print("Waiting for a client...")

while True:
    clientMsg , clientAddr = server.recvfrom(1024)
    clientMsg = clientMsg.decode('ascii')
    list_temp = list(map(int, clientMsg.split(' ')))
    total = sum(list_temp)
    server.sendto(str(total).encode('ascii'), clientAddr)
    print('6388118: server received from: {} with data {}'.format(clientAddr, clientMsg))