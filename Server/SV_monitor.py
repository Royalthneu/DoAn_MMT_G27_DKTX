from vidstream import StreamingServer
from XL_Chucnang import Connection
from XL_Chucnang.CRUDConfig import read_config

def monitor():  # Cập nhật hàm monitor để chấp nhận client_socket_stream
    server_ip, port = read_config()
    video_port = 9999
    
    server = StreamingServer('127.0.0.1', video_port)
    server.start_server()

    while input("") != 'STOP':
        continue

    # When You Are Done
    server.stop_server()
