import tkinter as tk
import socket
import threading
import XL_Chucnang.Connection as Connection
import Server.SV_app_process
import Server.SV_services_process
import Server.SV_shutdown_reset
import Server.SV_monitor
import Server.SV_keylogger
import Server.SV_del_copy

from tkinter import messagebox

# Tạo cửa sổ chính
window = tk.Tk()
window.geometry("369x83+24+119")
window.minsize(120, 1)
window.maxsize(5564, 1901)
window.resizable(0, 0)
window.title("RUN SERVER")
window.configure(
    background="#d9d9d9", highlightbackground="#d9d9d9", highlightcolor="#000000"
)

btn_open = None
btn_open = None

# Hàm xử lý khi mở server


def open_server():
    global server_socket
    lbl_status.config(text="Server is openning")
    threading.Thread(target=main).start()


# Hàm xử lý khi đóng server
def close_server():
    global server_socket
    lbl_ip.config(text=f"Bí mật")
    # try:
    server_socket.close()
    messagebox.showinfo(title="THÔNG BÁO", message=f"Closing server")
    lbl_status.config(text="Server stopped.")
    # except:
    #     messagebox.showinfo(title = 'THÔNG BÁO', message=F'Server was not running.')
    #     lbl_status.config(text="Server was not running.")


# Tạo và đặt các nhãn, nút trên giao diện
def create_label(window, text, relx, rely, width):
    return tk.Label(
        window,
        text=text,
        background="#d9d9d9",
        foreground="#000000",
        font="-family {Segoe UI} -size 9",
        anchor="w",
    ).place(relx=relx, rely=rely, height=13, width=width)


# def create_button(window, text, relx, rely, command=None, state="normal"):
#     return tk.Button(
#         window,
#         text=text,
#         background="#d9d9d9",
#         foreground="#000000",
#         font="-family {Segoe UI} -size 9",
#         command=command,
#         state=state,
#     ).place(relx=relx, rely=rely, height=26, width=97)


def create_button_config(text, command, state, x, y, width, height):
    button = tk.Button(window, text=text, command=command, state=state)
    button.place(x=x, y=y, width=width, height=height)
    return button


# Labels cấu hình
labels_config = [
    {"text": "Server IP:", "relx": 0.041, "rely": 0.289, "width": 93},
    {"text": "Port: 8081", "relx": 0.054, "rely": 0.602, "width": 80},
]
for config in labels_config:
    create_label(
        window, config["text"], config["relx"], config["rely"], config["width"]
    )

lbl_status = tk.Label(
    window,
    text="Server is closing",
    background="#d9d9d9",
    foreground="#000000",
    font="-family {Segoe UI} -size 9",
    anchor="w",
)
lbl_status.place(relx=0.300, rely=0.58, height=20, width=300)

lbl_ip = tk.Label(
    window,
    text="Bí mật",
    background="#d9d9d9",
    foreground="#000000",
    font="-family {Segoe UI} -size 9",
    anchor="w",
)
lbl_ip.place(relx=0.22, rely=0.25, height=20, width=119)

btn_open = create_button_config("Open Server", open_server, "normal", x=250, y=10, width=97, height=26)
btn_close = create_button_config("Close Server", close_server, "disabled", x=250, y=60, width=97, height=26)

# Biến server_socket toàn cục
server_socket = None

# Chức năng chính của server


def main():
    global server_socket
    server_ip = socket.gethostbyname(socket.gethostname())
    port = 8081

    if Connection.check_ip_address_valid(server_ip) and Connection.check_port_valid(port):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((server_ip, port))
        server_socket.listen(3)
        messagebox.showinfo(
            title="THÔNG BÁO",
            message=f"Server is listenning on: {server_ip}:{port}",)
        # print(f"Server đang lắng nghe tại {server_ip}:{port}")
        btn_open.config(state="disabled")
        btn_close.config(state="normal")
        lbl_status.config(text=f"Server is openning")
        lbl_ip.config(text=f"{server_ip}")
    else:
        messagebox.showinfo(
            title="THÔNG BÁO",
            message="Địa chỉ IP hoặc Port không hợp lệ hoặc không mở.",)
        lbl_status.config(text="Địa chỉ IP hoặc Port không hợp lệ.")
        lbl_ip.config(text=f"Bí mật")
        return

    try:
        while True:
            client_socket, addr = server_socket.accept()
            print(f"Client connected from {addr}")
            client_thread = threading.Thread(target=handle_client, args=(client_socket,))
            client_thread.start()
    except:
        print("Server is shutting down...")
        btn_open.config(state="normal")
        btn_close.config(state="disabled")
    finally:
        server_socket.close()
        print("Server stopped.")
        btn_open.config(state="normal")
        btn_close.config(state="disabled")


# Hàm xử lý kết nối với client
def handle_client(client_socket):
    try:
        while True:
            buffer = client_socket.recv(1024).decode()
            if not buffer:
                print("Lỗi kết nối đến Client hoặc kết nối đã đóng.")
                break
            print(f"Lệnh đã nhận: {buffer}")
            # Các lệnh xử lý từ client
            if buffer.startswith("LIST_APPS_RUNNING"):
                Server.SV_app_process.list_apps_running(client_socket)
            elif buffer.startswith("START_APP_BY_PATH"):
                app_path = buffer.split(" ", 1)[1]
                Server.SV_app_process.start_app_by_path(client_socket, app_path)
            elif buffer.startswith("STOP_APP"):
                pid = int(buffer.split()[1])
                Server.SV_app_process.stop_app(client_socket, pid)
            elif buffer.startswith("LIST_SERVICES_RUNNING"):
                Server.SV_services_process.list_running_services(client_socket)
            elif buffer.startswith("START_SERVICE"):
                service_name = buffer.split(" ", 1)[1]
                Server.SV_services_process.start_service(client_socket, service_name)
            elif buffer.startswith("STOP_SERVICE"):
                service_name = buffer.split(" ", 1)[1]
                Server.SV_services_process.stop_service(client_socket, service_name)
            elif buffer == "SHUTDOWN_SERVER":
                Server.SV_shutdown_reset.shutdown_server(client_socket)
            elif buffer == "RESET_SERVER":
                Server.SV_shutdown_reset.reset_server(client_socket)
            elif buffer.startswith("VIEW_MONITOR"):
                Server.SV_monitor.monitor(client_socket)
            elif buffer.startswith("START_KEYLOGGER"):
                print("Starting keylogger...")
                Server.SV_keylogger.start_keylogger(client_socket)
            elif buffer == "STOP_KEYLOGGER":
                print("Keylogger stopped")
            elif buffer.startswith("DELETE_FILE"):
                file_path = buffer.split(" ", 1)[1]
                Server.SV_del_copy.delete_file(client_socket, file_path)
            elif buffer.startswith("COPY_FILE"):
                file_path = buffer.split(" ", 1)[1]
                Server.SV_del_copy.copy_file(client_socket, file_path)
            else:
                print("Không biết lệnh vừa nhận từ máy Client.")
    except Exception as e:
        print(f"Lỗi không mong muốn: {e}")
    finally:
        client_socket.close()
        print("Đóng kết nối với máy Client.")


# Menu
menubar = tk.Menu(window, font="TkMenuFont", bg="#d9d9d9", fg="#000000")
window.configure(menu=menubar)

# Bắt đầu vòng lặp chính
window.mainloop()
