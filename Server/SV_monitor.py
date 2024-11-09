import socket
import keyboard
from vidstream import ScreenShareClient
import threading

from XL_Chucnang import Connection
from XL_Chucnang.Connection import send_command
from XL_Chucnang.CRUDConfig import read_config


def monitor(client_socket):    
    video_port = 9999
    
    server_ip, port = read_config()
    # if not Connection.check_port_open(video_port):
    #     Connection.open_port(video_port)
   
    # server_socket_stream = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # server_socket_stream.bind((server_ip, video_port))
    # server_socket_stream.listen(3) 
    
    # try:
    #     while True:            
    #         client_socket, addr = server_socket_stream.accept()
    #         client_thread = threading.Thread(target=monitor, args=(client_socket,))
    #         client_thread.start()
    # except KeyboardInterrupt:
    #     print("Server is shutting down...")
    # finally:
    #     server_socket_stream.close()
    #     print("Server stopped.")       
    
    client_view_stream = ScreenShareClient(str(server_ip), video_port)

    # Bắt đầu luồng chia sẻ màn hình trong một luồng riêng biệt
    stream_thread_stream = threading.Thread(target=client_view_stream.start_stream)
    stream_thread_stream.start()
    
    while input("") != 'STOP':
        continue

    # Theo dõi phím ESC để dừng chia sẻ màn hình
    print("Press ESC to stop screen sharing.")
    keyboard.wait('esc')  # Chờ đến khi phím ESC được nhấn

    # Dừng chia sẻ màn hình
    client_view_stream.stop_stream()
    print("Screen sharing stopped.")