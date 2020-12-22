import socket, threading                                                

host = socket.gethostbyname(socket.gethostname())                                                 
port = 12345                                                             
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)              
server.bind((host,port))                                              
server.listen()                                #Starts listening for incoming connections
DISCONNECT_MESSAGE = "EXIT"
clients = []
names = []

def broadcast(message):                                                 
    for client in clients:
        client.send(message)

def handle(client): 
    connected = True                                        
    while connected:
        try:                                                          
            message = client.recv(1024)
            broadcast(message)

            if message == DISCONNECT_MESSAGE:
                break
              


        except:                                                        
            index = clients.index(client)
            clients.remove(client)
            client.close()
            name = names[index]
            broadcast('{} left!'.format(name).encode('ascii'))
            names.remove(name)
            break 

    client.close()   
                


def receive():
                                                              
    while True:
        client, address = server.accept()
        print("Connected with {}".format(str(address)))       
        client.send('NAME'.encode('ascii'))
        name = client.recv(1024).decode('ascii')
        names.append(name)
        clients.append(client)
        print("{} is here!".format(name))
        broadcast("{} joined!".format(name).encode('ascii'))
        client.send('Connected to server!'.encode('ascii'))
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()
        broadcast("[No. of Users:] {}".format(threading.activeCount() - 1).encode('ascii'))
print("Server Starting...")
print(f"[STARTED] CONNECT TO SERVER ON {host}")
receive()          