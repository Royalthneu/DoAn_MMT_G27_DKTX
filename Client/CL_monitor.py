import socket
import keyboard
from vidstream import ScreenShareClient
import threading

from XL_Chucnang.CRUDConfig import read_config
from XL_Chucnang.Connection import receive_response, send_command

def monitor(client_socket):
    send_command(client_socket, "VIEW_MONITOR")
    
    server_ip, port = read_config() 
    ssc = ScreenShareClient(server_ip, 9999)

    # Bắt đầu luồng chia sẻ màn hình trong một luồng riêng biệt
    stream_thread = threading.Thread(target=ssc.start_stream)
    stream_thread.start()

    # Theo dõi phím ESC để dừng chia sẻ màn hình
    print("Press ESC to stop screen sharing.")
    keyboard.wait('esc')  # Chờ đến khi phím ESC được nhấn

    # Dừng chia sẻ màn hình
    ssc.stop_stream()
    print("Screen sharing stopped.")   
    
    
        
    