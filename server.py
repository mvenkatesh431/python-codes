import socket

def server():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    #host = socket.gethostname()
    port = 9779

    s.bind(('',port))   # observe it's tuple
    print("Listening on localhost and  Port ", port)

    s.listen(2)
    conn, addr = s.accept()
    print("Connection Recieved from ", addr)

    while True:
       recvData = conn.recv(1024).decode()
       if not recvData: break
       print("Recieved data : ", recvData)
       sendData = input("Your Reply -> ")
       conn.send(sendData.encode())
    conn.close()

server()

       
