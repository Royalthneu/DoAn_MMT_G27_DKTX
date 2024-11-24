from tkinter import messagebox
import tkinter as tk

from CL_view import CL_app_process, CL_services_process, CL_shutdown_reset, CL_view_screen, CL_keylogger, CL_del_copy


class CL_Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view

        # Gắn các sự kiện cho nút
        self.view.btn_connect.configure(command=self.connect_to_server)
        self.view.btn_applications.configure(
            command=lambda:self.open_window(CL_app_process))
        self.view.btn_services.configure(
            command=lambda: self.open_window(CL_services_process)) 
        self.view.btn_shutdown_reset.configure(
            command=lambda: self.open_window(CL_shutdown_reset))
        self.view.btn_view_screen.configure(
            command=lambda: self.open_window(CL_view_screen))
        self.view.btn_keylogger.configure(
            command=lambda: self.open_window(CL_keylogger))
        self.view.btn_file_operations.configure(
            command=lambda: self.open_window(CL_del_copy))

    def connect_to_server(self):
        ip = self.view.entry_ip.get()
        port = self.view.entry_port.get()

        if not ip or not port:
            messagebox.showerror("Error", "Vui lòng nhập IP và Port!")
            return

        self.model.set_ip_address(ip)
        self.model.set_port(port)
        messagebox.showinfo("Success", f"Kết nối tới Server {ip}:{port} thành công!")

    def show_message(self, feature):
        messagebox.showinfo("Feature", f"Tính năng '{feature}' đang được triển khai.")
        
    def open_window(self, window_class):
    # Tạo cửa sổ mới
        top = tk.Toplevel()
        # Khởi tạo cửa sổ từ lớp window_class
        window_class(top=top)
        # Đảm bảo rằng cửa sổ chính không thể click khi cửa sổ top đang mở
        top.grab_set()
        # Khi cửa sổ top đóng, hủy grab_set
        top.protocol("WM_DELETE_WINDOW", lambda: (top.grab_release(), top.destroy()))
    
    