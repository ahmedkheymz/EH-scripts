
# created this program By AhmedAS



import socket

# Simple function that can scan Service banner.. 
def banner (ip, port):
    
  con = socket.socket() 
  con.connect((ip,int(port)))
  con.settimeout(3.4)
  print(str(con.recv(1024))) 




def main():
 try:
    ip = input("Please enter the IP: ")
    port = input("Please enter the Port: ")
    banner(ip,port)
    
 except TimeoutError:
     print(" Sorry can't reach "+ip)
if __name__ == '__main__':
    
 try:
     main()
 except KeyboardInterrupt:
     exit()
    