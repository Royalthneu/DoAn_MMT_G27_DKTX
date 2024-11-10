import json
import socket
import keyboard
from vidstream import StreamingServer
from XL_Chucnang.CRUDConfig import read_config
from XL_Chucnang.Connection import send_command

def monitor(client_socket):  # Cập nhật hàm monitor để chấp nhận client_socket_stream
    send_command(client_socket, "VIEW_MONITOR")
    
    client_ip, port = read_config("CL_addr_config.json")
    
    server = StreamingServer(str(client_ip), 6789)
    server.start_server()
    
    # Theo dõi phím ESC để dừng chia sẻ màn hình
    print("Press ESC to stop screen sharing.")
    keyboard.wait('esc')  # Chờ đến khi phím ESC được nhấn
    
    # When You Are Done
    server.stop_server()