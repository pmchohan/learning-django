import socket

mySock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySock.connect(('data.pr4e.org', 80))

cmd = 'GET http://data.pr4e.org/page1.htm HTTP/1.0\r\n\r\n'.encode()
mySock.send(cmd)

while True:
    data = mySock.recv(512)
    if len(data) < 1:
        break

    print(data.decode(), end='')

mySock.close()

# Output:
"""
HTTP/1.1 200 OK
Date: Sun, 29 Sep 2024 13:35:31 GMT
Server: Apache/2.4.52 (Ubuntu)
Last-Modified: Mon, 15 May 2017 11:11:47 GMT
ETag: "80-54f8e1f004857"
Accept-Ranges: bytes
Content-Length: 128
Cache-Control: max-age=0, no-cache, no-store, must-revalidate
Pragma: no-cache
Expires: Wed, 11 Jan 1984 05:00:00 GMT
Connection: close
Content-Type: text/html

<h1>The First Page</h1>
<p>
If you like, you can switch to the 
<a href="http://data.pr4e.org/page2.htm">
Second Page</a>.
</p>
"""