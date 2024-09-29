# Introduction to Dynamic Web Content

## Web Applications & Request Response Cycle

### 1. Technologies in loading Web Page:
- Web Browser
- Web Server

Browser is lookin for events. When one happens, say a click our app (browser) it opens a socket across the network and sends a specially formatted request to the web server.

e.g `Get http://dash.web.com/file.htm`
and in response we get file.htm and browser understands it and displays it graphically
~~~
Extra: Port 80 for http and 443 for https by default is used.
~~~

### 2. Network Sockets/TCP Connection:

basically phone calls (software side) for computers. Connection is not always active, you connect get what you want and close the connection.

So we are not directly accessing the data there is a software in between our connection. that also checks if we are allowed to get that data

- TCP port numbers

a communication endpoint assigned to web app for communication
~~~
Extra:
port 25 for incoming email
port 23 for login
port 80 or 443 for web server
prot 109 or 110 for personal mail box
~~~

### 3. HTTP (HyperText Transfer Protocol):

A standard that browsers use to communicate with servers. there are others as well for other stuff.

- composition of URL (Uniform Resource Locator)


    | http://  | data.pr4e.org | /page1.htm|
    | ---: | :---: | :--- |
    | protocol | host | document |

~~~
Extra: Internet and Sockets were invented in 1970s and HTTP was invented in 1990
~~~

- making an http request

    client needs to say Hi first
    e.g `Get http://dash.web.com/file.htm HTTP/1.0` + headers or extra data

    the response will be somewhat like:
    ~~~
    HTTP/1.1 200 OK
    Date: ...
    Server: ...
    Last-Modified: ...
    Content-Type: text/html

    <h1>blah</h1>
    blah blah
    ~~~

### 4. Building a Simple Web Browser in Python:

code: [simple_browser.py](../codes/simple_browser.py)
~~~
Python string is Unicode, request to server should be UTF-8. So we use encode and decode in our code.
~~~

### 5. Building a Simple Web Server in Python:

code: [simple_server.py](../codes/simple_server.py)

in django when running locally (production) we can debug by checking which requests are being made.

### 6. Understanding Browser Developer Mode/Console:

- in Network tab you can see each request-response cycle
- in Inspect tab you can look at DOM (Document Object Model) (not necessarily the code from response)
