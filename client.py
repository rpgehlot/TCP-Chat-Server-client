import socket
import sys
import select
import string
#name = raw_input('Enter your name\n')

def prompt() :
  sys.stdout.write('<You>')
  sys.stdout.flush()
  
if __name__ == "__main__":
         
        if len(sys.argv) < 3:
           print "Usage: python client.py localhost 9999"
           sys.exit()

        host = sys.argv[1]
        port = int(sys.argv[2]) 
	# Create a socket (SOCK_STREAM means a TCP socket)
	print 'Establishing Connection ...'
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(2)
	sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	# Connect to server and send data
	try:
         sock.connect((host,port))
        except:
         print "Unable to connect"
         sys.exit()
        print "Connected to localhost server at port 9999"
        prompt()
	while 1:
                 
                 sockets = [sys.stdin,sock]
                 read,write,error = select.select(sockets,[],[])
                 for socket in read:
                   if socket == sock:
                      data = socket.recv(4096)
                      if not data :
                        print 'Connection closed'
                        sys.exit()
                      else :
                        #print data
                        sys.stdout.write(data)
                        prompt()
                   else:
                      msg = sys.stdin.readline()
                      sock.send(msg)
                      prompt()  
      	sock.close()
