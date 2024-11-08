import XuLy_ChucNang
import XuLy_KetNoi_GiaoTiep
import socket

from XuLyFileConfig import update_config
import XuLy_ChucNang.App_process.CL_app_process
import XuLy_ChucNang.Services_process.CL_services_process
import XuLy_ChucNang.Shutdown_reset.CL_shutdown_reset
import XuLy_ChucNang.Monitor.CL_monitor
import XuLy_ChucNang.Keylogger.CL_keylogger
import XuLy_ChucNang.Del_copy.CL_del_copy


def main():
    while True:
        server_ip = input("Dien dia chi IP cua Server: ")
        if not XuLy_KetNoi_GiaoTiep.check_ip_address_valid(server_ip):
            print("IP khong hop le. Vui long dien lai.")
            continue
        
        port = int(input("Dien so port: "))
        if not XuLy_KetNoi_GiaoTiep.check_port_valid(port):
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
            XuLy_ChucNang.App_process.CL_app_process.app_process(client_socket)
        elif choice == '2':
           XuLy_ChucNang.Services_process.CL_services_process.services_process(client_socket)   
        elif choice == '3':
            XuLy_ChucNang.Shutdown_reset.CL_shutdown_reset.shutdown_reset(client_socket)
        elif choice == '4':            
            XuLy_ChucNang.Monitor.CL_monitor.monitor(client_socket)
        elif choice == '5':
            XuLy_ChucNang.Keylogger.CL_keylogger.bat_tat_key_logger(client_socket)
        elif choice == '6':
            XuLy_ChucNang.Del_copy.CL_del_copy.del_copy(client_socket)                
        elif choice == '0':
            client_socket.close()
            print("Disconnected from server.")
            break
        else:
            print("Invalid choice, try again.")
            
if __name__ == "__main__":
    main()