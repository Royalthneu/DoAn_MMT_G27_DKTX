import socket
import threading
from tkinter import messagebox

from CL_view import CL_app_process

#CL_model.py
class CL_Model:
    def __init__(self, view):
        self.view = view
        self.ip_address = ""
        self.port = ""

    def list_apps_running(self, client_socket):
        """ Tạo một luồng mới để xử lý việc gửi yêu cầu và nhận dữ liệu """
        threading.Thread(target=self._list_apps_running, args=(client_socket,), daemon=True).start()

    def _list_apps_running(self, client_socket):
        try:
            # Gửi lệnh yêu cầu danh sách ứng dụng đang chạy đến server
            client_socket.sendall("CM_LIST_APPS_RUNNING".encode())

            # Decode dữ liệu an toàn
            response = client_socket.recv(65535).decode('utf-8')
            print(f"Decoded response: {response}")  # Log decoded response

            if not response:
                self.view.show_error("Không nhận được dữ liệu từ server.")
                return

            if "Lệnh không hợp lệ" in response:
                self.view.show_error("Server: Lệnh không hợp lệ.")
                return

            # Xử lý dữ liệu nhận được
            app_list = self.parse_app_list(response)
            
            # Cập nhật TreeView thông qua CL_App_Process
            app_process = CL_app_process(self.view)  # Khởi tạo CL_App_Process với view
            app_process.update_tree_view(app_list)

        except Exception as e:
            self.view.show_error(f"Lỗi kết nối: {str(e)}")
        finally:
            client_socket.close()

    def parse_app_list(self, data):
        """ Xử lý dữ liệu từ server và trả về danh sách ứng dụng dưới dạng dict. """
        app_list = []
        lines = data.splitlines()

        # Bỏ qua tiêu đề cột và dòng phân cách (2 dòng đầu)
        app_list_data = lines[3:] if len(lines) > 3 else []

        # Phân tích dữ liệu ứng dụng
        for line in app_list_data:
            parts = line.split()
            if len(parts) >= 2:
                pid = parts[1]
                app_name = " ".join(parts[0:])
                app_list.append({'pid': pid, 'name': app_name})

        return app_list    

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
        name = window_instance.entry_nhap_Name.get()
        if name:  # Kiểm tra nếu tên không rỗng
            print(f"Tên đã nhập: {name}")
            # self.start_app(name)  # Gọi hàm start_app với tên đã nhập
            window_instance.top.destroy()  # Đóng cửa sổ CL_form_nhap_Name
        else:
            messagebox.showerror(title = "Lỗi", message="Tên không hợp lệ! Vui lòng nhập lại.")
        return name
        
    def get_pid_from_entry(self, window_instance):
        pid = window_instance.entry_nhap_PID.get()  # Lấy giá trị từ Entry trong View
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