# SV_controller.py

import socket
from SV_model import SV_Model
from SV_view import SV_View

class SV_Controller:
    def __init__(self):
        self.model = SV_Model()
        self.view = SV_View(self)

    def start_server(self, host, port):
        """Khởi động server và chờ kết nối từ client"""
        try:
            self.model.start_server(host, port)
            self.view.show_status("Server đã khởi động thành công!")
        except Exception as e:
            self.view.show_status(f"Lỗi khởi động server: {str(e)}")

    def handle_client(self, connection, address):
        """Xử lý yêu cầu từ client"""
        try:
            self.view.show_status(f"Kết nối mới từ {address}")
            data = self.model.receive_data(connection)
            self.view.show_client_data(data)
            response = self.model.process_request(data)
            self.model.send_data(connection, response)
        except Exception as e:
            self.view.show_status(f"Lỗi xử lý yêu cầu từ client: {str(e)}")
        finally:
            self.model.close_connection(connection)
    
    def stop_server(self):
        """Dừng server"""
        self.model.stop_server()
        self.view.show_status("Server đã dừng!")
