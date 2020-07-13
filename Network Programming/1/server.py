import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(("127.0.0.1", 9999))
# binds the address that consists of the hostname and port to the socket
# we are passing a tuple as the parameter here

s.listen()
# waits for a message to the signal

print("Listening...")

while True:
    client, address = s.accept()
    # the accept method waits for a connection attemp to come and accepts it.
    # it then returns a client for responses and the address of the client that
    # is connected.

    print("Connected to {}".format(address))

    msg = "Hello Client!"

    client.send(message.encode('ascii'))
    # it is imp to encode the message first, because otherwise we can't send it
    # properly

    client.close()

