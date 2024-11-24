import random
import socket
import subprocess
from tkinter import messagebox

class CL_Model:
    def __init__(self):
        self.ip_address = ""
        self.port = ""

    def set_ip_address(self, ip):
        self.ip_address = ip

    def set_port(self, port):
        self.port = port

    def get_ip_address(self):
        return self.ip_address

    def get_port(self):
        return self.port
    
    def get_name_from_entry(self, window_instance):
        # Lấy tên từ entry
        name = window_instance.entry_nhap_Name.get().strip()
        if name:  # Kiểm tra nếu tên không rỗng
            print(f"Tên đã nhập: {name}")
            # self.start_app(name)  # Gọi hàm start_app với tên đã nhập
            window_instance.top.destroy()  # Đóng cửa sổ CL_form_nhap_Name
        else:
            messagebox.showerror(title = "Lỗi", message="Tên không hợp lệ! Vui lòng nhập lại.")
        return name
        
    def get_pid_from_entry(self, window_instance):
        pid = window_instance.entry_nhap_PID.get().strip()  # Lấy giá trị từ Entry trong View
        if pid.isdigit():
            print(f"PID đã nhập: {pid}")
            # self.stop_app(pid)
            window_instance.top.destroy()
        else:
            messagebox.showerror(title= "Lỗi", message="PID không hợp lệ! Vui lòng nhập lại.")  # Gửi thông báo lỗi
        return pid    

    def connect_to_server(self, server_ip, server_port):
        """Kết nối tới server với IP và port đã cho."""
        try:
            self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.client_socket.connect((server_ip, server_port))
            return self.client_socket
        except socket.error as e:
            print(f"Connection failed: {e}")
            return None
    
    def check_ip_address_valid(ip):
        try:
            socket.inet_aton(ip)
            return True
        except socket.error:
            return False
    
    def check_port_valid(port):
        if 0 < int(port) <= 65535:
            return True
        else:
            return False

    def send_command(self, socket, command):
        """Gửi câu lệnh từ client/server đến server/client"""
        socket.sendall(command.encode())
    
    def receive_response(self, socket, buffer_size=65535):
        """Nhận phản hồi từ server/client"""
        return socket.recv(buffer_size).decode()