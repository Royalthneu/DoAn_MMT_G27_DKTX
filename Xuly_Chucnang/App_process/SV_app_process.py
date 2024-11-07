
import os
import socket
import subprocess
from module_support import read_config, replace_path, send_error_message, send_success_message, receive_response

def app_process(client_socket): 
    try:
        while True:
            # Nhận lệnh từ client
            command = receive_response(client_socket).strip()

            if command == "LIST_APPS_RUNNING":
                list_apps_running(client_socket)   
            elif command.startswith("START_APP_BY_PATH"):
                app_path = command.split(" ", 1)[1]  # Lấy đường dẫn ứng dụng   
                start_app_by_path(client_socket, replace_path(app_path))            
            elif command.startswith("STOP_APP"):
                pid = int(command.split(" ", 1)[1])  # Lấy PID từ lệnh
                stop_app(client_socket, pid)            
            else:
                error_msg = "Khong hieu cau lenh tu may CLient.\n"
                client_socket.sendall(error_msg.encode())
    finally:
        # Đóng kết nối
        client_socket.close()        
        print("Server stopped.")

def list_apps_running(client_socket):
    try:
        # Lấy danh sách ứng dụng đang chạy bằng tasklist
        output = subprocess.check_output("tasklist", encoding='utf-8') 
        send_success_message(client_socket, output)        
    except Exception as e:
        send_error_message(client_socket, str(e))   

def start_app_by_path(client_socket, app_path):
    #Khởi động ứng dụng từ đường dẫn
    if not os.path.isfile(app_path):
        send_error_message(client_socket, f"Duong dan '{app_path}' khong ton tai.")
        return    
    try:
        # Khởi động ứng dụng
        subprocess.Popen([app_path], shell=True)
        send_success_message(client_socket, f"Khoi dong application: {app_path}")
    except Exception as e:
        send_error_message(client_socket, f" khi start application: {e}")

def stop_app(client_socket, pid):
    #Dừng ứng dụng theo PID
    try:
        # Dừng ứng dụng bằng taskkill
        subprocess.run(["taskkill", "/F", "/PID", str(pid)], check=True)
        send_success_message(client_socket, f"Stop application theo PID {pid}")
    except Exception as e:
        send_error_message(client_socket, f" khi stop application bang PID {pid}: {e}")

if __name__ == "__main__":    
    server_ip, port = read_config()
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_ip, port))  # Dùng IP và port từ file config
    app_process(client_socket)
    client_socket.close()