import json
import os

# Kiểm tra xem file JSON có tồn tại không
def check_config_file(CONFIG_FILE):
    return os.path.exists(str(CONFIG_FILE))

# Đọc cấu hình từ file JSON cho server
def read_config_server(CONFIG_FILE):
    try:
        with open(str(CONFIG_FILE), "r") as file:
            config = json.load(file)
        return config.get("server_ip"), config.get("server_port")
    except json.JSONDecodeError:
        print("File cấu hình không hợp lệ. Vui lòng kiểm tra nội dung file.")
        return None, None
    except FileNotFoundError:
        print("File cấu hình không tồn tại.")
        return None, None
    
# Đọc cấu hình từ file JSON cho client
def read_config_client(CONFIG_FILE):
    try:
        with open(str(CONFIG_FILE), "r") as file:
            config = json.load(file)
        return config.get("client_ip"), config.get("client_port")
    except json.JSONDecodeError:
        print("File cấu hình không hợp lệ. Vui lòng kiểm tra nội dung file.")
        return None, None
    except FileNotFoundError:
        print("File cấu hình không tồn tại.")
        return None, None

# Ghi cấu hình mới vào file JSON (bao gồm cả server và client)
def write_config(CONFIG_FILE, server_ip, server_port, client_ip, client_port):
    config = {
        "server_ip": server_ip,
        "server_port": server_port,
        "client_ip": client_ip,
        "client_port": client_port
    }
    with open(str(CONFIG_FILE), "w") as file:
        json.dump(config, file, indent=4)
    print(f"Configuration saved: Server IP = {server_ip}, Server Port = {server_port}, Client IP = {client_ip}, Client Port = {client_port}")

# Cập nhật cấu hình trong file JSON (bao gồm cả server và client)
def update_config(CONFIG_FILE, server_ip=None, server_port=None, client_ip=None, client_port=None):
    if check_config_file(CONFIG_FILE):
        with open(CONFIG_FILE, "r") as file:
            config = json.load(file)
        # Cập nhật các giá trị mới nếu chúng được truyền vào
        if server_ip is not None:
            config["server_ip"] = server_ip
        if server_port is not None:
            config["server_port"] = server_port
        if client_ip is not None:
            config["client_ip"] = client_ip
        if client_port is not None:
            config["client_port"] = client_port
        with open(CONFIG_FILE, "w") as file:
            json.dump(config, file, indent=4)
        print(f"Configuration updated: Server IP = {config['server_ip']}, Server Port = {config['server_port']}, Client IP = {config['client_ip']}, Client Port = {config['client_port']}")
    else:
        print("Configuration file does not exist.")
        create_file = input("Would you like to create a new configuration file? (y/n): ").strip().lower()
        if create_file == "y":
            write_config(CONFIG_FILE, server_ip, server_port, client_ip, client_port)
            print(f"New configuration file created with Server IP = {server_ip}, Server Port = {server_port}, Client IP = {client_ip}, Client Port = {client_port}")
        else:
            print("Exiting program.")
            exit()  # Thoát chương trình nếu người dùng không muốn tạo file
