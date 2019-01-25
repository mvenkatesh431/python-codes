import socket

def client():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    #host = socket.gethostname()
    port = 9779

    s.connect(('127.0.0.1',port))   # observe it's tuple
    print("Listening on local and Port ", port)

    message = input("Your message : ")

    while message.lower().strip() != 'bye':
       s.send(message.encode())
       recvData = s.recv(1024).decode()
       print("Recieved data : ", recvData)
       message = input("Your Reply -> ")

    conn.close()

client()
