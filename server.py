import socket

TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 1024  # Normally 1024, but we want fast response

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)

conn, addr = s.accept()
while True:
    data = conn.recv(BUFFER_SIZE)
    if not data:
        break
    print("received data:", data)
    good_boy = "https://memepedia.ru/wp-content/uploads/2019/06/keanu-meme.jpg"
    print(good_boy)
    conn.send(data)  # echo
conn.close()