import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
client.connect((socket.gethostname(), 41111))
print('Enter two numbers: ', end='')
x = input()
client.send(x.encode('ascii'))
data = client.recv(1024)
print(data.decode("ascii"))
client.close()