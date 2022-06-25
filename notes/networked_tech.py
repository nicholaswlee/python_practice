### Talking on the internet
### Port 80 is the web port/server (HTTP)
### TCP sockets
import socket
### This is like "dialing the phone", this makes a socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
### Connects the socket to the domain name. This function
### takes a tuple, 2nd arg the the port number
mysock.connect(('data.pr4e.org', 80))
### .encode() turns unicode to UTF
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
### This sends the command to the server
mysock.send(cmd)
### Receives data from server until reaches end
while True:
    data = mysock.recv(512)
    if(len(data) < 1):
        break
    print(data.decode())
mysock.close()

### Trying to extract baseball data
baseball_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
baseball_sock.connect(('www.espn.com', 80))
cmd = 'GET https://www.espn.com/mlb/scoreboard HTTP/1.0\r\n\r\n'.encode()
### This sends the command to the server
baseball_sock.send(cmd)

while True:
    ### Up to 512 characters received at a time
    data = baseball_sock.recv(512)
    if(len(data) < 1):
        break
    ### UTF-8 to unicode
    print(data.decode())
baseball_sock.close()
### Using Hypertext Transfer Protocol
### Used to receive web pages, allows browsers
### to receive documents from the web.
### http://www.something/page
### protocol host           document
### Request response cycle is when user requests
### something from webserver and then uses it

### Use ord() to find number associated with char
print(ord('\n'))

### UNICODE allows characters to be able to establish a system
### abstraction of all possible characters
### UFT-8 -> 1-4 bytes, variable length
### In python, everything is unicode
### In python3 -> byte string is b'abc'
### string -> this is type string: u'我叫李文瑞'
### We use decode() to decode. Assumes UTF-8
### will turn it into a string