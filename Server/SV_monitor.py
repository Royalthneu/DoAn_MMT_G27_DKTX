import json
import socket
import subprocess
import keyboard
from vidstream import ScreenShareClient
import threading

from XL_Chucnang import Connection
from XL_Chucnang.Connection import check_port_open, open_port
from XL_Chucnang.CRUDConfig import read_config_client


def monitor(client_socket):   
    client_ip, client_port = read_config_client("config.json") 
    print(client_ip)   
    print(client_port)
    # if not check_port_open(video_port):
    #     open_port(video_port)
    
    # client_ip = '172.21.0.1'
    client_view_stream = ScreenShareClient(client_ip, client_port)
    stream_thread_stream = threading.Thread(target=client_view_stream.start_stream)
    stream_thread_stream.start()

    # Theo dõi phím ESC để dừng chia sẻ màn hình
    print("Press ESC to stop screen sharing.")
    keyboard.wait('esc')  # Chờ đến khi phím ESC được nhấn

    # Dừng chia sẻ màn hình
    client_view_stream.stop_stream()
    print("Screen sharing stopped.")    


