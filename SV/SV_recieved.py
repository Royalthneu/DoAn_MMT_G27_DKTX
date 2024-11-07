from SV_app_process import list_apps_running, start_app_by_path, stop_app


BUFFER_SIZE = 1024

def handle_client(client_socket):
    """Xử lý các lệnh từ client."""
    try:
        while True:
            buffer = client_socket.recv(BUFFER_SIZE).decode()
            if not buffer:
                print("Client disconnected or error occurred.")
                break
            print(f"Received command: {buffer}")
           
            # List / Start / Stop các Applications đang chạy SERVER
            if buffer.startswith("LIST_APPS_RUNNING"):
                list_apps_running(client_socket) 
            elif buffer.startswith("START_APP_BY_PATH"):
                app_path = buffer.split(" ",1)[1]
                start_app_by_path(client_socket, app_path)                 
            elif buffer.startswith("STOP_APP"):
                pid = int(buffer.split()[1])
                stop_app(client_socket, pid)
                
            # List / Start / Stop Services (Processes) đang chạy SERVER
            elif buffer.startswith("LIST_SERVICE_RUNNING"):
                list_running_services(client_socket)           
            elif buffer.startswith("START_SERVICE"):
                service_name = buffer.split(" ",1)[1]
                start_service(client_socket, service_name)
            elif buffer.startswith("STOP_SERVICE"):
                service_name = buffer.split(" ",1)[1]
                stop_service(client_socket, service_name) 
            
            # Shutdown / Reset máy SERVER
            elif buffer == "SHUTDOWN_SERVER":
                shutdown_server(client_socket)
            elif buffer == "RESET_SERVER":
                reset_server(client_socket)
            
            
            # Xem màn hình hiện thời của máy SERVER
            elif buffer.startswith("SCREEN_CAPTURING"):
                screen_capturing(client_socket)
                
            # Khóa / Bắt phím nhấn (keylogger) ở máy SERVER
            elif buffer.startswith("START_KEY_LOGGER"):
                print("Starting keylogger...")                
                start_keylogger(client_socket)
            elif buffer == "STOP_KEY_LOGGER":
                print("Keylogger stopped")  
                        
            # Xóa files ; Copy files từ máy SERVER
            elif buffer.startswith("DELETE_FILE"):
                file_path = buffer.split(" ", 1)[1]  # Lấy đường dẫn file từ lệnh
                delete_file(client_socket, file_path)
            elif buffer.startswith("COPY_FILE"):
                file_path = buffer.split(" ", 1)[1]  # Lấy đường dẫn file từ lệnh
                copy_file(client_socket, file_path)       
                
            elif buffer.startswith("GO BACK MENU LIST"):
                print("Client requested to return to menu.")                
                break
            else:
                print("Unknown command received.")

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        client_socket.close()
        print("Client connection closed.")
