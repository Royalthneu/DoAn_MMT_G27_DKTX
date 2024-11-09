from socket import socket
import threading
from vidstream import StreamingServer

from Server_run import handle_client
from XL_Chucnang.CRUDConfig import read_config

def monitor():    
    
    server_ip, port = read_config() 
    server = StreamingServer(server_ip, port)
    server.start_server()
    
    while input("") != 'STOP':
        continue

    #When You Are Done
    server.stop_server()  