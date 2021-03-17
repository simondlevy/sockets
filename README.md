This repository contains Python code showing how you can combine three Python packages
([Sockets](https://docs.python.org/3/library/socket.html),
[Threads](https://docs.python.org/3/library/threading.html), and
[Binary data packing / unpacking](https://docs.python.org/3/library/struct.html))
to send data from a server to a client:

##  Quickstart

Open up a terminal (command) window and do:

```
  python3 server.py
```

Open up another terminal window and do:

```
  python3 client.py
```

In the client window you should see a stream of three floating-point values that change rapidly

##  Example use

Modifying this code for use your robot, internet-of-things, or remote-sensing project should be easy.
After cloning the repository on your server computer (e.g., RaspberryPi) and your client computer (e.g., laptop),
modify the ```ADDR``` value in
[header.py](https://github.com/simondlevy/sockets/blob/master/header.py#L9) on both computers to 
be the ID of the server.  To see how to make a RaspberryPi into a wireless server, take a look at
this [repository](https://github.com/simondlevy/RPiAdHocWiFi).


