
import os
import subprocess


def list_apps_running(client_socket):
    try:
        #list app bang tasklist
        output = subprocess.check_output("tasklist", encoding='utf-8') 
        client_socket.sendall(output.encode('utf-8')) 
    except Exception as e:
        error_msg = f"Loi: {e}"
        print(error_msg)
        client_socket.sendall(error_msg.encode('utf-8'))  

def start_app_by_path(client_socket, app_path):
    # Kiem tra duong dan app ton tai
    if not os.path.isfile(app_path):
        error_msg = f"Loi: Duong dan '{app_path}' khong ton tai.\n"
        client_socket.sendall(error_msg.encode())
        return    
    try:
        # start app
        subprocess.Popen([app_path], shell=True)
        success_msg = f"Khoi dong application: {app_path}\n"
        client_socket.sendall(success_msg.encode())
    except Exception as e:
        error_msg = f"Loi khoi dong application: {e}\n"
        client_socket.sendall(error_msg.encode())
        
    # Stop app bang PID
def stop_app(client_socket, pid):
    try:
        # Stop app bang taskkill
        subprocess.run(["taskkill", "/F", "/PID", str(pid)], check=True)
        success_msg = f"Stopped application with PID {pid}\n"
        client_socket.sendall(success_msg.encode())
    except Exception as e:
        error_msg = f"Error stopping application with PID {pid}: {e}\n"
        client_socket.sendall(error_msg.encode())