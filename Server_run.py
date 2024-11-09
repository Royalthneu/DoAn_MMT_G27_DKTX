import socket
import threading
from XL_Chucnang.CRUDConfig import read_config
import XL_Chucnang.Connection as Connection
import Server.SV_app_process
import Server.SV_services_process
import Server.SV_shutdown_reset
import Server.SV_monitor
import Server.SV_keylogger
import Server.SV_del_copy
from vidstream import StreamingServer

def main():
    server_ip = socket.gethostbyname(socket.gethostname())
    port = 8081
    if Connection.check_port_open(port):
        print(f"\nCổng {port} đã được mở.")
    else:
        # Nếu cổng chưa mở, hỏi người dùng có muốn mở không
        response = input(f"Cổng {port} chưa mở. Bạn có muốn mở cổng {port} không? (y/n): ")
        if response.lower() == 'y':
            Connection.open_port(port)
        else:
            print(f"Cổng {port} sẽ không được mở. Thoát chương trình.")
            return
        
    if Connection.check_ip_address_valid(server_ip) and Connection.check_port_valid(port):
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
        
    server_socket_stream = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket_stream.bind((server_ip, 9999))
    server_socket_stream.listen(1)     
    
    try:
        while True:
            # Chấp nhận kết nối từ client
            client_socket_stream, addr = server_socket_stream.accept() 
            print(f"Client connected from {addr}")

            # Tạo một thread mới để xử lý client
            client_thread_stream = threading.Thread(target=start_stream, args=(client_socket_stream,))
            client_thread_stream.start()    
            
    except KeyboardInterrupt:
        print("Server is shutting down...")
    finally:
        server_socket.close()
        print("Server stopped.")  
      
def handle_client(client_socket):
    #Xử lý các lệnh từ client.
    try:
        while True:       
            buffer = client_socket.recv(4096).decode()              
            if not buffer:
                print("Loi ket noi den Client hoac ket noi da dong.")
                break
            print(f"Lenh da nhan: {buffer}")
           
            # List / Start / Stop các Applications đang chạy SERVER
            if buffer.startswith("LIST_APPS_RUNNING"):
                Server.SV_app_process.list_apps_running(client_socket) 
            elif buffer.startswith("START_APP_BY_PATH"):
                app_path = buffer.split(" ",1)[1]
                Server.SV_app_process.start_app_by_path(client_socket, app_path)                 
            elif buffer.startswith("STOP_APP"):
                pid = int(buffer.split()[1])
                Server.SV_app_process.stop_app(client_socket, pid)
                
            # List / Start / Stop Services (Processes) đang chạy SERVER
            elif buffer.startswith("LIST_SERVICES_RUNNING"):
                Server.SV_services_process.list_running_services(client_socket)           
            elif buffer.startswith("START_SERVICE"):
                service_name = buffer.split(" ",1)[1]
                Server.SV_services_process.start_service(client_socket, service_name)
            elif buffer.startswith("STOP_SERVICE"):
                service_name = buffer.split(" ",1)[1]
                Server.SV_services_process.stop_service(client_socket, service_name) 
            
            # Shutdown / Reset máy SERVER
            elif buffer == "SHUTDOWN_SERVER":
                Server.SV_shutdown_reset.shutdown_server(client_socket)
            elif buffer == "RESET_SERVER":
                Server.SV_shutdown_reset.reset_server(client_socket)
            
            
            # Xem màn hình hiện thời của máy SERVER
            elif buffer.startswith("VIEW_MONITOR"):
                start_stream()
                
            # Khóa / Bắt phím nhấn (keylogger) ở máy SERVER
            elif buffer.startswith("START_KEYLOGGER"):
                print("Starting keylogger...")                
                Server.SV_keylogger.start_keylogger(client_socket)
            elif buffer == "STOP_KEYLOGGER":
                print("Keylogger stopped")  
                        
            # Xóa files ; Copy files từ máy SERVER
            elif buffer.startswith("DELETE_FILE"):
                file_path = buffer.split(" ", 1)[1]  # Lấy đường dẫn file từ lệnh
                Server.SV_del_copy.delete_file(client_socket, file_path)
            elif buffer.startswith("COPY_FILE"):
                file_path = buffer.split(" ", 1)[1]  # Lấy đường dẫn file từ lệnh
                Server.SV_del_copy.copy_file(client_socket, file_path)
            else:
                print("Khong biet lenh vua nhan tu may Client.")

    except Exception as e:
        print(f"Loi khong mong muon: {e}")
    finally:
        client_socket.close()
        print("Dong ket noi voi may Client.")

def start_stream():   
    try:
        server_ip, port = read_config() 
        server = StreamingServer(server_ip, port)
        server.start_server()
        print(f"Video streaming server started at {server_ip}:{port}")
        
        while input("") != 'STOP':
            continue
        
        #When You Are Done
        #server.stop_server()  
    except Exception as e:
        print(f"Failed to start video stream server: {e}")
        

if __name__ == "__main__":
    main()