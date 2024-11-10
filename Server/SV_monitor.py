import json
import socket
import subprocess
import keyboard
from vidstream import ScreenShareClient
import threading

from XL_Chucnang import Connection
from XL_Chucnang.Connection import check_port_open, open_port
from XL_Chucnang.CRUDConfig import read_config


def monitor(client_socket):   
    client_ip, port = read_config("CL_addr_config.json")    
    # if not check_port_open(video_port):
    #     open_port(video_port)
    
    client_view_stream = ScreenShareClient(client_ip, 6789)
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


