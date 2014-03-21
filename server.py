# !/usr/bin/python
import socket
import select
def send_to_remaining(sock,message):
      for socket in Connection_list:
        if socket != server_sock and socket != sock :
            try :
                socket.send('\n'+message)
            except :
                # broken socket connection may be, chat client pressed ctrl+c for example
                socket.close()
                Connection_list.remove(socket)

if __name__ == "__main__":

	Connection_list = []
	host,port = "localhost",9999
	server_sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	server_sock.bind((host,port))
	server_sock.listen(10)
	Connection_list.append(server_sock)
        print "Chat Server started at Port 9999 on localhost"
        
	while 1:
	  readable_list,writable_list,error_list = select.select(Connection_list,[],[])

	  for socket in readable_list:
	    if socket == server_sock:   
	       new_conn,addr = server_sock.accept()
	       Connection_list.append(new_conn)
	       print "Got a connection from {} ".format(addr)
	       send_to_remaining(new_conn,"(%s %s) entered the chatroom\n" % addr)
	    else:
	      try:
		 data = socket.recv(1024)
		 if data:
		  send_to_remaining(socket,'>'+str(socket.getpeername())+data)
	      except:
		 send_to_remaining(socket,"User (%s %s) is offline\n"% addr)
		 print " User (%s %s) is offline " % addr 
		 socket.close()
		 Connection_list.remove(socket)
		 continue
	server_sock.close()         



















     
