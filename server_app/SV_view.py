# SV_view.py

import tkinter as tk

class SV_View:
    def __init__(self, controller):
        self.controller = controller
        self.window = tk.Tk()
        self.window.title("Server Điều khiển Máy khách")
        
        self.host_label = tk.Label(self.window, text="Địa chỉ IP của Server:")
        self.host_label.pack()
        self.host_entry = tk.Entry(self.window)
        self.host_entry.pack()

        self.port_label = tk.Label(self.window, text="Port của Server:")
        self.port_label.pack()
        self.port_entry = tk.Entry(self.window)
        self.port_entry.pack()

        self.start_button = tk.Button(self.window, text="Khởi động Server", command=self.start_server)
        self.start_button.pack()

        self.stop_button = tk.Button(self.window, text="Dừng Server", command=self.stop_server)
        self.stop_button.pack()

        self.status_label = tk.Label(self.window, text="Trạng thái:")
        self.status_label.pack()
        self.status_text = tk.Text(self.window, height=5, width=40)
        self.status_text.pack()

        self.client_data_label = tk.Label(self.window, text="Dữ liệu từ Client:")
        self.client_data_label.pack()
        self.client_data_text = tk.Text(self.window, height=5, width=40)
        self.client_data_text.pack()

    def show_status(self, status):
        """Hiển thị trạng thái server"""
        self.status_text.insert(tk.END, status + "\n")
    
    def show_client_data(self, data):
        """Hiển thị dữ liệu từ client"""
        self.client_data_text.insert(tk.END, f"Dữ liệu client: {data}\n")

    def start_server(self):
        """Khởi động server khi nhấn nút khởi động"""
        host = self.host_entry.get()
        port = int(self.port_entry.get())
        self.controller.start_server(host, port)
    
    def stop_server(self):
        """Dừng server khi nhấn nút dừng"""
        self.controller.stop_server()

    def run(self):
        """Chạy giao diện GUI"""
        self.window.mainloop()
