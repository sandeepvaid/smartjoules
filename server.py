import socket
class Server:
    def __init__(self):
        self.s = socket.socket() 
        port = 9999
        self.s.bind(('', port))
        while True:
 
        
          c, addr = self.s.accept()    
          print ('Got connection from', addr )

          # send a thank you message to the client. encoding to send byte type.
          c.send('Thank you for connecting'.encode())

          # Close the connection with the client
          c.close()

          # Breaking once connection closed
          break
server = Server()