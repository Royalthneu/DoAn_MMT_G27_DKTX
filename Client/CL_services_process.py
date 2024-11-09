import socket
from XL_Chucnang.CRUDConfig import read_config
from XL_Chucnang.Connection import receive_response_65535, send_command, receive_response


def services_process(client_socket):   
    while True:
        print("\n-- List / Start / Stop cac Services dang chay SERVER --")
        print("1. List Services dang chay")
        print("2. Stop Service theo Ten")        
        print("3. Start Service theo ten")       
        print("0. Quay lai menu chinh")
            
        choice = input("Dien lua chon: ")
    
        if choice == '1':
            list_running_services(client_socket)
        elif choice == '2':
            list_running_services(client_socket)
            stop_service(client_socket)
        elif choice == '3':
            start_service(client_socket)
        elif choice == '0':
            break
        else:
            print("Chon khong dung. Chon lai.")

def list_running_services(client_socket):
    send_command(client_socket, "LIST_SERVICES_RUNNING")   
    print("Cac Services dang chay:\n" + receive_response_65535(client_socket))

def start_service(client_socket):
    service_name = input("Nhap ten service muon start: ")
    send_command(client_socket, f"START_SERVICE {service_name}")  
    print(receive_response(client_socket) )

def stop_service(client_socket):
    service_name = input("Nhap ten service muon stop: ")
    send_command(client_socket, f"STOP_SERVICE {service_name}")   
    print(receive_response(client_socket))

if __name__ == "__main__":    
    server_ip, port = read_config()
    if server_ip is None or port is None:
        print("Khong the lay IP va Port từ file config.json. Vui long kiem tra file config.json.")
    else:        
        try:
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client_socket.connect((server_ip, port))  # Dùng IP và port từ file config.json
            services_process(client_socket)
            client_socket.close()
        except socket.error as e:
            print(f"Connection failed: {e}. Please check if the IP and Port in config.json are correct.")

