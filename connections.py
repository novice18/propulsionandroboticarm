
def create_socket():
    try:
        #Creating following 3 global variables
        global host
        global port
        global s         #This is socket variable which is named s

        #Assigning values to these 3 global variables
        host = ""
        port = 9999
        s = socket.socket()    # Creating a socket and assigning it to s

    except socket.error as msg:
        print("Socket creation error: " + str(msg))


######################################################################################################################
########## # Binding the socket and listening for connections:
# Before accepting connection we listen for connections after binding host and port with the socket
######################################################################################################################
def bind_socket():
    try:
        # Declaring them again so that we can use the above global variable
        global host
        global port
        global s
        print("Binding the Port: " + str(port))

        s.bind((host, port))
        s.listen(5)

    except socket.error as msg:
        print("Socket Binding error" + str(msg) + "\n" + "Retrying...")
        bind_socket()



def createconnection():
    create_socket()
    bind_socket()
