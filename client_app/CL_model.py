import socket

class ServerConnection:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.socket = None

    def connect(self):
        """Kết nối với server"""
        try:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.connect((self.ip, self.port))
            return True
        except Exception as e:
            return False

    def disconnect(self):
        """Đóng kết nối với server"""
        if self.socket:
            self.socket.close()
            self.socket = None

    def send_data(self, data):
        """Gửi dữ liệu tới server"""
        if self.socket:
            self.socket.sendall(data.encode())
    
    def receive_data(self):
        """Nhận dữ liệu từ server"""
        if self.socket:
            return self.socket.recv(1024).decode()
        return ""
