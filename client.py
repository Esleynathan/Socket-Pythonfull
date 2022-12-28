import socket

HOST = 'localhost'
PORT = 8002

arquivo = open('x.png', 'rb')

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.connect((HOST, PORT))

## Solicitando uma mensagem para armazenar ##
# sock.send(input('Digite sua mensagem: ').encode())

sock.send(input('Digite o nome do arquivo: ').encode())
sock.send(arquivo.read())

confirmacao = sock.recv(1024)
if confirmacao == b'ok':
    print('Sua mensagem recebida.')