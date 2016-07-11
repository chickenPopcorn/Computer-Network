Ruicong Xie rx2119 HW2

1.
- a. request-immediate-response
- b. publish-subscribe/notify
- c. multicast
- d. request-wait-response

2.
- FTP: may run in active or passive mode, In both cases, the client creates a TCP control connection from a random, usually an unprivileged, port N to the FTP server command **port 21**. In active mode, the client starts listening for incoming data connections from the server on port M. It sends the FTP command PORT M to inform the server on which port it is listening. By default, M=N. The server then initiates a data channel to the client from its **port 20**, the FTP server data port.

- Nest: **Nest Weave** communication protocol lets devices talk directly to each other and to Nest products. Nest Weave solves many issues associated with connecting products in the home, including the ability to connect power-constrained devices as well as devices that require low latency and redundancy. It uses 802.15.4 and Wi-Fi 802.11 b/g/n.

Note | Port Num | Protocol
------------ | ------------- | -------------
Device-to-device | 11095 | TCP
Device-to-service | 11095 | UDP




3 see server.py

4 http://unicode-table.com/
- a. U+0054 54
- b. U+05D1 D7 91
- c. U+20AC E2 82 AC
- d. U+6728 E6 9C A8
- e. U+2764 E2 9D A4

5 see  bach_family.json and bach_family.xml
6 see index.php and page2.php

7
  - a. 16 RRT
  - b. 8 RRT
  - c. 9 RRT
  - d. 3 RRT

8
  - a. 6 simultaneous connections for my HTTP/1.1 connection and all image requests are send simultaneously for the HTTP/2.0.
  - b. With pipelining http/1.1 is in theory faster than HTTP/1.0 with more simultaneous connections, however it still suffers from head-of-line block. Because HTTP is a stateless connection, client must response in the sequence of requests. Meaning if early a response is blocked all the subsequence response must wait for it to finish. On the other hand HTTP2.0 support full multiplexing which addresses the problem by allowing multiple request and response messages to be in flight at the same time; This, in turn, allows a client to use just one connection per origin to load a page.
