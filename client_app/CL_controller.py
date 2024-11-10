import tkinter as tk
from CL_model import ServerConnection
from CL_view import ClientView

class ClientController:
    def __init__(self, root):
        self.model = None
        self.view = ClientView(root)
        self.view.connect_server = self.connect_server
        self.view.list_apps = self.list_apps
        self.view.list_services = self.list_services
        self.view.shutdown_reset = self.shutdown_reset
        self.view.view_server_screen = self.view_server_screen
        self.view.toggle_keylogger = self.toggle_keylogger
        self.view.manage_files = self.manage_files

    def connect_server(self):
        ip = self.view.Entry_IP_address.get()
        port = self.view.Entry_Port.get()
        self.model = ServerConnection(ip, port)
        
        if self.model.connect():
            tk.messagebox.showinfo("Success", "Connected to server!")
        else:
            tk.messagebox.showerror("Error", "Failed to connect to server!")

    def list_apps(self):
        # Xử lý danh sách ứng dụng
        pass

    def list_services(self):
        # Xử lý danh sách services
        pass

    def shutdown_reset(self):
        # Xử lý shutdown/reset server
        pass

    def view_server_screen(self):
        # Xử lý xem màn hình server
        pass

    def toggle_keylogger(self):
        # Xử lý bật/tắt keylogger
        pass

    def manage_files(self):
        # Xử lý quản lý file
        pass
