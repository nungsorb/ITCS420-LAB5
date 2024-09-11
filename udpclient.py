import socket, time

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
msgFromClient = input('Enter a number: ')
client.sendto(msgFromClient.encode('ascii'), (socket.gethostname(), 2233))

msgFromServer = client.recvfrom(1024)
msgFromServer = msgFromServer[0].decode('ascii')
print('6388118: {} {}'.format(time.asctime(), msgFromServer))