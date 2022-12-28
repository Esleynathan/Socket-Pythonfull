import socket

HOST = 'localhost'
PORT = 8002

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.connect((HOST, PORT))

sock.send(input('Digite sua mensagem: ').encode())

sock.send(b"enviado2")

confirmacao = sock.recv(1024)
if confirmacao == b'ok':
    print('Sua mensagem recebida.')