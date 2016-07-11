#!/usr/bin/python
# -*- coding: UTF-8 -*-
import socket
import urllib
import re
import unicodedata

s    = socket.socket() # Create a socket object
host = socket.getfqdn() # Get local machine name
port = 7717
s.bind((host, port)) # Bind to the port

print 'Starting server on', host, port
print 'The Web server URL for this would be http://%s:%d/' % (host, port)

s.listen(5)                 # Now wait for client connection.

welcome_en = 'welcome'
welcome_ko = '\xED\x99\x98\xEC\x98\x81'
welcome_fi = 'Tervetuloa'
form = """<form>
  	     Test Input:<br>
  		  <input type="text" name="test"><br>
  		  <input type="submit">
      </form>"""

reg = re.compile("[a-zA-Z0-9]*(%[a-zA-Z0-9][a-zA-Z0-9])*[a-zA-Z0-9]*")

print 'Entering infinite loop; hit CTRL-C to exit'
while True:
    # Establish connection with client.
    c, (client_host, client_port) = s.accept()
    print 'Got connection from', client_host, client_port
    rqt=c.recv(1000)

    try:
        rqt_lng  =rqt.split("Accept-Language",1)[1]
        rqt_path =rqt.split("GET",1)[1]
    	rqt_path =rqt_path.split(' ')[1]

    except IndexError:
    	print 'bad request'

    if 'ko' in rqt_lng:
        message = welcome_ko
    elif 'fi' in rqt_lng:
        message = welcome_fi
    else:
        message = welcome_en

    c.send('HTTP/1.0 200 OK\n')
    c.send('Content-Type: text/html\n')
    c.send('\n')

    result = ''
    if '?test=' in rqt_path:
        rqt_key =rqt_path.split("=",1)[1]
        print rqt_key
        text_output = urllib.unquote(rqt_key)

        flag = False
        for char in text_output.decode("UTF-8"):
            if unicodedata.category(char) in ['Lu', 'Ll', 'Lo', 'Nd', 'Lt', 'Lm', 'Nl', 'No']:
                flag = True

        if ("+" in rqt_key) or (not reg.match(rqt_key)) or (not flag):
            rqt_key = urllib.unquote(rqt_key)
            meet    = "doesn't meet"
            result  ="the input is "+rqt_key+". It "+meet+" the criterion."
        else:
            meet        = "meets"
            b_len       = len(text_output.decode("UTF-8"))
            c_len       = len(text_output)
            result      ="the input is "+text_output+". It "+meet+" the criterion. "+"The length of the string in characters is "+str(b_len) +" in byte is "+ str(c_len)

    c.send("""
        <html>
        <body>
        <h1>"""+message+"""
        </h1>"""+form+result+"""
        </body>
        </html>
    """)

    c.close()
