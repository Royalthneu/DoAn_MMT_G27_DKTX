import socket
import time
import keyboard
from vidstream import StreamingServer
from XL_Chucnang.CRUDConfig import read_config
from XL_Chucnang.Connection import send_command

def monitor(client_socket):  # Cập nhật hàm monitor để chấp nhận client_socket_stream
    send_command(client_socket, "VIEW_MONITOR")
    
    video_port = 9999
    server_ip, port = read_config()
    
    # client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    # client_socket.connect((server_ip, video_port))
    print(f"Ket noi server co dia chi {server_ip}:{video_port} thanh cong")
    
    server = StreamingServer(str(server_ip), video_port)
    server.start_server()
    
    # Theo dõi phím ESC để dừng chia sẻ màn hình
    print("Press ESC to stop screen sharing.")
    keyboard.wait('esc')  # Chờ đến khi phím ESC được nhấn
    
    # When You Are Done
    server.stop_server()

