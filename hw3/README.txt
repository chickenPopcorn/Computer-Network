1. Brief description of my code
There are Server.py and Client.py. The Server acts as a server for the chat room
Clients. They are heavily commented and correctly formatted according to guidance of
lint Flake8 for python. Users can register as a new user using digits and letters only
for password and username. The server can handle multiple clients at the same time using thread.
It reading user login information from a local file, encrypt them and save them in
a dictionary. It is able to connect all users through socket and process the command
who, last, broadcast, logout, send(one or multiple users). It is also able to log
offline messages.  It handles all sock errors accordingly.

The Client.py is a simple client side socket program. User can use both domain name
and ip address to connect to server It send data from standard input from user to
server and receive data from other clients through server. Client.py is able to handle
utf-8 as user input for message using encode and decode. When prompt with password
information, it hides that data from displaying and send it to server.

2. Development environment
It is developed on Ubuntu 15.10 It runs python 2.7 But it should also run on any machine
using python 2.7 with sys, re, signal, getpass, select, socket, datetime

3. To_run
If only one version of python is installed simple do with example of using 4119 as port number
any working port number should do the job, and Localhost as a sample host address
-Server side
python Server.py 4119
-Client side
python Client.py Localhost 4119
For login information lookup user_pass.txt, which is identical as the one in instruction
(encrypt.py encrypts user information no need to run it)

4. Sample Command
who
last number_of_minutes_below_60
send user message
send (user1 user2 ....) message
broadcast message
logout
All commands are working as specified by the instruction


5. Additional features
a. offline message
when send message to users that are currently offline. message will be stored in a dictionary.
when that user log in in the future it will be displayed to that user message by message with
easy to understand format. After message is display it will be delete from the dictionary. So
Future login will not be prompted with the same messages.

b. register new user
user can type y to register when signed in, else to proceed to login. when register user can choose
their username containing only digits and numbers that does't exist in the database. new username
and password(will be encrypted) will be stored in the user_pass.txt file and loaded into server.

c. hidden password
when user login password information will be hidden for security reasons. The entered password
can be correctly send to server for authentication

d. broadcast user status
Server will automatically broadcast will user login and logout status information to all currently
online users. Even if they are logout for inactive, socket error, and logout voluntarily, which is
more difficult to handle that it sounds. That is why I have two functions to handle socket.

e. whitespace in command
whitespace in command is significant same as instruction, however multiple whitespace is treated as
a single one using regular expression. If user mistyped command send (    user1     user2    )     message
instead of send (user1 user2) message command should work with no problem.
