# SV_model.py

import socket

class SV_Model:
    def __init__(self):
        self.server_socket = None

    def start_server(self, host, port):
        """Khởi động server và lắng nghe kết nối"""
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((host, port))
        self.server_socket.listen(5)
    
    def accept_client(self):
        """Chấp nhận kết nối từ client"""
        connection, address = self.server_socket.accept()
        return connection, address
    
    def receive_data(self, connection):
        """Nhận dữ liệu từ client"""
        data = connection.recv(1024).decode()
        return data
    
    def process_request(self, data):
        """Xử lý yêu cầu từ client"""
        # Bạn có thể thay đổi logic ở đây để xử lý các yêu cầu khác nhau
        return f"Đã nhận lệnh: {data}"
    
    def send_data(self, connection, data):
        """Gửi dữ liệu trả lời cho client"""
        connection.sendall(data.encode())
    
    def close_connection(self, connection):
        """Đóng kết nối với client"""
        connection.close()

    def stop_server(self):
        """Dừng server"""
        if self.server_socket:
            self.server_socket.close()
            self.server_socket = None
