from Check import ip_port
import socket

def main():
    while True:
        server_ip = input("Enter the server IP address: ") 
        
        if not ip_port.check_ip_address_valid(server_ip):
            print("Invalid IP address. Please try again.")
            continue
        
        try:
            port = int(input("Enter the server port: "))
        except ValueError:
            print("Port must be a number.")
            continue
      
        if not ip_port.check_port_valid(port):
            print("Invalid port. Please enter a port between 1 and 65535.")
            continue

        try:
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # client_socket.settimeout(3) # Set thời gian chời kết nối ở đây là 3s  
            client_socket.connect((server_ip, port))
            print("Connected to the server successfully!")
            break
        except socket.error as e:
            print(f"Connection failed: {e}. Please check IP and Port were opened.")
            client_socket.close()
            continue

    while True:
        print("\n--- MAIN MENU ---")
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
            keylogger(client_socket)
        elif choice == '6':
            del_copy(client_socket)                
        elif choice == '0':
            client_socket.close()
            print("Disconnected from server.")
            break
        else:
            print("Invalid choice, try again.")
