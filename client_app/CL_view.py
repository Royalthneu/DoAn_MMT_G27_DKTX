import tkinter as tk
from tkinter import ttk

class ClientView:
    def __init__(self, top=None):
        
        top.geometry("375x529+11+283")
        top.minsize(120, 1)
        top.maxsize(5564, 1901)
        top.resizable(0, 0)
        top.title("RUN CLIENT")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="#000000")
        
        self.Entry_IP_address = None
        self.Entry_Port = None
        
        # Separator definitions
        separators = [(0.027, 0.113), (0.027, 0.34)]
        for relx, rely in separators:
            sep = ttk.Separator(top)
            sep.place(relx=relx, rely=rely, relwidth=0.933)
        
        self.create_widgets()

    def create_widgets(self):
        # Tạo các nút và Entry
        self.create_label("Nhập IP của server", 0.08, 0.149, 26, 111)
        self.Entry_IP_address = self.create_entry(0.4, 0.149, 0.491, 20)
        
        self.create_label("Nhập Port của Server", 0.08, 0.206, 26, 121)
        self.Entry_Port = self.create_entry(0.4, 0.206, 0.491, 20)
        
        self.create_button("Ket noi Server", 0.32, 0.261, 26, 107, self.connect_server)
        self.create_button("1. List / Start / Stop cac Applications", 0.08, 0.378, 36, 317, self.list_apps)
        self.create_button("2. List / Start / Stop cac Services", 0.08, 0.469, 36, 317, self.list_services)
        self.create_button("3. Shutdown / Reset may SERVER", 0.08, 0.561, 36, 317, self.shutdown_reset)
        self.create_button("4. Xem man hinh hien thoi cua may SERVER", 0.08, 0.654, 36, 317, self.view_server_screen)
        self.create_button("5. Khoa / Bat phim nhan (keylogger)", 0.08, 0.749, 36, 317, self.toggle_keylogger)
        self.create_button("6. Xoa files ; Copy files tu may SERVER", 0.08, 0.843, 36, 317, self.manage_files)

    def create_label(parent, text, relx, rely, height, width):
        lbl = tk.Label(parent, text=text, background="#d9d9d9", foreground="#000000", font="-family {Segoe UI} -size 9")
        lbl.place(relx=relx, rely=rely, height=height, width=width)

    def create_button(self, text, relx, rely, height, width, command):
        btn = tk.Button(top, text=text, background="#d9d9d9", foreground="#000000", font="-family {Segoe UI} -size 9", command=command)
        btn.place(relx=relx, rely=rely, height=height, width=width)

    def create_entry(self, relx, rely, relwidth, height):
        entry = tk.Entry(top)
        entry.place(relx=relx, rely=rely, relwidth=relwidth, height=height)
        entry.configure(background="white", font="-family {Courier New} -size 10", foreground="#000000")
        return entry

    def connect_server(self):
        # Xử lý kết nối server
        pass
    
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
