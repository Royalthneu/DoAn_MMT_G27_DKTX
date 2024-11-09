from socket import socket
import threading
from vidstream import StreamingServer

from Server_run import handle_client
from XL_Chucnang.CRUDConfig import read_config

def monitor():    
    
    server_ip, port = read_config() 
    server = StreamingServer(server_ip, 9999)
    server.start_server()
    
    while input("") != 'STOP':
        continue

    # When You Are Done
    # server.stop_server()
    
    # server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # server_socket.bind((server_ip, port))
    # server_socket.listen(5) 
    
    # client_socket, addr = server_socket.accept()
    # print(f"Client connected from {addr}")

    # # Tạo một thread mới để xử lý client
    # client_thread = threading.Thread(target=handle_client, args=(client_socket,))
    # client_thread.start() 