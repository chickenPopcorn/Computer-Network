# chat_client.py

import sys, socket, select, signal, getpass

RECV_BUFFER = 4096 # Max buffer size

HIDDEN_LIST = ["entered password letters and digits only: ",
               "entered password letters and digits only!!!: ",
               "Please enter your password "]

# Server will exit gracefully upon CTR_C keyboard input
def Exit_gracefully(signal, frame):
    print('Exited gracefully!')
    sys.exit(0)

# Main client function
def chat_client():
    if(len(sys.argv) < 3):
        print 'Usage : python chat_client.py hostname port'
        sys.exit()
    # parse the port number
    try:
        host = socket.gethostbyname(sys.argv[1])
        port = int(sys.argv[2])
    except:
        print 'Wrong format for host and/or port number'
        sys.exit()
    # creating socket
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(2)
    except:
        print "Socket creation failed"
        sys.exit()
    # connect to remote host
    try:
        s.connect((host, port))
    except:
        print 'Unable to connect'
        sys.exit()

    print 'Connecting to remote host'

    sys.stdout.flush()

    while 1:
        socket_list = [sys.stdin, s]

        # Get the list sockets which are readable
        read_sockets, write_sockets, error_sockets = select.select(socket_list, [], [])

        for sock in read_sockets:
            if sock == s:
                # incoming message from remote server, s
                try:
                    data = sock.recv(RECV_BUFFER)
                except:
                    print "Recv from server failed"
                    sys.exit()
                if not data:
                    print '\nDisconnected from chat server'
                    sys.exit()
                else:
                    # if it's promp the password then hide password from displaying
                    if data in HIDDEN_LIST:
                        s.send(getpass.getpass(data))
                    else:
                        sys.stdout.write(data.decode('utf8'))
                        sys.stdout.flush()

            else:
                # user entered a message
                try:
                    msg = sys.stdin.readline()
                    s.send(msg.decode('utf-8').encode('utf8'))
                    sys.stdout.flush()
                except:
                    print "send failed"
                    sys.exit()

if __name__ == "__main__":
    signal.signal(signal.SIGINT, Exit_gracefully)
    sys.exit(chat_client())
