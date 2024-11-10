from XL_Chucnang.CRUDConfig import read_config_server
from XL_Chucnang.Connection import receive_response_65535, send_command, receive_response
import socket

def app_process(client_socket):    
    while True:    
        
        print("\n-- List / Start / Stop cac Applications dang chay SERVER --")
        print("1. List Applications dang chay")
        print("2. Stop Application theo PID")        
        print("3. Start Application theo duong dan (path)")        
        print("0. Tro lai Menu Chinh")
        
        choice = input("Dien lua chon: ")

        if choice == '1':
            list_apps_running(client_socket)        
        elif choice == '2':
            list_apps_running(client_socket)
            stop_app_running_by_PID(client_socket)            
        elif choice == '3':            
            start_app_by_path(client_socket)         
        elif choice == '0':
            print("Quay lai menu chinh.")
            break
        else:
            print("Lua chon khong hop le. Vui long chon lai.")


            
def list_apps_running(client_socket):    
    send_command(client_socket, "LIST_APPS_RUNNING")    
    running_apps = receive_response_65535(client_socket)
    if not running_apps.strip():  # Kiểm tra nếu danh sách trống
        print("\nKhong co applications dang chay.\n")
    else:
        print("\nDanh sach applications dang chay nhu sau:\n", running_apps)

def stop_app_running_by_PID(client_socket):
    pid = input("Dien PID cua application muon dung (Vi du: 12345): ")
    if pid.isdigit():  # Kiểm tra xem PID có phải là số không
        send_command(client_socket, f"STOP_APP {pid}")               
        response = receive_response(client_socket)
        if "not found" in response.lower() or "already stopped" in response.lower():
            print("App khong chay hoac khong duoc phep stop.")
        else:
            print(response)
    else:
        print("PID khong hop le.")
        
def start_app_by_path(client_socket):    
    app_path = input(r"Dien duong dan app de start (e.g., C:\Windows\System32\notepad.exe): ")
    send_command(client_socket, f"START_APP_BY_PATH {app_path}")    
    response = receive_response(client_socket)
    if "not allowed" in response.lower() or "not found" in response.lower():
        print(f"khong tim thay hoac khong duoc phep start App trong duong dan '{app_path}' .")
    else:
        print(response)
    
    
# Khởi tạo socket và gọi hàm
if __name__ == "__main__":  
    server_ip, server_port = read_config_server("config.json")  
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_ip, server_port))  # Địa chỉ IP và port của server
    app_process(client_socket)
    client_socket.close()
    
    
    
