import json
import os
import subprocess

def send_command(socket, command):
    #Gửi câu lệnh từ client/server đến server/client.
    socket.sendall(command.encode())
    
def send_command_utf8(socket, command):
    #Gửi câu lệnh từ client/server đến server/client.
    socket.sendall(command.encode("utf-8"))

def receive_response(socket, buffer_size=4096):
    #Nhận phản hồi từ server/client.
    return socket.recv(buffer_size).decode()

def receive_response_65535(socket, buffer_size=65535):
    #Nhận phản hồi từ server/client.
    return socket.recv(buffer_size).decode()


def receive_response_utf8(socket, buffer_size=4096):
    #Nhận phản hồi từ server/client.
    return socket.recv(buffer_size).decode("utf-8")

def replace_path(file_path):
    if '\\\\' in file_path:
         file_path = file_path.replace("\\\\", "\\")  # Thay thế '\\' thành '\'
     
def send_message(client_socket, message):
    #Hàm gửi thông báo đến client
    client_socket.sendall(message.encode())
    
def send_error_message(client_socket, message):
    #Hàm gửi thông báo lỗi
    send_command_utf8(client_socket, f"Loi: {message}\n")

def send_success_message(client_socket, message):
    #Hàm gửi thông báo thành công
    send_command_utf8(client_socket, f"{message}\n")
    
def run_powershell_command(command):
    """Hàm thực thi lệnh PowerShell và trả về kết quả hoặc lỗi"""
    try:
        result = subprocess.run(
            ["powershell", "-Command", command],
            check=True, capture_output=True, text=True
        )
        return result.stdout
    except subprocess.CalledProcessError as e:
        return e.stderr
         

# Sử dụng file config.json để lưu ip và port
CONFIG_FILE = "config.json"

# Kiểm tra xem file JSON có tồn tại không
def check_config_file():
    return os.path.exists(CONFIG_FILE)

# Đọc cấu hình từ file JSON
def read_config():
    try:
        with open("config.json", "r") as file:
            config = json.load(file)
        return config.get("server_ip"), config.get("port")
    except json.JSONDecodeError:
        print("File cấu hình không hợp lệ. Vui lòng kiểm tra nội dung file.")
        return None, None
    except FileNotFoundError:
        print("File cấu hình không tồn tại.")
        return None, None

# Ghi cấu hình mới vào file JSON
def write_config(server_ip, port):
    config = {
        "server_ip": server_ip,
        "port": port
    }
    with open(CONFIG_FILE, "w") as file:
        json.dump(config, file, indent=4)
    print(f"Configuration saved: IP = {server_ip}, Port = {port}")


# Cập nhật cấu hình trong file JSON
def update_config(server_ip, port):
    if check_config_file():
        with open(CONFIG_FILE, "r") as file:
            config = json.load(file)
        # Cập nhật giá trị mới
        config["server_ip"] = server_ip
        config["port"] = port
        with open(CONFIG_FILE, "w") as file:
            json.dump(config, file, indent=4)
        print(f"Configuration updated: IP = {server_ip}, Port = {port}")
    else:
        print("Configuration file does not exist.")
        create_file = input("Would you like to create a new configuration file? (y/n): ").strip().lower()
        if create_file == "y":
            write_config(server_ip, port)
            print(f"New configuration file created with IP = {server_ip}, Port = {port}")
        else:
            print("Exiting program.")
            exit()  # Thoát chương trình nếu người dùng không muốn tạo file
