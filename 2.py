import socket, threading



client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)     
client.connect(('192.168.100.3', 12345))   
DISCONNECT_MESSAGE = "EXIT"  
name = input("Enter you Name: ")

def receive():
    while True:                                                
        try:
            message = client.recv(1024).decode('ascii')
            if message == 'NAME':
                client.send(name.encode('ascii'))
            else:
                print(message)
        except:                                                 
            print("An error occured!")
            client.close()
            break
def write():
    while True:                                                 
        message = '{}: {}'.format(name, input(''))
        client.send(message.encode('ascii'))

receive_thread = threading.Thread(target=receive)               
receive_thread.start()
write_thread = threading.Thread(target=write)                   
write_thread.start()
