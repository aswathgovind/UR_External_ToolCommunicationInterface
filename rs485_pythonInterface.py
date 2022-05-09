import socket
host = 'robot_ip'
port = 54321         # Remains the same, because it is specified as default port in URCaps code
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
s.sendall(b'Hello rs485 port from ash')
data = s.recv(1024)
s.close()
print('Received', repr(data))