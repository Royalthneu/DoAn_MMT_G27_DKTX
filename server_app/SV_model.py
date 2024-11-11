# SV_model.py

import socket



class SV_Model:
    def __init__(self, server_ip, port):
        self.server_ip = server_ip
        self.port = port


    def start_server(self):
        try:
            self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.server_socket.bind((self.server_ip, self.port))
            self.server_socket.listen(3)
            print(f"Server is listening on: {self.server_ip}:{self.port}")
            return True
        except Exception as e:
            print(f"Error while starting server: {e}")
            return False

    def accept_client(self):
        try:
            client_socket, addr = self.server_socket.accept()
            return client_socket, addr
        except Exception as e:
            print(f"Error while accepting client: {e}")
            return None, None

    def close_server(self):
        if self.server_socket:
            self.server_socket.close()  # Đóng socket của server
            print("Server stopped.")
        self.server_socket = None  # Đảm bảo server_socket không còn giá trị sau khi dừng
        
        
        
    # def check_ip_address_valid(self, ip):
    #     try:
    #         socket.inet_aton(ip)
    #         return True
    #     except socket.error:
    #         return False
        
    # def check_server_port_valid(self, server_port):
    #     if 0 < int(server_port) <= 65535:
    #         return True
    #     else:
    #         return False
        
    # def check_server_port_open(self, server_port):
    #     # Kiểm tra xem cổng đã được mở hay chưa.
    #     with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    #         return s.connect_ex(('localserver_ip', server_port)) == 0

    # def open_server_port(self, server_port):
    #     # Mở một cổng bằng PowerShell.
    #     try:
    #         command = f'New-NetFirewallRule -DisplayName "Open server_port {server_port}" -Direction Inbound -Localserver_port {server_port} -Protocol TCP -Action Allow'
    #         result = subprocess.run(
    #             ["powershell", "-Command", command],
    #             capture_output=True, text=True
    #         )
    #         if result.returncode == 0:
    #             print(f"Cổng {server_port} đã được mở thành công.")
    #         else:
    #             print(f"Lỗi khi mở cổng {server_port}:", result.stderr)
    #     except Exception as e:
    #         print("Lỗi khi thực thi lệnh PowerShell:", e)


    
    # def send_command(self, socket, command):
    #     """Gửi dữ liệu trả lời cho client"""
    #     socket.sendall(command.encode())
    
    # def send_command_utf8(self, socket, command):
    #     """Gửi dữ liệu trả lời cho client"""
    #     socket.sendall(command.encode("utf8"))      
    
    # def receive_response(self, socket, buffer_size=65535):
    #     """Nhận dữ liệu từ client"""
    #     data = socket.recv(buffer_size).decode()
    #     return data
    
    # def receive_response_utf8(self, socket, buffer_size=65535):
    #     """Nhận dữ liệu từ client"""
    #     data = socket.recv(buffer_size).decode("utf8")
    #     return data
    
    # def replace_path(self, file_path):
    #     if '\\\\' in file_path:
    #         file_path = file_path.replace("\\\\", "\\")  # Thay thế '\\' thành '\'
            
    # def send_message(self, client_socket, message):
    #     #Hàm gửi thông báo đến client
    #     client_socket.sendall(message.encode())
    
    # def run_powershell_command(command):
    #     """Hàm thực thi lệnh PowerShell và trả về kết quả hoặc lỗi"""
    #     try:
    #         result = subprocess.run(
    #             ["powershell", "-Command", command],
    #             check=True, capture_output=True, text=True
    #         )
    #         return result.stdout
    #     except subprocess.CalledProcessError as e:
    #         return e.stderr        
    
    
    # def process_request(self, data):
    #     """Xử lý yêu cầu từ client"""
    #     # Bạn có thể thay đổi logic ở đây để xử lý các yêu cầu khác nhau
    #     return f"Đã nhận lệnh: {data}"
    
    # def close_socket(self, socket):
    #     """Đóng kết nối với client"""
    #     socket.close()

    # def stop_server(self):
    #     """Dừng server"""
    #     if self.server_socket:
    #         self.server_socket.close()
    #         self.server_socket = None
            

