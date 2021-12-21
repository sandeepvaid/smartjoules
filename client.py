import socket
import sys
import json
class Client:
    def __init__(self):
        try:
            self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            print("Socket successfully created")
        except socket.error as err:
            print ("socket creation failed with error %s" %(err))
            
    def connect(self,host_ip,port):
        self.s.connect(host_ip,port)
        
    def request(self,req_object):
        try:
            jsonObject = json.loads(req_objectq)
            self.s.sendall(jsonObject)
        except:
            print('error')