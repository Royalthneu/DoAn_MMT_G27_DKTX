from Xuly_Chucnang.App_process.CL_app_process import app_process
import connection
from Xuly_Chucnang.Del_copy.CL_del_copy import del_copy
from Xuly_Chucnang.Keylogger.CL_keylogger import bat_tat_key_logger
from Xuly_Chucnang.Monitor.CL_monitor import monitor
from Xuly_Chucnang.Services_process.CL_services_process import services_process
from Xuly_Chucnang.Shutdown_reset.CL_shutdown_reset import shutdown_reset
import socket

from CRUD import update_config

def main():
    while True:
        server_ip = input("Dien dia chi IP cua Server: ")
        if not connection.check_ip_address_valid(server_ip):
            print("IP khong hop le. Vui long dien lai.")
            continue
        
        port = int(input("Dien so port: "))
        if not connection.check_port_valid(port):
            print("Port khong hop le. Vui long dien lai.")
            continue

        try:
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # client_socket.settimeout(3) # Set thời gian chời kết nối ở đây là 3s  
            client_socket.connect((server_ip, port))
            print(f"Ket noi server co dia chi {server_ip}:{port} thanh cong")
            break
        except socket.error as e:
            print(f"Ket noi khong thanh cong: {e}. Vui long kiem tra server co dang chay khong va IP, port co dung khong.")
            client_socket.close()
            continue
    
    # Lưu đỉa chị server và port và config.json
    update_config(server_ip, port)
      
    while True:
        print("\n- MENU CHINH -")
        print("1. List / Start / Stop cac Applications dang chay SERVER")
        print("2. List / Start / Stop cac Services dang chay SERVER")
        print("3. Shutdown / Reset may SERVER")       
        print("4. Xem man hinh hien thoi cua may SERVER")        
        print("5. Khoa / Bat phim nhan (keylogger) o may SERVER")
        print("6. Xoa files ; Copy files tu may SERVER")              
        print("0. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            app_process(client_socket)
        elif choice == '2':
            services_process(client_socket)   
        elif choice == '3':
            shutdown_reset(client_socket)
        elif choice == '4':            
            monitor(client_socket)
        elif choice == '5':
            bat_tat_key_logger(client_socket)
        elif choice == '6':
            del_copy(client_socket)                
        elif choice == '0':
            client_socket.close()
            print("Disconnected from server.")
            break
        else:
            print("Invalid choice, try again.")
            
if __name__ == "__main__":
    main()