                                                     ┌──(root㉿user)-[~]
└─# python3          
Python 3.12.7 (main, Nov  8 2024, 17:55:36) [GCC 14.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from scapy.all import *
>>> 
>>> # Function to handle the packets
>>> def packet_callback(packet):
...     if packet.haslayer(IP):  # Check if the packet has an IP layer
...         ip_src = packet[IP].src  # Source IP
...         ip_dst = packet[IP].dst  # Destination IP
...         protocol = packet[IP].proto  # Protocol (TCP/UDP)
...         
...         # Display relevant information
...         print(f"Packet: {packet.summary()}")
...         print(f"Source IP: {ip_src}")
...         print(f"Destination IP: {ip_dst}")
...         print(f"Protocol: {protocol}")
...         
...         # Optionally display payload data
...         if packet.haslayer(Raw):
...             payload = packet[Raw].load
...             print(f"Payload Data: {payload[:50]}...")  # Display first 50 bytes of payload
...         print("\n---\n")
... 
>>> # Start sniffing the network and capture packets
>>> print("Starting packet sniffer...")
Starting packet sniffer...
>>> sniff(prn=packet_callback, store=0)  # 'store=0' avoids saving the packets


Packet: Ether / IP / TCP 192.168.1.48:48030 > 104.18.32.47:https PA / Raw
Source IP: 192.168.1.48
Destination IP: 104.18.32.47
Protocol: 6
Payload Data: b'\x17\x03\x03\x00"\xe7\x9cx3\xc4\xf15}\x02C"\x96\r\x15-5\xf6\x14:!\xd05\xd5C\x0ff\xc0j&H\x02\xbc\x9b\xe3'...

---

Packet: Ether / IP / TCP 104.18.32.47:https > 192.168.1.48:48030 PA / Raw
Source IP: 104.18.32.47
Destination IP: 192.168.1.48
Protocol: 6
Payload Data: b'\x17\x03\x03\x00"5\x05\xcd9v\xee6\x85\xd9\x7f\x9dB\xae\xe8\xbf="\x0c\x05\xbb/\x9c\x01!=\xae\xe5\xa4,\xf1\xafx`F'...

---

Packet: Ether / IP / TCP 192.168.1.48:48030 > 104.18.32.47:https A
Source IP: 192.168.1.48
Destination IP: 104.18.32.47
Protocol: 6

---

Packet: Ether / 192.168.1.1 > 224.0.0.1 igmp / Raw / Padding
Source IP: 192.168.1.1
Destination IP: 224.0.0.1
Protocol: 2
Payload Data: b'\x11d\xec\x1e\x00\x00\x00\x00\x02}\x00\x00'...

---

Packet: Ether / IP / TCP 192.168.1.48:48030 > 104.18.32.47:https PA / Raw
Source IP: 192.168.1.48
Destination IP: 104.18.32.47
Protocol: 6
Payload Data: b'\x17\x03\x03\x00"\xe9\xd7\x8b\xcaX\x0f=}\x83\xa0\r\x0bY\xb7\xbf\xa4(%\xfa\x82n\xeaH>\x93\x92u\xe1\xbd$\x17\xe8E\xf3'...

---

Packet: Ether / IP / TCP 104.18.32.47:https > 192.168.1.48:48030 PA / Raw
Source IP: 104.18.32.47
Destination IP: 192.168.1.48
Protocol: 6
Payload Data: b'\x17\x03\x03\x00":\x8e52A\x84\xeb\xc2A\xf9/Zn\x87\xf5\x8e|\xc5s\xc6\x03\nkp\xdcI\xdcF\x04C\xef\x1eV\x90'...

---

Packet: Ether / IP / TCP 192.168.1.48:48030 > 104.18.32.47:https A
Source IP: 192.168.1.48
Destination IP: 104.18.32.47
Protocol: 6

---

Packet: Ether / IP / TCP 192.168.1.48:48030 > 104.18.32.47:https PA / Raw
Source IP: 192.168.1.48
Destination IP: 104.18.32.47
Protocol: 6
Payload Data: b'\x17\x03\x03\x00"k\xcc\xd3\xae\x98\x11\'\xc6\x04\x81"\xd2\xd1\x96gZ\xda\xaf\x07\xbe\x97\xb2\xaa\x98\xe7\xc2?e\x154\x17\t;h'...

---

Packet: Ether / IP / TCP 192.168.1.48:48030 > 104.18.32.47:https FPA / Raw
Source IP: 192.168.1.48
Destination IP: 104.18.32.47
Protocol: 6
Payload Data: b"\x17\x03\x03\x00\x13\x0c\xc7\x14b'\x87]\xce\xd8\x0c\xd3\x8f1F\x1c\x9eH\xc2g"...

---

Packet: Ether / IP / TCP 104.18.32.47:https > 192.168.1.48:48030 A
Source IP: 104.18.32.47
Destination IP: 192.168.1.48
Protocol: 6

---

Packet: Ether / IP / TCP 104.18.32.47:https > 192.168.1.48:48030 FA
Source IP: 104.18.32.47
Destination IP: 192.168.1.48
Protocol: 6

---

Packet: Ether / IP / TCP 192.168.1.48:48030 > 104.18.32.47:https A
Source IP: 192.168.1.48
Destination IP: 104.18.32.47
Protocol: 6

---

Packet: Ether / IP / UDP / DNS Qry b'spocs.getpocket.com.'
Source IP: 192.168.1.48
Destination IP: 192.168.1.1
Protocol: 17

---

Packet: Ether / IP / UDP / DNS Qry b'spocs.getpocket.com.'
Source IP: 192.168.1.48
Destination IP: 192.168.1.1
Protocol: 17

---

Packet: Ether / IP / UDP / DNS Ans b'prod.ads.prod.webservices.mozgcp.net.'
Source IP: 192.168.1.1
Destination IP: 192.168.1.48
Protocol: 17

---

Packet: Ether / IP / UDP / DNS Ans b'prod.ads.prod.webservices.mozgcp.net.'
Source IP: 192.168.1.1
Destination IP: 192.168.1.48
Protocol: 17

---

Packet: Ether / IP / UDP 192.168.1.48:43083 > 34.117.188.166:https / Raw
Source IP: 192.168.1.48
Destination IP: 34.117.188.166
Protocol: 17
Payload Data: b'\xc1\x00\x00\x00\x01\x08\x80\x95?!\xc6\x8eB\xf9\x03mA\x8e\x00B\x15w\xca\xfd(\xae\xaax\x00\xf9\xce\xcf\x16)\x99{\xf3\xe1\xec\xbe\x9d\xf4\xd3\xa4~\x80\xac8#\x03'...

---

Packet: Ether / IP / UDP 34.117.188.166:https > 192.168.1.48:43083 / Raw
Source IP: 34.117.188.166
Destination IP: 192.168.1.48
Protocol: 17
Payload Data: b'\xca\x00\x00\x00\x01\x03mA\x8e\x08\xe0\x95?!\xc6\x8eB\xf9\x00@u\x9cc\xf8\xc7\x1d\xfayZR\x99\x10\\\xf0\x13\x9a\x84(\x1c\xca\x9d\xd1\\&\xfe\xb1\xbd\xf3\x98\xad'...

---

Packet: Ether / IP / UDP 34.117.188.166:https > 192.168.1.48:43083 / Raw
Source IP: 34.117.188.166
Destination IP: 192.168.1.48
Protocol: 17
Payload Data: b"\xea\x00\x00\x00\x01\x03mA\x8e\x08\xe0\x95?!\xc6\x8eB\xf9E9\xa3\xd42\x82\x82\xb6\xe8f,\x0c\x9d\x980\xef\xf9:\x08d\tQ\xcd\xcb\x84\xb8ea\xcd'\xf2\xbb"...

---

Packet: Ether / IP / UDP 34.117.188.166:https > 192.168.1.48:43083 / Raw
Source IP: 34.117.188.166
Destination IP: 192.168.1.48
Protocol: 17
Payload Data: b'\xe6\x00\x00\x00\x01\x03mA\x8e\x08\xe0\x95?!\xc6\x8eB\xf9E9\xb3$]&p\xab/g\r\xe8\x94\x07s\x94J 8B\xca\x921\xb4\xb0\xd3o\xf23\xb6\xd6+'...

---

Packet: Ether / IP / UDP 192.168.1.48:43083 > 34.117.188.166:https / Raw
Source IP: 192.168.1.48
Destination IP: 34.117.188.166
Protocol: 17
Payload Data: b'\xec\x00\x00\x00\x01\x08\xe0\x95?!\xc6\x8eB\xf9\x03mA\x8e@\x16\x04Qs\xaf\x01\xe3\xe2\xfa6\xdf\xbcC\xb9G\x85\xa1\xc8\xb9c\x1b\x0c\r'...

---

Packet: Ether / IP / UDP 34.117.188.166:https > 192.168.1.48:43083 / Raw
Source IP: 34.117.188.166
Destination IP: 192.168.1.48
Protocol: 17
Payload Data: b'\xe9\x00\x00\x00\x01\x03mA\x8e\x08\xe0\x95?!\xc6\x8eB\xf9B\xc5,TTr{\xc0\xd3/\xb0\x875w>x\xec\x81\xbfj\x1c\xf6>\xb4\xa7\xe69\xa3q\xe3\x82-'...

---

Packet: Ether / IP / UDP 192.168.1.48:43083 > 34.117.188.166:https / Raw
Source IP: 192.168.1.48
Destination IP: 34.117.188.166
Protocol: 17
Payload Data: b'\xe3\x00\x00\x00\x01\x08\xe0\x95?!\xc6\x8eB\xf9\x03mA\x8e@\x17\xaa`H\x8f]\x1a]\xfb\xa9\xe1p\x9aO&\xb2,/\xe4\xf8b\xdcZ\xc0'...

---

Packet: Ether / IP / UDP / DNS Qry b'o.pki.goog.'
Source IP: 192.168.1.48
Destination IP: 192.168.1.1
Protocol: 17

---

Packet: Ether / IP / UDP / DNS Qry b'o.pki.goog.'
Source IP: 192.168.1.48
Destination IP: 192.168.1.1
Protocol: 17

---

Packet: Ether / IP / UDP / DNS Ans b'pki-goog.l.google.com.'
Source IP: 192.168.1.1
Destination IP: 192.168.1.48
Protocol: 17

---

Packet: Ether / IP / UDP / DNS Ans b'pki-goog.l.google.com.'
Source IP: 192.168.1.1
Destination IP: 192.168.1.48
Protocol: 17

---

Packet: Ether / IP / TCP 192.168.1.48:34436 > 142.251.111.94:http S
Source IP: 192.168.1.48
Destination IP: 142.251.111.94
Protocol: 6

---

Packet: Ether / IP / TCP 142.251.111.94:http > 192.168.1.48:34436 SA
Source IP: 142.251.111.94
Destination IP: 192.168.1.48
Protocol: 6

---

Packet: Ether / IP / TCP 192.168.1.48:34436 > 142.251.111.94:http A
Source IP: 192.168.1.48
Destination IP: 142.251.111.94
Protocol: 6

---

Packet: Ether / IP / TCP 192.168.1.48:34436 > 142.251.111.94:http PA / Raw
Source IP: 192.168.1.48
Destination IP: 142.251.111.94
Protocol: 6
Payload Data: b'POST /s/wr3/yvU HTTP/1.1\r\nHost: o.pki.goog\r\nUser-A'...

---

Packet: Ether / IP / TCP 142.251.111.94:http > 192.168.1.48:34436 A
Source IP: 142.251.111.94
Destination IP: 192.168.1.48
Protocol: 6

---

Packet: Ether / IP / UDP 192.168.1.48:43083 > 34.117.188.166:https / Raw
Source IP: 192.168.1.48
Destination IP: 34.117.188.166
Protocol: 17
Payload Data: b'\xe8\x00\x00\x00\x01\x08\xe0\x95?!\xc6\x8eB\xf9\x03mA\x8e@\x14b\xa8\n\xab \xf1)\xccY\t\x1d\x19\xb8\x8c\xc1\xaf\x0f\xa3\x13\xb9'...

---

Packet: Ether / IP / UDP 192.168.1.48:43083 > 34.117.188.166:https / Raw
Source IP: 192.168.1.48
Destination IP: 34.117.188.166
Protocol: 17
Payload Data: b'\xe3\x00\x00\x00\x01\x08\xe0\x95?!\xc6\x8eB\xf9\x03mA\x8e@\x14\xf0\x9e\xa5&\xed\x07iUd\x1ch7[K\xec9N\x91\xcb\xba'...

---

Packet: Ether / IP / UDP 34.117.188.166:https > 192.168.1.48:43083 / Raw
Source IP: 34.117.188.166
Destination IP: 192.168.1.48
Protocol: 17
Payload Data: b'\xe1\x00\x00\x00\x01\x03mA\x8e\x08\xe0\x95?!\xc6\x8eB\xf9@\x16\xdb\x19\xa1\xb1Z\x1a\xb7`\xfezL\xc2&\xb8Q\xa7\xf3j\xc1\xf1\xbc\x11'...

---

Packet: Ether / IP / TCP 192.168.1.48:49850 > 34.117.188.166:https S
Source IP: 192.168.1.48
Destination IP: 34.117.188.166
Protocol: 6

---

Packet: Ether / IP / TCP 142.251.111.94:http > 192.168.1.48:34436 PA / Raw
Source IP: 142.251.111.94
Destination IP: 192.168.1.48
Protocol: 6
Payload Data: b'HTTP/1.1 200 OK\r\nContent-Type: application/ocsp-re'...

---

Packet: Ether / IP / TCP 192.168.1.48:34436 > 142.251.111.94:http A
Source IP: 192.168.1.48
Destination IP: 142.251.111.94
Protocol: 6

---

Packet: Ether / IP / UDP 192.168.1.48:43083 > 34.117.188.166:https / Raw
Source IP: 192.168.1.48
Destination IP: 34.117.188.166
Protocol: 17
Payload Data: b'\xe1\x00\x00\x00\x01\x08\xe0\x95?!\xc6\x8eB\xf9\x03mA\x8e@8a\xf2\x93D\xdcJ\xdc\xce\xa0F}\xa1N\xa8\\>\xdc\xb0\x93q\x1dCI\xc9(OD|\xaa\xe6'...

---

Packet: Ether / IP / UDP 192.168.1.48:43083 > 34.117.188.166:https / Raw
Source IP: 192.168.1.48
Destination IP: 34.117.188.166
Protocol: 17
Payload Data: b'S\xe0\x95?!\xc6\x8eB\xf9|s\x12\xf3ad\xbfO/\x91\x03{\x87E\x93\\,\x8c=\xdc_\x85J\x05\x84L%\xadU\x1eT\xcd[\x1c\xf2\xe1\xf4\x1d\x11\xb6\x01'...

---

Packet: Ether / IP / UDP 192.168.1.48:43083 > 34.117.188.166:https / Raw
Source IP: 192.168.1.48
Destination IP: 34.117.188.166
Protocol: 17
Payload Data: b'S\xe0\x95?!\xc6\x8eB\xf9\x16\xc3qt.%\x8b\xcdt#\x90\xdc\xd9\x0c\x85|\xd2c\xfb\xe60gN\x1a\xa4\xc0\x057\\5\xff\x9dbh\x03t\x8e_W\xb0\xfe'...

---

Packet: Ether / IP / TCP 34.117.188.166:https > 192.168.1.48:49850 SA
Source IP: 34.117.188.166
Destination IP: 192.168.1.48
Protocol: 6

---

Packet: Ether / IP / TCP 192.168.1.48:49850 > 34.117.188.166:https A
Source IP: 192.168.1.48
Destination IP: 34.117.188.166
Protocol: 6

---

Packet: Ether / IP / TCP 192.168.1.48:49850 > 34.117.188.166:https PA / Raw
Source IP: 192.168.1.48
Destination IP: 34.117.188.166
Protocol: 6
Payload Data: b'\x16\x03\x01\x02\x00\x01\x00\x01\xfc\x03\x03\xae\xa8\xd8\xe2\xe8\xc1\t?\xc7\xa9Hb\x90-}\x84f>0\xf9<H{\xa4\xc8\x13B\x8f\xeev_\xba \x08\xb0\x88jR\x13'...

---

Packet: Ether / IP / UDP 34.117.188.166:https > 192.168.1.48:43083 / Raw
Source IP: 34.117.188.166
Destination IP: 192.168.1.48
Protocol: 17
Payload Data: b'\\mA\x8e\xa2\xdef\x82)\x0f\xb8\x96\x98\xd5\xd0"\x8b|<4\'O\xb4\x88\xa3\x17\xaf\xefe\xc2\xe7\xbb\x11\xf3\xb3!8\xdb\x99\xc1*\xab\xdfO\x0f)\xd5V\xf2\xe9'...

---

Packet: Ether / IP / UDP 34.117.188.166:https > 192.168.1.48:43083 / Raw
Source IP: 34.117.188.166
Destination IP: 192.168.1.48
Protocol: 17
Payload Data: b']mA\x8ec\xd1\xab\xc9(\x91\x95\xb9\xb4\x1e@\xd0r\xc5\xb9\xcd]v\xf2\xaa\xc4\xe2\x8cf@.*\xdd1\xdc\xdd\xf0\xbb\xc5%\x81\xb8i\x84\xae\xd9\x02U\x0c\x12\xf0'...

---

Packet: Ether / IP / UDP 192.168.1.48:43083 > 34.117.188.166:https / Raw
Source IP: 192.168.1.48
Destination IP: 34.117.188.166
Protocol: 17
Payload Data: b'G\xe0\x95?!\xc6\x8eB\xf9\x835T\xe6\xe9\xfe\xae\xf9#\x10]rBa\xa0\x17P\xbe\xec\xe2V\xe0y\xa3'...

---

Packet: Ether / IP / UDP 34.117.188.166:https > 192.168.1.48:43083 / Raw
Source IP: 34.117.188.166
Destination IP: 192.168.1.48
Protocol: 17
Payload Data: b'SmA\x8e\x0e\xe9\x9f\x12f\x95jA\xfc\xc6\xd2GgP\xed\xe0\xc8i\x92\nU\x03\x1e\x0fU*'...

---

Packet: Ether / IP / TCP 34.117.188.166:https > 192.168.1.48:49850 A
Source IP: 34.117.188.166
Destination IP: 192.168.1.48
Protocol: 6

---

Packet: Ether / IP / TCP 34.117.188.166:https > 192.168.1.48:49850 PA / Raw
Source IP: 34.117.188.166
Destination IP: 192.168.1.48
Protocol: 6
Payload Data: b"\x16\x03\x03\x00z\x02\x00\x00v\x03\x03\t\x10#\xf9mE\x0f\x8a3N\x06\xc5\x15D\x87':D\xf3\\\x95@&\xb4\xce\xf1;\x80\x94\xc32T \x08\xb0\x88jR\x13"...

---

Packet: Ether / IP / TCP 34.117.188.166:https > 192.168.1.48:49850 PA / Raw
Source IP: 34.117.188.166
Destination IP: 192.168.1.48
Protocol: 6
Payload Data: b'\x03\xb0\xdc\xbf\xdf2?\xb9"a,\x0e<\x07\xde\xa0+\xa6\x1e\x8f+\x91\xf5-/\x8e\xc3\x87\x84\x96\xc7\x82\xd9@{\xf9n@J^\x92\xf1\x15\x14\nn\xc6\xad\'V'...

---

Packet: Ether / IP / TCP 34.117.188.166:https > 192.168.1.48:49850 PA / Raw
Source IP: 34.117.188.166
Destination IP: 192.168.1.48
Protocol: 6
Payload Data: b'kc\x04\xa5\xe5<Y\xf5\xf2\x97.\x18\xdc\xc3\x89\xbf\xda(1\x1a\x0b/?\xd9Sx\xf5a_\xd7=\x7f\x8a\xbfL!J\xd5\xbcA\x0fu\xaa\xdc2\x10\xa1!\xc4['...

---

Packet: Ether / IP / TCP 192.168.1.48:49850 > 34.117.188.166:https A
Source IP: 192.168.1.48
Destination IP: 34.117.188.166
Protocol: 6

---

Packet: Ether / IP / TCP 192.168.1.48:49850 > 34.117.188.166:https A
Source IP: 192.168.1.48
Destination IP: 34.117.188.166
Protocol: 6

---

Packet: Ether / IP / TCP 192.168.1.48:49850 > 34.117.188.166:https A
Source IP: 192.168.1.48
Destination IP: 34.117.188.166
Protocol: 6

---

Packet: Ether / IP / TCP 192.168.1.48:49850 > 34.117.188.166:https PA / Raw
Source IP: 192.168.1.48
Destination IP: 34.117.188.166
Protocol: 6
Payload Data: b'\x14\x03\x03\x00\x01\x01\x17\x03\x03\x005}\xfc\xd5\x83>\x17V\xd5\xd0\xe4\xbf\xfeH\xad\xf4V\x11R\xec\xd7\xf8\xaahNDX\xf3\xd7\x99\xaa\xc5&\xda\x98+\x19\x9a\xc8]'...

---

Packet: Ether / IP / TCP 192.168.1.48:49850 > 34.117.188.166:https PA / Raw
Source IP: 192.168.1.48
Destination IP: 34.117.188.166
Protocol: 6
Payload Data: b'\x17\x03\x03\x00\xa5k\x80,\x13\x0c\xd4\xc2R\x80ou\xb0\x9c\xd5\x07ko\xad\xa1\x1fv\xa7\x00\xd9\x89\xf1\xe1Vv\xc5e\x9bvn\x9d\xf1JHO\t\x91\x17\x84LL'...

---

Packet: Ether / IP / UDP 192.168.1.48:43083 > 34.117.188.166:https / Raw
Source IP: 192.168.1.48
Destination IP: 34.117.188.166
Protocol: 17
Payload Data: b'S\xe0\x95?!\xc6\x8eB\xf9\xe5\xa5\xc4\xef\xc97\x19\xe8t\x02+\x08\x0e\xe5r\xa7g,\x82R\xbe\x1dj'...

---

Packet: Ether / IP / TCP 34.117.188.166:https > 192.168.1.48:49850 PA / Raw
Source IP: 34.117.188.166
Destination IP: 192.168.1.48
Protocol: 6
Payload Data: b"\x17\x03\x03\x02'YqX\x04\xa1\xeb:\xae:\xaf\x90%)\x82\xe2\xf7\xec\xdfz\x08\xb8\x11o\xfd\x8b\x19\xa6\x85\xbb\xabGx\xda\x8aF>\xc3\xbb#\x1b-_\xb0\x15\xc4"...

---

Packet: Ether / IP / TCP 34.117.188.166:https > 192.168.1.48:49850 PA / Raw
Source IP: 34.117.188.166
Destination IP: 192.168.1.48
Protocol: 6
Payload Data: b'\x17\x03\x03\x00\x1aq\xd3\x11\xc0u+\xa6mSq\x0b\xe3\xa6\x05\x92\x9b(K#x\x83\x01 \x1b\x05\xd6'...

---

Packet: Ether / IP / TCP 192.168.1.48:49850 > 34.117.188.166:https PA / Raw
Source IP: 192.168.1.48
Destination IP: 34.117.188.166
Protocol: 6
Payload Data: b'\x17\x03\x03\x00\x1aC6\xbc\xc8\x87\xfa\x11*\xe7a\xe4\x97\x06\xd3T\xc8a!\xe4\x83I\xca\xb91\xcf\x0b'...

---

Packet: Ether / IP / TCP 34.117.188.166:https > 192.168.1.48:49850 A
Source IP: 34.117.188.166
Destination IP: 192.168.1.48
Protocol: 6

---

Packet: Ether / IP / UDP 34.117.188.166:https > 192.168.1.48:43083 / Raw
Source IP: 34.117.188.166
Destination IP: 192.168.1.48
Protocol: 17
Payload Data: b'TmA\x8e}`\xc2/_E\x9fw\xe1\x9d\x98\xfcW\x8e\x0b`\x0e\xe5*\xc5\x7f\x99\xc4\x1cY\xa2\x8deV\x00\xb5w\xf2\xd0Y\xc2\xbezR\x10\xd1L\x0c\xc0\xf5\xf5'...

---

Packet: Ether / IP / UDP 34.117.188.166:https > 192.168.1.48:43083 / Raw
Source IP: 34.117.188.166
Destination IP: 192.168.1.48
Protocol: 17
Payload Data: b'EmA\x8eak\xdal\x18\xf3\xb1k\x1b\xca\xfc\xb7F\xa6\x8f+\xbf\x07\x19\xf1\x92\xd3a\x96#\xca\xc6\xbc\x04\x96(\xd3\xec)\xe9P\x90\xc3~<\x045\x1b\xeavC'...

---

Packet: Ether / IP / UDP 34.117.188.166:https > 192.168.1.48:43083 / Raw
Source IP: 34.117.188.166
Destination IP: 192.168.1.48
Protocol: 17
Payload Data: b"JmA\x8es\xa4T\x7fW'I\x80\xe1\xf0\x8b\x96yH\x8a1\xe8+pq\x1a\xfdj\n\x87\xe3\x02\xd8qK\xc8\x1c1c\x86\xb9;\xca\xb1-\xed\x9c\xdeJ&\xfc"...

---

Packet: Ether / IP / UDP 34.117.188.166:https > 192.168.1.48:43083 / Raw
Source IP: 34.117.188.166
Destination IP: 192.168.1.48
Protocol: 17
Payload Data: b'HmA\x8eJ(\xb0_\xf8\xd1\xe9\xe7F\x1a\x1c=\x94\x8ddL/dz\xb6\xd8\xf3\x95\xb6\x01\xb6\x06?_\x19h\xef\x12\x84s*\x955Fj\x0b\xa4\x13>h%'...

---

Packet: Ether / IP / UDP 192.168.1.48:43083 > 34.117.188.166:https / Raw
Source IP: 192.168.1.48
Destination IP: 34.117.188.166
Protocol: 17
Payload Data: b'Z\xe0\x95?!\xc6\x8eB\xf9\x16\xd9<\x04\xcb\xdc\xf0\x9c\xcd\x17aT\xe1\t\xd4\x1bQ>\x90\xb8T\xe9(H\xc0Z\xf7\x9aK'...

---

Packet: Ether / IP / UDP 34.117.188.166:https > 192.168.1.48:43083 / Raw
Source IP: 34.117.188.166
Destination IP: 192.168.1.48
Protocol: 17
Payload Data: b'^mA\x8eW\xb1\xa2NK\xf3b\xb1W\xd8\xf7o\xf06\x1cT\n\x07Mk\xbb\x99@'...

---

Packet: Ether / IP / TCP 34.107.243.93:https > 192.168.1.48:54860 PA / Raw
Source IP: 34.107.243.93
Destination IP: 192.168.1.48
Protocol: 6
Payload Data: b'\x17\x03\x03\x00\x13D\xc6\x1fp\xec\x0c\xe3\x94\xd3\xc7\xf6\xba\xccY\x86\xafV!\x8f'...

---

Packet: Ether / IP / TCP 192.168.1.48:54860 > 34.107.243.93:https PA / Raw
Source IP: 192.168.1.48
Destination IP: 34.107.243.93
Protocol: 6
Payload Data: b'\x17\x03\x03\x00\x17dC\xda\xe7\xfe\x1f-t\xb0]\x95\xc2\xdb\xe4\x8a)\xef\xc2\xd8[Z\x9c\x01'...

---

Packet: Ether / IP / TCP 34.107.243.93:https > 192.168.1.48:54860 A
Source IP: 34.107.243.93
Destination IP: 192.168.1.48
Protocol: 6

---

Packet: Ether / 192.168.1.1 > 224.0.0.1 igmp / Raw / Padding
Source IP: 192.168.1.1
Destination IP: 224.0.0.1
Protocol: 2
Payload Data: b'\x11d\xec\x1e\x00\x00\x00\x00\x02}\x00\x00'...

---

Packet: Ether / IP / TCP 192.168.1.48:34436 > 142.251.111.94:http A
Source IP: 192.168.1.48
Destination IP: 142.251.111.94
Protocol: 6

---

Packet: Ether / IP / TCP 142.251.111.94:http > 192.168.1.48:34436 A
Source IP: 142.251.111.94
Destination IP: 192.168.1.48
Protocol: 6

---

Packet: Ether / IP / TCP 192.168.1.48:34436 > 142.251.111.94:http A
Source IP: 192.168.1.48
Destination IP: 142.251.111.94
Protocol: 6

---

Packet: Ether / IP / TCP 142.251.111.94:http > 192.168.1.48:34436 A
Source IP: 142.251.111.94
Destination IP: 192.168.1.48
Protocol: 6

---

Packet: Ether / IP / TCP 192.168.1.48:34436 > 142.251.111.94:http A
Source IP: 192.168.1.48
Destination IP: 142.251.111.94
Protocol: 6

---

Packet: Ether / IP / TCP 142.251.111.94:http > 192.168.1.48:34436 A
Source IP: 142.251.111.94
Destination IP: 192.168.1.48
Protocol: 6

---

Packet: Ether / IP / TCP 192.168.1.48:34436 > 142.251.111.94:http A
Source IP: 192.168.1.48
Destination IP: 142.251.111.94
Protocol: 6

---

Packet: Ether / IP / TCP 142.251.111.94:http > 192.168.1.48:34436 A
Source IP: 142.251.111.94
Destination IP: 192.168.1.48
Protocol: 6

---

Packet: Ether / IP / TCP 192.168.1.48:34436 > 142.251.111.94:http A
Source IP: 192.168.1.48
Destination IP: 142.251.111.94
Protocol: 6

---

Packet: Ether / IP / TCP 142.251.111.94:http > 192.168.1.48:34436 A
Source IP: 142.251.111.94
Destination IP: 192.168.1.48
Protocol: 6

---

Packet: Ether / IP / TCP 192.168.1.48:49850 > 34.117.188.166:https PA / Raw
Source IP: 192.168.1.48
Destination IP: 34.117.188.166
Protocol: 6
Payload Data: b'\x17\x03\x03\x00"\xdbf\x95t~\n\xafY4\x8d\xc1\xf8Y\x04~\xec}\x1apd*\xed\xa5\xe0\xd1F\xbd\xbe\xa4\xfb\xf5\x94\xe4_'...

---

Packet: Ether / IP / TCP 34.117.188.166:https > 192.168.1.48:49850 A
Source IP: 34.117.188.166
Destination IP: 192.168.1.48
Protocol: 6

---

Packet: Ether / IP / TCP 34.117.188.166:https > 192.168.1.48:49850 PA / Raw
Source IP: 34.117.188.166
Destination IP: 192.168.1.48
Protocol: 6
Payload Data: b'\x17\x03\x03\x00"\xb6l\xb8\xaaV>U\x7f|\x15\x8d\xd2\xbb\xe0\xb0 \xb5\x1cE\x0c\xab\xd2ZH\xfe\xfc\xfb\xd8\xa7\xa84v\n\x04'...

---

Packet: Ether / IP / TCP 192.168.1.48:49850 > 34.117.188.166:https A
Source IP: 192.168.1.48
Destination IP: 34.117.188.166
Protocol: 6

---

Packet: Ether / IP / TCP 192.168.1.48:34436 > 142.251.111.94:http A
Source IP: 192.168.1.48
Destination IP: 142.251.111.94
Protocol: 6

---

Packet: Ether / IP / TCP 142.251.111.94:http > 192.168.1.48:34436 A
Source IP: 142.251.111.94
Destination IP: 192.168.1.48
Protocol: 6

---

Packet: Ether / IP / TCP 192.168.1.48:34436 > 142.251.111.94:http A
Source IP: 192.168.1.48
Destination IP: 142.251.111.94
Protocol: 6

---

Packet: Ether / IP / TCP 142.251.111.94:http > 192.168.1.48:34436 A
Source IP: 142.251.111.94
Destination IP: 192.168.1.48
Protocol: 6

---

Packet: Ether / IP / UDP / BOOTP / DHCP Discover
Source IP: 0.0.0.0
Destination IP: 255.255.255.255
Protocol: 17

---

Packet: Ether / IP / UDP / BOOTP / DHCP Offer
Source IP: 192.168.1.1
Destination IP: 255.255.255.255
Protocol: 17

---

Packet: Ether / IP / TCP 192.168.1.48:34436 > 142.251.111.94:http A
Source IP: 192.168.1.48
Destination IP: 142.251.111.94
Protocol: 6

---

Packet: Ether / IP / TCP 142.251.111.94:http > 192.168.1.48:34436 A
Source IP: 142.251.111.94
Destination IP: 192.168.1.48
Protocol: 6

---

Packet: Ether / IP / UDP / BOOTP / DHCP Discover
Source IP: 0.0.0.0
Destination IP: 255.255.255.255
Protocol: 17

---

Packet: Ether / IP / UDP / BOOTP / DHCP Offer
Source IP: 192.168.1.1
Destination IP: 255.255.255.255
Protocol: 17

---

Packet: Ether / IP / TCP 192.168.1.48:34436 > 142.251.111.94:http A
Source IP: 192.168.1.48
Destination IP: 142.251.111.94
Protocol: 6

---

Packet: Ether / IP / TCP 142.251.111.94:http > 192.168.1.48:34436 A
Source IP: 142.251.111.94
Destination IP: 192.168.1.48
Protocol: 6

---

Packet: Ether / IP / TCP 192.168.1.48:34436 > 142.251.111.94:http A
Source IP: 192.168.1.48
Destination IP: 142.251.111.94
Protocol: 6

---

Packet: Ether / IP / TCP 142.251.111.94:http > 192.168.1.48:34436 A
Source IP: 142.251.111.94
Destination IP: 192.168.1.48
Protocol: 6

---

Packet: Ether / IP / TCP 192.168.1.48:34436 > 142.251.111.94:http A
Source IP: 192.168.1.48
Destination IP: 142.251.111.94
Protocol: 6

---

Packet: Ether / IP / TCP 142.251.111.94:http > 192.168.1.48:34436 A
Source IP: 142.251.111.94
Destination IP: 192.168.1.48
Protocol: 6

---

Packet: Ether / IP / TCP 192.168.1.48:34436 > 142.251.111.94:http FA
Source IP: 192.168.1.48
Destination IP: 142.251.111.94
Protocol: 6

---

Packet: Ether / IP / TCP 142.251.111.94:http > 192.168.1.48:34436 FA
Source IP: 142.251.111.94
Destination IP: 192.168.1.48
Protocol: 6

---

Packet: Ether / IP / TCP 192.168.1.48:34436 > 142.251.111.94:http A
Source IP: 192.168.1.48
Destination IP: 142.251.111.94
Protocol: 6

---

Packet: Ether / IP / TCP 192.168.1.48:49850 > 34.117.188.166:https PA / Raw
Source IP: 192.168.1.48
Destination IP: 34.117.188.166
Protocol: 6
Payload Data: b'\x17\x03\x03\x00"\t,}\x8c\x04\xa5f\x91\x8b\x8cY\xc3F\xac8W^W^\xb9\xee,ji\xac\x91\xfd\xd4\xd6\xe5\x85\xf4\xf8n'...

---

Packet: Ether / IP / TCP 34.117.188.166:https > 192.168.1.48:49850 PA / Raw
Source IP: 34.117.188.166
Destination IP: 192.168.1.48
Protocol: 6
Payload Data: b'\x17\x03\x03\x00"t\xc8Lm\x04\xecQ\x9e\x8b\xb5\x00\xedj\x0bk\x00\xd2\x00\xd8\'\x9f\xba\xdd\xd7\x18\x9b8E\x84\xcb1\x91\x16\x14'...

---

Packet: Ether / IP / TCP 192.168.1.48:49850 > 34.117.188.166:https A
Source IP: 192.168.1.48
Destination IP: 34.117.188.166
Protocol: 6

---

Packet: Ether / IP / UDP / BOOTP / DHCP Discover
Source IP: 0.0.0.0
Destination IP: 255.255.255.255
Protocol: 17

---

Packet: Ether / IP / UDP / BOOTP / DHCP Offer
Source IP: 192.168.1.1
Destination IP: 255.255.255.255
Protocol: 17

---

Packet: Ether / IP / UDP / BOOTP / DHCP Discover
Source IP: 0.0.0.0
Destination IP: 255.255.255.255
Protocol: 17

---

Packet: Ether / IP / UDP / BOOTP / DHCP Offer
Source IP: 192.168.1.1
Destination IP: 255.255.255.255
Protocol: 17

---

Packet: Ether / 192.168.1.1 > 224.0.0.1 igmp / Raw / Padding
Source IP: 192.168.1.1
Destination IP: 224.0.0.1
Protocol: 2
Payload Data: b'\x11d\xec\x1e\x00\x00\x00\x00\x02}\x00\x00'...

---

Packet: Ether / IP / UDP / BOOTP / DHCP Discover
Source IP: 0.0.0.0
Destination IP: 255.255.255.255
Protocol: 17

---

Packet: Ether / IP / UDP / BOOTP / DHCP Offer
Source IP: 192.168.1.1
Destination IP: 255.255.255.255
Protocol: 17

---

Packet: Ether / IP / TCP 192.168.1.48:49850 > 34.117.188.166:https PA / Raw
Source IP: 192.168.1.48
Destination IP: 34.117.188.166
Protocol: 6
Payload Data: b'\x17\x03\x03\x00"\xe2\xa8:{\x109h\xc9=.%o\x99G\x8e\xadsc\xd5\x9b\xeb\x08\x03M\xeb\xd4\x9b\xac\xeb\xd2\x94\xa3\xa4\xd3'...

---

Packet: Ether / IP / TCP 192.168.1.48:49850 > 34.117.188.166:https FPA / Raw
Source IP: 192.168.1.48
Destination IP: 34.117.188.166
Protocol: 6
Payload Data: b'\x17\x03\x03\x00\x13e\xe2\x00e\x0e\xf4\xc92\xa9\xfbth\xec\xe8\xd6\xcd\x05\xb5{'...

---

Packet: Ether / IP / TCP 34.117.188.166:https > 192.168.1.48:49850 A
Source IP: 34.117.188.166
Destination IP: 192.168.1.48
Protocol: 6

---

Packet: Ether / IP / TCP 34.117.188.166:https > 192.168.1.48:49850 FA
Source IP: 34.117.188.166
Destination IP: 192.168.1.48
Protocol: 6

---

Packet: Ether / IP / TCP 192.168.1.48:49850 > 34.117.188.166:https A
Source IP: 192.168.1.48
Destination IP: 34.117.188.166
Protocol: 6

---

Packet: Ether / 192.168.1.1 > 224.0.0.1 igmp / Raw / Padding
Source IP: 192.168.1.1
Destination IP: 224.0.0.1
Protocol: 2
Payload Data: b'\x11d\xec\x1e\x00\x00\x00\x00\x02}\x00\x00'...

---

^C<Sniffed: TCP:0 UDP:0 ICMP:0 Other:0>
>>> 
