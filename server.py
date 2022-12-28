import socket
HOST = 'localhost'
PORT = 8002

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind ((HOST, PORT))

sock.listen(5)

while True:
    ### Enviando uma mensagem ###
    # novoSock, _ = sock.accept()
    # mensagem = novoSock.recv(1024).decode() - Decodificando(desfazendo o binario) da mensagem.
    # print(mensagem)
    # novoSock.send(b'ok')

    novoSock, _ = sock.accept()
    nomeArquivo = novoSock.recv(1024).decode()
    novoArquivo = novoSock.recv(10000000)

    with open (f'arquivos/{nomeArquivo}.png', 'wb') as arq:
        arq.write(novoArquivo)

    novoSock.send(b'ok')