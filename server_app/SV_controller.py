# SV_controller.py

import socket
import threading
from SV_model import SV_Model, SV_NetworkModel, SV_App_Process, SV_Del_Copy, SV_Keylogger, SV_ScreenShare, SV_Services
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
            threading.Thread(target=self.listen_for_clients,daemon=True).start()
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
                    client_thread = threading.Thread(
                        target=self.handle_client, args=(client_socket,))
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

    def handle_client(self, client_socket, client_address):
        """Xử lý lệnh từ Client"""
        try:
            while True:
                command = self.model.receive_response(client_socket).strip()

                # List app running
                if command == "LIST_APPS_RUNNING":
                    result = self.model.list_apps_running2()
                    self.model.send_command(client_socket, result)
                elif command.startswith("START_APP_BY_PATH"):
                    app_path = command.split(" ", 1)[1]
                    result = self.model.start_app_by_path(app_path)
                    self.model.send_command(client_socket, result)
                elif command.startswith("STOP_APP"):
                    pid = int(command.split(" ", 1)[1])
                    result = self.model.stop_app_by_pid(pid)
                    self.model.send_command(client_socket, result)

                # List services running
                elif command == "LIST_SERVICES_RUNNING":
                    result = self.model.list_running_services()
                    self.model.send_command(client_socket, result)

                elif command.startswith("START_SERVICE"):
                    service_name = command.split(" ", 1)[1]
                    result = self.model.start_service(service_name)
                    self.model.send_command(client_socket, result)

                elif command.startswith("STOP_SERVICE"):
                    service_name = command.split(" ", 1)[1]
                    result = self.model.stop_service(service_name)
                    self.model.send_command(client_socket, result)

                # Shutdown_reset
                elif command == "SHUTDOWN_SERVER":
                    result = self.model.shutdown_server()
                    self.model.send_command(client_socket, result)

                elif command == "RESET_SERVER":
                    result = self.model.reset_server()
                    self.model.send_command(client_socket, result)

                # Screen_share
                elif command.startswith("START_SCREEN_SHARING"):
                    # Lấy IP và port từ lệnh
                    client_ip, client_port = command.split(
                        " ")[1], int(command.split(" ")[2])
                    client_view_stream, stream_thread = self.model.start_screen_sharing(
                        client_ip, client_port)
                    self.model.send_command(
                        client_socket, "Screen sharing started.")

                    # Chờ dừng chia sẻ màn hình
                    while True:
                        stop_command = self.model.receive_response(
                            client_socket).strip()
                        if stop_command == "STOP_SCREEN_SHARING":
                            result = self.model.stop_screen_sharing(
                                client_view_stream)
                            self.model.send_command(client_socket, result)
                            break

                # Key Logger
                elif command == "START_KEYLOGGER":
                    listener = self.model.start_keylogger()
                    self.model.send_command(
                        client_socket, "Keylogger started.")
                    # Listen for stop command
                    while True:
                        stop_command = self.model.receive_response(
                            client_socket).strip()
                        if stop_command == "STOP_KEYLOGGER":
                            result = self.model.stop_keylogger(listener)
                            self.model.send_command(client_socket, result)
                            break

                # Del va Copy
                elif command.startswith("DELETE_FILE"):
                    # Lấy đường dẫn file từ lệnh
                    file_path = command.split(" ", 1)[1]
                    # Gọi hàm delete_file trong model
                    result = self.model.delete_file(file_path)
                    # Gửi kết quả về client
                    self.model.send_command(client_socket, result)

                elif command.startswith("COPY_FILE"):
                    # Lấy đường dẫn file từ lệnh
                    file_path = command.split(" ", 1)[1]
                    file_size, message = self.model.copy_file(
                        file_path)  # Gọi hàm copy_file trong model

                    if file_size is not None:
                        # Gửi kích thước file đến client
                        client_socket.sendall(
                            file_size.to_bytes(4, byteorder='big'))
                        # Gửi nội dung file tới client
                        with open(file_path, 'rb') as f:
                            while (chunk := f.read(4096)):
                                client_socket.sendall(chunk)
                    else:
                        # Gửi lỗi nếu file không tồn tại
                        self.model.send_command(client_socket, message)

                else:
                    self.model.send_error_message(
                        client_socket, "Unknown command.")

        except Exception as e:
            self.view.log_message(f"Error handling client {
                                  client_address}: {str(e)}")
        finally:
            client_socket.close()
            self.view.log_message(f"Client disconnected: {client_address}")

    def stop_server(self):
        self.model.close_server()
        self.view.set_lbl_status("Server is closed")
        self.view.set_lbl_server_ip("Bí mật")
        self.view.disable_close_button()
        self.view.enable_open_button()
