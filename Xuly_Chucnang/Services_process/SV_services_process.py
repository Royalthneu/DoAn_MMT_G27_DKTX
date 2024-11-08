from XuLy_KetNoi_GiaoTiep import run_powershell_command, send_message, receive_response

def server_process(client_socket):    
    while True:     
        try:
            while True:
                command = receive_response(client_socket).strip()
                
                if command == "LIST_SERVICES_RUNNING":
                    list_running_services(client_socket)
                elif command.startswith("START_SERVICE"):
                    service_name = command.split(" ", 1)[1]
                    start_service(client_socket, service_name)
                elif command.startswith("STOP_SERVICE"):
                    service_name = command.split(" ", 1)[1]
                    stop_service(client_socket, service_name)                
                else:
                    send_message(client_socket, "Lenh khong hop le.\n")                    
        finally:
            client_socket.close()
            print("Ket noi voi may Clien da dong.")            

def list_running_services(client_socket):
    #L iệt kê các dịch vụ đang chạy
    command = "Get-Service | Where-Object { $_.Status -eq 'Running' } | Format-Table -HideTableHeaders -Property Name,DisplayName"
    output = run_powershell_command(command)
    send_message(client_socket, output if output else "Khong co dich vu nao dang chay.\n")

def start_service(client_socket, service_name):
    # Khởi động dịch vụ
    command = f"Start-Process sc.exe -ArgumentList 'start', '{service_name}' -Verb runAs"
    output = run_powershell_command(command)
    if output:
        send_message(client_socket, f"Loi start dich vu '{service_name}': {output}")
    else:
        send_message(client_socket, f"Dich vu '{service_name}' da duoc yeu cau start.\n")

def stop_service(client_socket, service_name):
    # Dừng dịch vụ
    command = f"Start-Process sc.exe -ArgumentList 'stop', '{service_name}' -Verb runAs"
    output = run_powershell_command(command)
    if output:
        send_message(client_socket, f"Loi khi dung dich vu '{service_name}': {output}")
    else:
        send_message(client_socket, f"Dich vu '{service_name}' da duoc yeu cau dung.\n")

