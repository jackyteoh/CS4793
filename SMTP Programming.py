from socket import *
msg = "\r\n I love computer networks!"
endmsg = "\r\n. \r\n"
# Choose a mail server (e.g. Google mail server) and call it mailserver
mailserver = "smtp.nyu.edu"
portserver = 25
# Create socket called clientSocket and establish a TCP connection with mailserver
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((mailserver, portserver))
recv = clientSocket.recv(1024)
print(recv)
if recv[:3] != '220':
    print('220 reply not received from server.')

# Send HELO command nad print server response.
heloCommand = 'HELO Alice\r\n'
clientSocket.send(heloCommand)
recv1 = clientSocket.recv(1024)
print(recv1)
if recv1[:3] != '250':
    print('250 reply not received from server.')

# Send MAIL FROM command and print server response.
print("Sending the MAIL FROM command")
mailfromCommand = "MAIL FROM: jt2908@nyu.edu \r\n"
clientSocket.send(mailfromCommand)
recv2 = clientSocket.recv(1024)
print(recv2)

# Send RCPT TO command and print server response
print("Sending the RCPT TO command")
rcpttoCommand = "RCPT TO: jt2908@nyu.edu \r\n"
clientSocket.send(rcpttoCommand)
recv3 = clientSocket.recv(1024)
print(recv3)

# Send DATA command and print server response.
print("Sending DATA command")
dataCommand = "DATA\r\n"
clientSocket.send(dataCommand)
recv4 = clientSocket.recv(1024)
print(recv4)

# Send message data.
print("Sending the message")
clientSocket.send(msg)
# Message ends with a single period
clientSocket.send(endmsg)
recv4a = clientSocket.recv(1024)
print(recv4a)

# Send QUIT command and get server response
print("Sending QUIT command")
quitCommand = "QUIT\r\n"
clientSocket.send(quitCommand)
recv5 = clientSocket.recv(1024)
print(recv5)



