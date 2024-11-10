import socket
from XL_Chucnang.CRUDConfig import read_config_server
from XL_Chucnang.Connection import receive_response_65535, send_command, receive_response
from tkinter import messagebox, simpledialog

def initialize_socket(config_path):
    server_ip, server_port = read_config_server(config_path)
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_ip, server_port))
    return client_socket

def close_socket(client_socket):
    client_socket.close()

def list_apps_running(client_socket, tree_app):
    send_command(client_socket, "LIST_APPS_RUNNING")
    running_apps = receive_response_65535(client_socket)
    
    # Clear current tree contents
    for row in tree_app.get_children():
        tree_app.delete(row)

    if not running_apps.strip():
        messagebox.showinfo("Info", "No applications are currently running.")
    else:
        for line in running_apps.strip().splitlines():
            pid, app_name = line.split(": ", 1)
            tree_app.insert("", "end", text=pid, values=(app_name,))

def stop_app_running_by_PID(client_socket, tree_app):
    selected_item = tree_app.selection()
    if selected_item:
        pid = tree_app.item(selected_item)["text"]
        send_command(client_socket, f"STOP_APP {pid}")
        response = receive_response(client_socket)
        if "not found" in response.lower() or "already stopped" in response.lower():
            messagebox.showerror("Error", "App is not running or cannot be stopped.")
        else:
            messagebox.showinfo("Info", response)
            list_apps_running(client_socket, tree_app)
    else:
        messagebox.showwarning("Warning", "Please select an application to stop.")

def start_app_by_path(client_socket, tree_app):
    app_path = simpledialog.askstring("Start Application", "Enter the application path:")
    if app_path:
        send_command(client_socket, f"START_APP_BY_PATH {app_path}")
        response = receive_response(client_socket)
        if "not allowed" in response.lower() or "not found" in response.lower():
            messagebox.showerror("Error", f"Cannot start app at path '{app_path}'. Check path or permissions.")
        else:
            messagebox.showinfo("Info", response)
            list_apps_running(client_socket, tree_app)
