import threading
from tkinter import messagebox
import tkinter as tk

from CL_view import CL_app_process, CL_services_process, CL_shutdown_reset, CL_view_screen, CL_keylogger, CL_del_copy, CL_form_nhap_PID, CL_form_nhap_Name
from CL_model import CL_Model

#CL_controller.py
class CL_Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.client_socket = None
        
        self.view.btn_connect.configure(command=self.connect_to_server)
        self.assign_button_actions()

    def assign_button_actions(self):
        # Gắn các sự kiện cho nút CL_view        
        self.view.btn_applications.configure(
            command=lambda: self.open_window(self.client_socket, CL_app_process))
        self.view.btn_services.configure(
            command=lambda: self.open_window(self.client_socket, CL_services_process)) 
        self.view.btn_shutdown_reset.configure(
            command=lambda: self.open_window(self.client_socket, CL_shutdown_reset))
        self.view.btn_view_screen.configure(
            command=lambda: self.open_window(self.client_socket, CL_view_screen))
        self.view.btn_keylogger.configure(
            command=lambda: self.open_window(self.client_socket, CL_keylogger))
        self.view.btn_file_operations.configure(
            command=lambda: self.open_window(self.client_socket, CL_del_copy))  

    def connect_to_server(self):
        ip = self.view.entry_ip.get()
        port = self.view.entry_port.get()

        if not ip or not port:
            messagebox.showerror("Error", "Vui lòng nhập IP và Port!")
            return

        self.model.set_ip_address(ip)
        self.model.set_port(port)
                
        # Thực hiện kết nối đến server qua Model (nếu cần)
        self.client_socket = self.model.connect_to_server(ip, int(port))
        
        if self.client_socket:
            # Nếu kết nối thành công, hiển thị thông báo thành công
            messagebox.showinfo("Success", f"Kết nối tới Server {ip}:{port} thành công!")

        else:
            # Nếu kết nối thất bại, hiển thị thông báo lỗi
            messagebox.showerror("Error", "Không thể kết nối tới server. Kiểm tra lại IP và Port!")

    def show_message(self, feature):
        messagebox.showinfo("Feature", f"Tính năng '{feature}' đang được triển khai.")
        
    def open_window(self, client_socket, window_class):
    # Tạo cửa sổ mới
        top = tk.Toplevel()
        # Khởi tạo cửa sổ từ lớp window_class
        window_instance = window_class(top=top, client_socket=client_socket, controller=self)
        # Đảm bảo rằng cửa sổ chính không thể click khi cửa sổ top đang mở
        top.grab_set()
        
        #1. Gắn các sự kiện cho nút CL_app_process
        if isinstance(window_instance, CL_app_process):
            window_instance.btn_list_app.configure(command=lambda: self.list_apps_running(client_socket))
            window_instance.btn_start_app.configure(command=lambda: self.open_window(client_socket, CL_form_nhap_Name))            
            window_instance.btn_stop_app.configure(command=lambda: self.open_window(client_socket, CL_form_nhap_PID))            
            window_instance.btn_clear_list_app.configure(command=self.clear_list_apps)
            
        elif isinstance(window_instance, CL_form_nhap_Name): 
                # Sự kiện khi nhấn nút btn_nhap_Name
                window_instance.btn_nhap_Name.configure(command=lambda: self.start_app(client_socket, window_instance))
                
        elif isinstance(window_instance, CL_form_nhap_PID): 
                # Sự kiện khi nhấn nút btn_nhap_ID
                window_instance.btn_nhap_PID.configure(command=lambda: self.stop_app(client_socket, window_instance))    
        
        #2. Gắn các sự kiện cho nút CL_services_process  


        #3. Gắn các sự kiện cho nút CL_shutdown_reset 
        
        
        #4. Gắn các sự kiện cho nút CL_view_screen 
        
        
        #5. Gắn các sự kiện cho nút CL_keylogger 
        
        
        #6. Gắn các sự kiện cho nút CL_del_copy  
        
        
        # Khi cửa sổ top đóng, hủy grab_set
        top.protocol("WM_DELETE_WINDOW", lambda: (top.grab_release(), top.destroy()))
        
    #1. CL_app_process    
    def list_apps_running(self, client_socket):
        """ Xử lý sự kiện nhấn nút 'LIST APPS' """
        self.model.list_apps_running(client_socket)
        
        
    def start_app(self, client_socket, window_instance):
        app_name = self.model.get_name_from_entry(window_instance)  # Lấy tên từ model
        if app_name:
            self.model.send_command(client_socket, f"START_APP_BY_NAME {app_name}")
            response = self.model.receive_response(client_socket)
            return response

    def stop_app(self, client_socket, window_instance):
        app_pid = self.model.get_pid_from_entry(window_instance)  # Lấy tên từ model
        if app_pid:
            self.model.send_command(client_socket, f"STOP_APP_BY_PID {app_pid}")
            response = self.model.receive_response(client_socket)
            return response

    def clear_list_apps(treeview):   
        for item in treeview.get_children():
            treeview.delete(item)  
    
    #2. Xử lý CL_services_process  
    def list_service_running(self, client_socket):
        self.model.send_command(client_socket, "LIST_SERVICES_RUNNING")
        response = self.model.receive_response(client_socket)
        return response
    
    def start_service(self, client_socket, name):
        self.model.send_command(client_socket, f"START_SERVICE_BY_NAME {name}")
        response = self.model.receive_response(client_socket)
        return response

    def stop_service(self,client_socket, pid):
        self.model.send_command(client_socket, f"STOP_SERVICE_BY_PID {pid}")
        response = self.model.receive_response(client_socket)
        return response

    def clear_list_services(treeview):        
        for item in treeview.get_children():
            treeview.delete(item)      
    
    #3. Xử lý CL_shutdown_reset 
    
    
    #4. Xử lý CL_view_screen 
    
    
    #5. Xử lý CL_keylogger 
    
    
    #6. Xử lý CL_del_copy     
    