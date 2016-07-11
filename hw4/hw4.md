hw4
Ruicong Xie
rx2119  

1.
a)
The Whois database is an online repository of information associated with registered domain names. It stores and publicly displays domain name information, such creation and expiration dates, the registrar of record, and its various contacts.
When you register a domain name, we collect this information, per the Internet Corporation for Assigned Names and Numbers (ICANN) regulations for domain name registrars. The information in the Whois database is available to anyone who does a Whois search for a particular domain name. You must enter valid information in your account. If you do not, you risk losing your domain name registration.

b)
whois columbia.edu
Administrative Contact:
Columbia University Computer Operations
Columbia University
615 West 131st Street
CUIT - 5th Floor
New York, NY 10027
UNITED STATES
(212) 854-2652
noc@columbia.edu

ext-ns1.columbia.edu


2.
a)
www.cs.columbia.edu
i.root-servers.net.
192.36.148.17
g.edu-servers.net
192.42.93.30
adns2.berkeley.edu.
128.32.136.14
sundog.ee.columbia.edu.
128.59.64.59
; <<>> DiG 9.8.3-P1 <<>> +trace www.cs.columbia.edu
;; global options: +cmd
.			437916	IN	NS	k.root-servers.net.
.			437916	IN	NS	l.root-servers.net.
.			437916	IN	NS	d.root-servers.net.
.			437916	IN	NS	a.root-servers.net.
.			437916	IN	NS	j.root-servers.net.
.			437916	IN	NS	m.root-servers.net.
.			437916	IN	NS	c.root-servers.net.
.			437916	IN	NS	f.root-servers.net.
.			437916	IN	NS	g.root-servers.net.
.			437916	IN	NS	e.root-servers.net.
.			437916	IN	NS	h.root-servers.net.
.			437916	IN	NS	b.root-servers.net.
.			437916	IN	NS	i.root-servers.net.
;; Received 228 bytes from 128.59.1.3#53(128.59.1.3) in 69 ms

edu.			172800	IN	NS	g.edu-servers.net.
edu.			172800	IN	NS	f.edu-servers.net.
edu.			172800	IN	NS	l.edu-servers.net.
edu.			172800	IN	NS	c.edu-servers.net.
edu.			172800	IN	NS	d.edu-servers.net.
edu.			172800	IN	NS	a.edu-servers.net.
;; Received 272 bytes from 192.36.148.17#53(192.36.148.17) in 31 ms

columbia.edu.		172800	IN	NS	dns2.itd.umich.edu.
columbia.edu.		172800	IN	NS	adns1.berkeley.edu.
columbia.edu.		172800	IN	NS	adns2.berkeley.edu.
columbia.edu.		172800	IN	NS	ns1.lse.ac.uk.
columbia.edu.		172800	IN	NS	sns-pb.isc.org.
columbia.edu.		172800	IN	NS	ext-ns1.columbia.edu.
;; Received 256 bytes from 192.42.93.30#53(192.42.93.30) in 81 ms

cs.columbia.edu.	3600	IN	NS	sundog.ee.columbia.edu.
cs.columbia.edu.	3600	IN	NS	diana.cs.columbia.edu.
cs.columbia.edu.	3600	IN	NS	apollo.cs.columbia.edu.
cs.columbia.edu.	3600	IN	NS	dns2.itd.umich.edu.
cs.columbia.edu.	3600	IN	NS	ext-ns1.columbia.edu.
;; Received 217 bytes from 128.32.136.14#53(128.32.136.14) in 102 ms

www.cs.columbia.edu.	60	IN	CNAME	webcluster.cs.columbia.edu.
webcluster.cs.columbia.edu. 60	IN	A	128.59.11.206
cs.columbia.edu.	60	IN	NS	diana.cs.columbia.edu.
cs.columbia.edu.	60	IN	NS	apollo.cs.columbia.edu.
cs.columbia.edu.	60	IN	NS	dns2.itd.umich.edu.
cs.columbia.edu.	60	IN	NS	ext-ns1.columbia.edu.
cs.columbia.edu.	60	IN	NS	sundog.ee.columbia.edu.
;; Received 242 bytes from 128.59.64.59#53(128.59.64.59) in 2 ms

b)
www.google.com
192.5.5.241
f.root-servers.net.
192.42.93.30
g.gtld-servers.net.
216.239.32.10
ns1.google.com.

; <<>> DiG 9.8.3-P1 <<>> +trace www.google.com
;; global options: +cmd
.			436991	IN	NS	e.root-servers.net.
.			436991	IN	NS	f.root-servers.net.
.			436991	IN	NS	m.root-servers.net.
.			436991	IN	NS	h.root-servers.net.
.			436991	IN	NS	a.root-servers.net.
.			436991	IN	NS	d.root-servers.net.
.			436991	IN	NS	l.root-servers.net.
.			436991	IN	NS	j.root-servers.net.
.			436991	IN	NS	k.root-servers.net.
.			436991	IN	NS	b.root-servers.net.
.			436991	IN	NS	i.root-servers.net.
.			436991	IN	NS	c.root-servers.net.
.			436991	IN	NS	g.root-servers.net.
;; Received 228 bytes from 128.59.1.3#53(128.59.1.3) in 52 ms

com.			172800	IN	NS	h.gtld-servers.net.
com.			172800	IN	NS	c.gtld-servers.net.
com.			172800	IN	NS	l.gtld-servers.net.
com.			172800	IN	NS	k.gtld-servers.net.
com.			172800	IN	NS	i.gtld-servers.net.
com.			172800	IN	NS	a.gtld-servers.net.
com.			172800	IN	NS	g.gtld-servers.net.
com.			172800	IN	NS	j.gtld-servers.net.
com.			172800	IN	NS	f.gtld-servers.net.
com.			172800	IN	NS	m.gtld-servers.net.
com.			172800	IN	NS	b.gtld-servers.net.
com.			172800	IN	NS	d.gtld-servers.net.
com.			172800	IN	NS	e.gtld-servers.net.
;; Received 504 bytes from 192.5.5.241#53(192.5.5.241) in 31 ms

google.com.		172800	IN	NS	ns2.google.com.
google.com.		172800	IN	NS	ns1.google.com.
google.com.		172800	IN	NS	ns3.google.com.
google.com.		172800	IN	NS	ns4.google.com.
;; Received 168 bytes from 192.42.93.30#53(192.42.93.30) in 78 ms

www.google.com.		300	IN	A	172.217.2.4
;; Received 48 bytes from 216.239.32.10#53(216.239.32.10) in 17 ms


www.google.co.in
193.0.14.129
k.root-servers.net.
199.249.125.1
b2.in.afilias-nst.org.
216.239.36.10
ns3.google.com.

; <<>> DiG 9.8.3-P1 <<>> +trace www.google.co.in
;; global options: +cmd
.			436831	IN	NS	a.root-servers.net.
.			436831	IN	NS	i.root-servers.net.
.			436831	IN	NS	j.root-servers.net.
.			436831	IN	NS	f.root-servers.net.
.			436831	IN	NS	k.root-servers.net.
.			436831	IN	NS	m.root-servers.net.
.			436831	IN	NS	c.root-servers.net.
.			436831	IN	NS	e.root-servers.net.
.			436831	IN	NS	b.root-servers.net.
.			436831	IN	NS	d.root-servers.net.
.			436831	IN	NS	h.root-servers.net.
.			436831	IN	NS	l.root-servers.net.
.			436831	IN	NS	g.root-servers.net.
;; Received 228 bytes from 128.59.1.3#53(128.59.1.3) in 43 ms

in.			172800	IN	NS	a0.in.afilias-nst.info.
in.			172800	IN	NS	a1.in.afilias-nst.in.
in.			172800	IN	NS	a2.in.afilias-nst.info.
in.			172800	IN	NS	b0.in.afilias-nst.org.
in.			172800	IN	NS	b1.in.afilias-nst.in.
in.			172800	IN	NS	b2.in.afilias-nst.org.
in.			172800	IN	NS	c0.in.afilias-nst.info.
;; Received 500 bytes from 193.0.14.129#53(193.0.14.129) in 110 ms

google.co.in.		86400	IN	NS	ns1.google.com.
google.co.in.		86400	IN	NS	ns2.google.com.
google.co.in.		86400	IN	NS	ns3.google.com.
;; Received 98 bytes from 199.249.125.1#53(199.249.125.1) in 11 ms

www.google.co.in.	300	IN	A	172.217.2.3
;; Received 50 bytes from 216.239.36.10#53(216.239.36.10) in 18 ms


wikipedia.org
192.5.5.241
f.root-servers.net.
199.19.54.1
b0.org.afilias-nst.org.
208.80.153.231
ns1.wikimedia.org.

; <<>> DiG 9.8.3-P1 <<>> +trace wikipedia.org
;; global options: +cmd
.			436671	IN	NS	c.root-servers.net.
.			436671	IN	NS	l.root-servers.net.
.			436671	IN	NS	e.root-servers.net.
.			436671	IN	NS	i.root-servers.net.
.			436671	IN	NS	j.root-servers.net.
.			436671	IN	NS	h.root-servers.net.
.			436671	IN	NS	m.root-servers.net.
.			436671	IN	NS	d.root-servers.net.
.			436671	IN	NS	f.root-servers.net.
.			436671	IN	NS	b.root-servers.net.
.			436671	IN	NS	k.root-servers.net.
.			436671	IN	NS	g.root-servers.net.
.			436671	IN	NS	a.root-servers.net.
;; Received 228 bytes from 128.59.1.3#53(128.59.1.3) in 40 ms

org.			172800	IN	NS	a2.org.afilias-nst.info.
org.			172800	IN	NS	a0.org.afilias-nst.info.
org.			172800	IN	NS	c0.org.afilias-nst.info.
org.			172800	IN	NS	b2.org.afilias-nst.org.
org.			172800	IN	NS	d0.org.afilias-nst.org.
org.			172800	IN	NS	b0.org.afilias-nst.org.
;; Received 433 bytes from 192.5.5.241#53(192.5.5.241) in 29 ms

wikipedia.org.		86400	IN	NS	ns1.wikimedia.org.
wikipedia.org.		86400	IN	NS	ns0.wikimedia.org.
wikipedia.org.		86400	IN	NS	ns2.wikimedia.org.
;; Received 143 bytes from 199.19.54.1#53(199.19.54.1) in 37 ms

wikipedia.org.		600	IN	A	208.80.154.224
;; Received 75 bytes from 208.80.153.231#53(208.80.153.231) in 46 ms

3.
book page 181
Peer 4 replace its first successor(peer 7) with its second successor(peer 14)
Peer 4 then asks its new first successor(peer 14) for the identifier and IP address
of its immediate successor(peer 20). Peer 4 then makes peer 20 its second successor.

4.
a)
With a NAK-only protocol, a lost packet will only be detected when a
subsequent packet is correctly received by the receiver which will then notice a
gap in the received sequence numbers. This means that with infrequent data
transmissions, a NAK based protocol can have a long error recovery time.
Hence, a NAK-only protocol would not be desirable in this case.

b)
On the other hand, if data is being sent often, then recovery under a NAK-only scheme
could happen quickly. Moreover, if errors are infrequent, then NAKs are only
occasionally sent when needed, and ACK are never sent – a significant reduction in
feedback in the NAK-only case over the ACK-only case.

c)
NAK is lost



5)
If the channel can arbitrarily duplicate package and package can appear at anytime.
Then the alternating bit protocol will not be able to achieve reliable data transfer.
After sender send package 0, it will wait for package ACK 0. Unfortunately, the ACK0
from last round may appear in the channel, and the sender will not be able to distinguish
them from each other, which will cause a problem. 
