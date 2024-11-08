import subprocess
from CRUD import run_powershell_command, send_message

def shutdown_server(client_socket):                      
    try:  
        # Sử dụng PowerShell để shutndown lại máy tính      
        recv_command = "Stop-Computer -Force"
        run_powershell_command(recv_command)    
        send_message(client_socket, "Server is shutting down...")
    except Exception as e:
        send_message(client_socket, f"Khong the shutdown server: {e}") 
     
def reset_server(client_socket):                    
    try:      
        # Sử dụng PowerShell để khởi động lại máy tính
        recv_command = "Restart-Computer -Force"
        run_powershell_command(recv_command)      
        send_message(client_socket, "Server is reset...")
    except Exception as e:
        send_message(client_socket, f"Khong the reset server: {e}")        
       

