# SV_controller.py

import socket
import threading
from SV_model import SV_Model
from SV_view import SV_View

class SV_Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.view.btn_open.config(command=self.start_server)
        self.view.btn_close.config(command=self.stop_server)

    def start_server(self):
        if self.model.start_server():
            self.view.show_message("THÔNG BÁO", f"Server is listening on: {self.model.server_ip}:{self.model.port}")
            self.view.set_lbl_status("Server is opening")
            self.view.set_lbl_server_ip(self.model.server_ip)
            self.view.disable_open_button()
            self.view.enable_close_button()
            threading.Thread(target=self.listen_for_clients, daemon=True).start()
        else:
            self.view.show_message("Lỗi", "Không thể khởi động server.")
            self.view.enable_open_button()
            self.view.disable_close_button()
            return

    def listen_for_clients(self):
        try:
            while True:
                client_socket, addr = self.model.accept_client()
                if client_socket:
                    print(f"Client connected from {addr}")
                    client_thread = threading.Thread(target=self.handle_client, args=(client_socket,))
                    client_thread.start()
                else:
                    break  # Nếu không có client kết nối, thoát khỏi vòng lặp
        except Exception as e:
            print(f"Error: {e}")
            self.view.enable_open_button()
            self.view.disable_close_button()
        finally:
            self.stop_server()
            self.view.enable_open_button()
            self.view.disable_close_button()

    def handle_client(self, client_socket):
        try:
            while True:
                buffer = client_socket.recv(1024).decode()
                if not buffer:
                    print("Connection lost or closed.")
                    break
                print(f"Command received: {buffer}")
                # Handle client commands
                # Example: process the command here...
        except Exception as e:
            print(f"Unexpected error: {e}")
        finally:
            client_socket.close()
            print("Connection closed.")

    def stop_server(self):
        self.model.close_server()
        self.view.set_lbl_status("Server is closed")
        self.view.set_lbl_server_ip("Bí mật")
        self.view.disable_close_button()
        self.view.enable_open_button()
