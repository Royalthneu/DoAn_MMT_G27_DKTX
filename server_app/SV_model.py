# SV_model.py

import os
import random
import socket
import subprocess
import threading
from vidstream import StreamingServer

import keyboard

class SV_Model:
    def __init__(self, server_ip, port):
        self.server_ip = server_ip
        self.port = port
        self.server_socket = None
        self.running = False

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

class SV_App_Process:
    @staticmethod
    def list_apps_running():
        """Liệt kê các ứng dụng đang chạy"""
        try:
            return subprocess.check_output("tasklist", encoding='utf-8')
        except Exception as e:
            return f"Error while listing apps: {str(e)}"

    @staticmethod
    def start_app_by_path(app_path):
        """Khởi động ứng dụng từ đường dẫn"""
        if not os.path.isfile(app_path):
            return f"Path '{app_path}' does not exist."
        try:
            subprocess.Popen([app_path], shell=True)
            return f"Started application: {app_path}"
        except Exception as e:
            return f"Error starting application: {str(e)}"

    @staticmethod
    def stop_app_by_pid(pid):
        """Dừng ứng dụng theo PID"""
        try:
            subprocess.run(["taskkill", "/F", "/PID", str(pid)], check=True)
            return f"Stopped application with PID {pid}."
        except Exception as e:
            return f"Error stopping application with PID {pid}: {str(e)}"   

class SV_Services:
    @staticmethod
    def list_running_services():
        command = "Get-Service | Where-Object { $_.Status -eq 'Running' } | Format-Table -HideTableHeaders -Property Name,DisplayName"
        return SV_NetworkModel.run_powershell_command(command)

    @staticmethod
    def start_service(service_name):
        command = f"Start-Process sc.exe -ArgumentList 'start', '{service_name}' -Verb runAs"
        return SV_NetworkModel.run_powershell_command(command)

    @staticmethod
    def stop_service(service_name):
        command = f"Start-Process sc.exe -ArgumentList 'stop', '{service_name}' -Verb runAs"
        return SV_NetworkModel.run_powershell_command(command)

class SV_Shutdown:
    @staticmethod
    def shutdown_server():
        try:
            SV_NetworkModel.run_powershell_command("Stop-Computer -Force")
            return "Server is shutting down..."
        except Exception as e:
            return f"Khong the shutdown server: {e}"

    @staticmethod
    def reset_server():
        try:
            SV_NetworkModel.run_powershell_command("Restart-Computer -Force")
            return "Server is reset..."
        except Exception as e:
            return f"Khong the reset server: {e}"

class SV_ScreenShare:
    @staticmethod
    def start_screen_sharing(client_ip, client_port):
        # Tạo đối tượng client chia sẻ màn hình và bắt đầu stream
        client_view_stream = StreamingServer.ScreenShareClient(client_ip, client_port)
        stream_thread = threading.Thread(target=client_view_stream.start_stream)
        stream_thread.start()
        return client_view_stream, stream_thread

    @staticmethod
    def stop_screen_sharing(client_view_stream):
        # Dừng việc chia sẻ màn hình
        client_view_stream.stop_stream()
        return "Screen sharing stopped."

class SV_Keylogger:
    @staticmethod
    def start_keylogger():
        keys_pressed = ""
        MAX_LINE_LENGTH = 50
        stop_keylogger = False
        listener = None

        def on_press(key):
            nonlocal keys_pressed, stop_keylogger
            if stop_keylogger:
                return False

            if hasattr(key, 'char') and key.char is not None:
                key_str = key.char
            else:
                key_str = f' {str(key)} '

            if key == keyboard.Key.enter:
                keys_pressed = ""
            else:
                keys_pressed += key_str

            return key_str

        listener = keyboard.Listener(on_press=on_press)
        listener.start()

        return listener

    @staticmethod
    def stop_keylogger(listener):
        listener.stop()
        return "KEYLOGGER_STOPPED"


class SV_Del_Copy:
    @staticmethod
    def delete_file(client_socket, file_path):
    # Xóa file tại đường dẫn được chỉ định trên server.
        if os.path.exists(file_path):
            try:
                os.remove(file_path)
                return f"Xoa file thanh cong."
            except Exception as e:
                return f"Loi: xoa file: {e}"
        else:
            return f"File khong ton tai tren may Server."  
        
    @staticmethod
    def copy_file(client_socket, file_path):
        #Sao chép file tại đường dẫn được chỉ định trên server và gửi tới client.
        if os.path.exists(file_path):        
            # Lấy kích thước file
            file_size = os.path.getsize(file_path)
            
            # Gửi kích thước file đến client
            client_socket.sendall(file_size.to_bytes(4, byteorder='big'))
            
            # Gửi file tới client
            with open(file_path, 'rb') as f:
                while (chunk := f.read(4096)):
                    client_socket.sendall(chunk)
        else:
            # Nếu file không tồn tại, gửi kích thước 0 để báo lỗi
            client_socket.sendall((0).to_bytes(4, byteorder='big'))

class SV_NetworkModel:
    @staticmethod
    def check_ip_address_valid(ip):
        try:
            socket.inet_aton(ip)
            return True
        except socket.error:
            return False
    
    @staticmethod
    def check_port_valid(port):
        if 0 < int(port) <= 65535:
            return True
        else:
            return False
    
    @staticmethod
    def check_port_open(port):
        """Kiểm tra xem cổng đã được mở hay chưa"""
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            return s.connect_ex(('localhost', port)) == 0

    @staticmethod
    def open_port(port):
        """Mở cổng TCP bằng PowerShell"""
        try:
            command = f'New-NetFirewallRule -DisplayName "Open Port {port}" -Direction Inbound -LocalPort {port} -Protocol TCP -Action Allow'
            result = subprocess.run(
                ["powershell", "-Command", command],
                capture_output=True, text=True
            )
            if result.returncode == 0:
                return f"Cổng {port} đã được mở thành công."
            else:
                return f"Lỗi khi mở cổng {port}: {result.stderr}"
        except Exception as e:
            return f"Lỗi khi thực thi lệnh PowerShell: {e}"

    @staticmethod
    def find_and_open_port():
        """Tìm một cổng bất kỳ từ 50000 đến 60000 và mở nó nếu cần"""
        while True:
            port = random.randint(50000, 60000)
            if SV_NetworkModel.check_port_open(port):
                return f"Cổng {port} đã được mở."
            else:
                return port

    @staticmethod
    def input_ip_port(prompt_ip, prompt_port):
        """Nhận thông tin IP và port từ người dùng và kiểm tra tính hợp lệ"""
        while True:
            ip = input(prompt_ip)
            if not SV_NetworkModel.check_ip_address_valid(ip):
                print("IP address không hợp lệ. Vui lòng nhập lại.")
                continue

            try:
                port = int(input(prompt_port))
                if not SV_NetworkModel.check_port_valid(port):
                    print("Port phải là số và nằm trong khoảng từ 1 đến 65535.")
                    continue
            except ValueError:
                print("Port phải là dạng số nguyên.")
                continue

            return ip, port

    @staticmethod
    def send_command(socket, command):
        """Gửi câu lệnh từ client/server đến server/client"""
        socket.sendall(command.encode())
    
    @staticmethod
    def receive_response(socket, buffer_size=4096):
        """Nhận phản hồi từ server/client"""
        return socket.recv(buffer_size).decode()

    @staticmethod
    def send_message(client_socket, message):
        """Hàm gửi thông báo đến client"""
        client_socket.sendall(message.encode())
    
    @staticmethod
    def send_error_message(client_socket, message):
        """Hàm gửi thông báo lỗi"""
        SV_NetworkModel.send_command(client_socket, f"Lỗi: {message}\n")

    @staticmethod
    def send_success_message(client_socket, message):
        """Hàm gửi thông báo thành công"""
        SV_NetworkModel.send_command(client_socket, f"{message}\n")
    
    @staticmethod
    def run_powershell_command(command):
        """Thực thi lệnh PowerShell và trả về kết quả hoặc lỗi"""
        try:
            result = subprocess.run(
                ["powershell", "-Command", command],
                check=True, capture_output=True, text=True
            )
            return result.stdout
        except subprocess.CalledProcessError as e:
            return e.stderr     

