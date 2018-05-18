#import socket module
from socket import *
portNumber = 80
serverSocket = socket(AF_INET, SOCK_STREAM)
#Prepare a sever socket
#Fill in start
serverSocket.bind(("", portNumber))
serverSocket.listen(1)
#Fill in end
while True:
 #Establish the connection
 print ('Ready to serve...')
 connectionSocket, addr = serverSocket.accept()#Fill in start #Fill in end
 try:
     message = connectionSocket.recv(1024)#Fill in start #Fill in end
     filename = message.split()[1]
     f = open(filename[1:])
     outputdata = f.read()
 #Send one HTTP header line into socket
 #Fill in start
     connectionSocket.send("HTTP/1.1 200 OK\n ")
 #Fill in end
 #Send the content of the requested file to the client
     for i in range(0, len(outputdata)):
         connectionSocket.send(outputdata[i].encode())
     connectionSocket.close()
 except IOError:
 #Send response message for file not found
 #Fill in start
     connectionSocket.send("HTTP/1.1 404 Not Found\n ")
 #Fill in end
 #Close client socket
 #Fill in start
     connectionSocket.close()
 #Fill in end 
serverSocket.close() 
