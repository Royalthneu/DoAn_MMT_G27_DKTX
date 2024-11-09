from vidstream import StreamingServer
from XL_Chucnang import Connection
from XL_Chucnang.CRUDConfig import read_config

def monitor():  # Cập nhật hàm monitor để chấp nhận client_socket_stream
    server = StreamingServer('192.168.1.109', 9999)
    server.start_server()

    while input("") != 'STOP':
        continue

    # When You Are Done
    server.stop_server()
