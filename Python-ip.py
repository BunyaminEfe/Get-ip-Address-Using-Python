##############################
#
# İnstagram: bejo_app
#
##############################
import socket 
hostname = socket.gethostname() 
IPAddress = socket.gethostbyname(hostname) 
print("Local Computer Name: " + hostname) 
print("Local Computer IP Address: " + IPAddress) 