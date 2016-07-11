# chat_server.py
from datetime import datetime
import sys, socket, select, hashlib, re, signal, thread

HOST        = ''
RECV_BUFFER = 4096 # Max buffer size
BLOCK_TIME  = 60 # Block time for failed authentication in seconds
MAX_TRY     = 3 # Max num of tried for authentication
TIME_OUT    = 30 # inactive time in minutes limit before loged out
LOGIN_TIME  = 60 # time limit for user to request last login
MINUTE      = 60 # num of seconds in a minute


# store usernames and passwords
UP_INFO          = {} # {username      :password}
# list of blocked users and their ip
BLOCKED_IP       = {} # {(ip, username):time}
# store login user information
SOCK_IP_USER_ACT = {} # {socket        :(ip, username, last acitve time)}
# saves offline messages for users
OFFLINE_MESSAGES = {} # {user          :[messages]}
# time of users log into server
USER_ENTER_LOG   = {} # {username      :login time}

def register(socket):
    handle_socket_send1(socket, "If you want to register first enter [y]: ")
    command = handle_socket_rec1(socket)
    if command  == "y\n":
        handle_socket_send1(socket, "entered username letters and digits only: ")
        username = handle_socket_rec1(socket)
        matched_user = re.match(r'(\w)+', username)
        while 1:
            if matched_user and not check_usr(matched_user.group(0)):
                break
            else:
                handle_socket_send1(socket, "try another username (letters and digits only): ")
                username = handle_socket_rec1(socket)
                matched_user = re.match(r'(\w)+', username)

        handle_socket_send1(socket, "entered password letters and digits only: ")
        password = handle_socket_rec1(socket)
        matched_pass = re.match(r'(\w)+', password)
        while 1:
            if matched_pass:
                break
            else:
                handle_socket_send1(socket, "entered password letters and digits only!!!: ")
                password = handle_socket_rec1(socket)
                matched_pass = re.match(r'(\w)+', password)

        up_file = open("user_pass.txt",'a')
        up_file.write(matched_user.group(0))
        up_file.write(" ")
        up_file.write(hashlib.sha1(matched_pass.group(0).encode()).hexdigest())
        up_file.write("\n")
        up_file.close()

# Server will exit gracefully upon CTR_C keyboard input
def Exit_gracefully(signal, frame):
    print('Evxited gracefully!')
    sys.exit(0)

# add current ip and username to blocked list
def addAddr((clientIP, uname)):
    global BLOCKED_IP
    BLOCKED_IP[(clientIP, uname)] = datetime.now()

# check if accepted ip and username is in the blocked list
# if not in the blocked list check if blocked time is reached
# if so return false for blocking else return true for not blocking
# if not in the list return true for not blocking
def checkForTime((clientIP, uname)):
    global BLOCKED_IP
    if (clientIP, uname) in BLOCKED_IP:
        if (datetime.now() - BLOCKED_IP[(clientIP, uname)]).total_seconds() < BLOCK_TIME:
            return False
        else:
            return True
    else:
        return True

# reading username and password from a local file
def read_user_info(filename):
    global UP_INFO
    with open(filename, 'r') as myfile:
        for line in myfile:
            (uname, stored_pass) = line.split()
            UP_INFO[uname] = stored_pass
    myfile.close()

# check user entered password after encript it
def check_pass(hashed_password, entered_pass):
    return hashed_password == hashlib.sha1(entered_pass.encode()).hexdigest()

# check if username is in the system
def check_usr(entered_uname):
    global UP_INFO
    return entered_uname in UP_INFO

# check if the user already logged into the server
def duplicate_login(username):
    global SOCK_IP_USER_ACT
    flag = False
    for s in SOCK_IP_USER_ACT:
        if username == SOCK_IP_USER_ACT[s][1]:
            flag = True
    return flag

def try_auth(addr, sockfd, server_socket):
    global SOCK_IP_USER_ACT
    if not authentication(addr, sockfd):
        sockfd.close()
    else:
        print "Client (%s, %s) connected" % addr
        broadcast(server_socket, sockfd,
                  "[%s] entered our chatting room\n" % SOCK_IP_USER_ACT[sockfd][1])
        read_offline(sockfd, SOCK_IP_USER_ACT[sockfd][1])

def try_read_user_info():
    try:
        read_user_info('user_pass.txt') # read in all usernames and passwords
    except:
        print "Usernames and passwords filename incorrect"
        sys.exit()

# authentication user entered information against stored user informationcheck
# for duplicate loging, ip and user name blocking, add multiple failed entry
# to block list all under the preset maxinum try
def authentication(addr, socket):
    global UP_INFO, BLOCKED_IP, SOCK_IP_USER_ACT, USER_ENTER_LOG
    block_flag = False
    enter_flag = False
    count = 0
    try_read_user_info()
    register(socket)
    try_read_user_info()
    while not block_flag and count < MAX_TRY:
        count += 1
        # reading username
        handle_socket_send1(socket, 'Please enter your username ')
        try:
            entered_uname = handle_socket_rec1(socket).split('\n')[0]
        except:
            return enter_flag
        # test for blocking or not
        if not checkForTime((addr[0], entered_uname)):
            # blocked
            handle_socket_send1(socket, 'Connection rejected\n')
            return enter_flag
        # reading password
        handle_socket_send1(socket, 'Please enter your password ')
        try:
            entered_pass = handle_socket_rec1(socket).split('\n')[0]
        except:
            return enter_flag
        if duplicate_login(entered_uname):
            # check for duplicate login
            handle_socket_send1(socket, 'username already logged in\n')
            enter_flag = False
            block_flag = True
        elif check_usr(entered_uname) and check_pass(UP_INFO[entered_uname], entered_pass):
            # check username and password in the system or not
            handle_socket_send1(socket, 'entered the right password\n')
            enter_flag                    = True
            block_flag                    = True
            USER_ENTER_LOG[entered_uname] = datetime.now()
            SOCK_IP_USER_ACT[socket]    = (addr, entered_uname, datetime.now())
        else:
            # if not in the system reject
            handle_socket_send1(socket, 'the username and password do not match\n')
            block_flag = False
            enter_flag = False
    if not block_flag:
        # add to block list after failing within max try
        addAddr((addr[0], entered_uname))
        handle_socket_send1(socket, 'Maxinum try reached\n')
    return enter_flag

# handle socket recieve before user logged in
def handle_socket_rec1(sock_from):
    msg = ""
    try:
        msg = sock_from.recv(RECV_BUFFER)
    except:
        sock_from.close()
    return msg

# handle socket send before user logged in
def handle_socket_send1(sock_to, message):
    try:
        sock_to.send(message)
    except:
        # broken socket connection
        sock_to.close()

# handle socket send when user logged in will broadcast to other user to update if failed
def handle_socket_rec2(sock_from, server_socket):
    global SOCK_IP_USER_ACT
    msg = ""
    try:
        msg = sock_from.recv(RECV_BUFFER)
    except:
        logout(sock_from, server_socket)
    return msg

# handle socket send when user logged in will broadcast to other user to update if failed
def handle_socket_send2(sock_to, message, server_socket):
    global SOCK_IP_USER_ACT
    try:
        sock_to.send(message)
    except:
        logout(sock_to, server_socket)

# handle last request, tell user which other users logged in in the last
# period of time, which is under the preset max
def last(server_socket, sock_from, input):
    global SOCK_IP_USER_ACT, USER_ENTER_LOG
    time = re.match(r'(\s*)(\d+)(.*)', input)
    if time:
        int_time = int(time.group(2))
        if int_time >= 0 and int_time <= LOGIN_TIME:
            user_list = []
            for user in USER_ENTER_LOG:
                time_in_min = (datetime.now() - USER_ENTER_LOG[user]).total_seconds() / MINUTE
                if time_in_min <= int_time and user != "Server":
                    user_list.append(user)
            message = ""
            if not user_list:
                message = "No one "
            else:
                for u in user_list:
                    message += "[" + u + "]" + " "
            message += "was/were logged in the last " + str(int_time) + " minute(s)\n"
            handle_socket_send2(sock_from, message, server_socket)
    else:
        command_failed(sock_from, server_socket)

# handle who request, check who is currently online
def who(server_socket, sock):
    global SOCK_IP_USER_ACT
    message = ""
    for u in get_current_users():
        if u[1] != "Server":
            message += "[" + u[1] + "]" + " "
    message += "currently online\n"
    handle_socket_send2(sock, message, server_socket)

# broadcast chat messages to all connected clients
def broadcast(server_socket, sock, message):
    global SOCK_IP_USER_ACT
    if len(SOCK_IP_USER_ACT) == 1:
        return
    for socket_to in SOCK_IP_USER_ACT:
        # send the message only to peer
        if socket_to != server_socket and socket_to != sock:
            handle_socket_send2(socket_to, message, server_socket)

# if command is incorrect, send user failed command message
def command_failed(socket_to, server_socket):
    global SOCK_IP_USER_ACT
    message = "your command failed\n"
    handle_socket_send2(socket_to, message, server_socket)

# get current online users' names
def get_current_users():
    global SOCK_IP_USER_ACT
    user_name_list = []
    for s in SOCK_IP_USER_ACT:
        if s != "0":
            user_name_list.append(SOCK_IP_USER_ACT[s])
    return user_name_list

# test send comand and distinguish it is send to one user or more
# and send the message if successfully parsed the command
# else send command failed message
def send(sock_from, input, server_socket):
    global SOCK_IP_USER_ACT, UP_INFO
    user_from = SOCK_IP_USER_ACT[sock_from][1]
    send_one = re.match(r'(\w*)(\s+)(.*)', input)
    send_more = re.match(r'(\()(\s*)(.*)(\s*)(\))(\s+)(.*)', input)
    if send_one:
        to_whom = send_one.group(1)
        message = send_one.group(3)
        message = '[' + user_from + '] ' + message + '\n'
        # send to specified user other than itself
        for sock_to in SOCK_IP_USER_ACT:
            user_name = SOCK_IP_USER_ACT[sock_to][1]
            if user_name == to_whom and user_name != user_from:
                handle_socket_send2(sock_to, message, server_socket)
        if to_whom in UP_INFO and to_whom not in\
                get_current_users() and to_whom != user_from:
            save_offline(user_from, to_whom, message)
    elif send_more:
        users_list = send_more.group(3).split()
        message = send_more.group(7)
        message = '[' + user_from + '] ' + message + '\n'
        # present user from sending message to itself
        try:
            users_list.remove(user_from)
        except:
            pass
        # send to specified users
        for sock_to in SOCK_IP_USER_ACT:
            if SOCK_IP_USER_ACT[sock_to][1] in users_list:
                handle_socket_send2(sock_to, message, server_socket)
                users_list.remove(SOCK_IP_USER_ACT[sock_to][1])
        for to_whom in users_list:
            if to_whom in UP_INFO:
                    save_offline(SOCK_IP_USER_ACT[sock_from][1], to_whom, message)
    else:
        command_failed(sock_from, server_socket)

# broadcast to all users that one user has logged out
def logout(sock, server_socket):
    global SOCK_IP_USER_ACT
    sock.close()
    out_user = SOCK_IP_USER_ACT[sock][1]
    del SOCK_IP_USER_ACT[sock]
    broadcast(server_socket, sock,"[%s] left our chatting room\n" % out_user)


# test user for inactive under preset time period
# if inactive for more than that time, log it out and broadcast to all users
def inactive_logout(server_socket):
    global SOCK_IP_USER_ACT
    log_out = []
    for s in SOCK_IP_USER_ACT:
        if s != server_socket:
            inactive_time = (datetime.now() - SOCK_IP_USER_ACT[s][2]).total_seconds() / MINUTE
            if inactive_time > TIME_OUT:
                log_out.append(s)
    for logout_sock in log_out:
        print "kicked inacive user"
        logout(logout_sock, server_socket)

# process user input for commands
def process_input(input):
    matchObj = re.match(r'(^find|^who|^last|^broadcast|^send|^logout)(\s+)(.*)', input, re.I)
    return matchObj

# process user command with preset commands if fail send command_failed message
def process_command(matchObj, socket_from, server_socket):
    global SOCK_IP_USER_ACT, UP_INFO
    if not matchObj:
        command_failed(socket_from, server_socket)
    else:
        command = matchObj.group(1)
        more_input = matchObj.group(3)
        if command == "who":
            who(server_socket, socket_from)
        elif command == "last":
            last(server_socket, socket_from, more_input)
        elif command == "broadcast":
            broadcast(server_socket, socket_from, "\r" + '[' + SOCK_IP_USER_ACT[socket_from][1] +
                      '] ' + matchObj.group(3) + "\n")
        elif command == "send":
            send(socket_from, more_input, server_socket)
        elif command == "logout":
            logout(socket_from, server_socket)

# read all offline message back to user
def read_offline(socket_to, username):
    global OFFLINE_MESSAGES
    if username in OFFLINE_MESSAGES.keys():
        for message in OFFLINE_MESSAGES[username]:
            handle_socket_send1(socket_to, message)
        del OFFLINE_MESSAGES[username]

# save offline message is user is not online
def save_offline(user_from, user_to, msg):
    global OFFLINE_MESSAGES
    message = "offline message from " + msg
    if user_to in OFFLINE_MESSAGES:
        OFFLINE_MESSAGES[user_to].append(message)
    else:
        OFFLINE_MESSAGES[user_to] = []
        OFFLINE_MESSAGES[user_to].append(message)

# main chat server creating socket handle incoming connection and requests
def chat_server():
    global UP_INFO, SOCK_IP_USER_ACT
    # test for correct command line arugments
    if(len(sys.argv) < 2):
        print 'Usage : python Server.py port'
        sys.exit()
    # port from command line argument
    try:
        PORT = int(sys.argv[1])
    except:
        print 'Wrong format for port number'
        sys.exit()

    # creating server socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((HOST, PORT))
    server_socket.listen(5)

    # add server socket object to the list of readable connections
    SOCK_IP_USER_ACT[server_socket] = ("0","Server", datetime.now())
    print "Chat server started on port " + str(PORT)

    while 1:
        # get the list sockets which are ready to be read through select
        # 4th arg, time_out  = 0 : poll and never block
        ready_to_read,ready_to_write,in_error = select.select(SOCK_IP_USER_ACT.keys(),[],[],0)
        # check for inactive users
        try:
            inactive_logout(server_socket)
        except:
            pass
        # read in users' input

        for sock in ready_to_read:
            # a new connection request recieved
            if sock == server_socket:
                sockfd, addr = server_socket.accept()

                # check for authentication
                thread.start_new_thread(try_auth, (addr, sockfd, server_socket))

            # a message from a client, not a new connection
            else:
                # process data recieved from client,
                try:
                    # receiving data from the socket.
                    data = handle_socket_rec2(sock, server_socket)

                    if data:
                        # update activity time for user
                        SOCK_IP_USER_ACT[sock] = (SOCK_IP_USER_ACT[sock][0],
                                                  SOCK_IP_USER_ACT[sock][1],
                                                  datetime.now()
                                                  )

                        process_command(process_input(data), sock, server_socket)
                    else:
                        # remove the socket that's broken
                        logout(sock, server_socket)
                # exception
                except:
                    continue
    server_socket.close()

# main
if __name__ == '__main__':
    # gracefully exit upon control c
    signal.signal(signal.SIGINT, Exit_gracefully)
    chat_server()
