from socket import *
from doctorclienthandler import DoctorClientHandler
HOST = "localhost"
PORT = 5000
ADDRESS = (HOST, PORT)

server = socket(AF_INET, SOCK_STREAM)
server.bind(ADDRESS)
server.listen(5)

while True:
    print("Waiting for connection . . . ")
    client, address = server.accept()
    print("... connected from ", address)
    handler = DoctorClientHandler(client)
    handler.start()