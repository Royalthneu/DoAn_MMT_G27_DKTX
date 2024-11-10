# Sử dụng file config.json để lưu ip và port
import json
import os

# Kiểm tra xem file JSON có tồn tại không
def check_config_file(CONFIG_FILE):
    return os.path.exists(str(CONFIG_FILE))

# Đọc cấu hình từ file JSON
def read_config(CONFIG_FILE):
    try:
        with open(str(CONFIG_FILE), "r") as file:
            config = json.load(file)
        return config.get("server_ip"), config.get("port")
    except json.JSONDecodeError:
        print("File cấu hình không hợp lệ. Vui lòng kiểm tra nội dung file.")
        return None, None
    except FileNotFoundError:
        print("File cấu hình không tồn tại.")
        return None, None

# Ghi cấu hình mới vào file JSON
def write_config(CONFIG_FILE, server_ip, port):
    config = {
        "server_ip": server_ip,
        "port": port
    }
    with open(str(CONFIG_FILE), "w") as file:
        json.dump(config, file, indent=4)
    print(f"Configuration saved: IP = {server_ip}, Port = {port}")


# Cập nhật cấu hình trong file JSON
def update_config(CONFIG_FILE, server_ip, port):
    if check_config_file(CONFIG_FILE):
        with open(CONFIG_FILE, "r") as file:
            config = json.load(file)
        # Cập nhật giá trị mới
        config["server_ip"] = server_ip
        config["port"] = port
        with open(CONFIG_FILE, "w") as file:
            json.dump(config, file, indent=4)
        print(f" configuration updated: IP = {server_ip}, Port = {port}")
    else:
        print("Configuration file does not exist.")
        create_file = input("Would you like to create a new configuration file? (y/n): ").strip().lower()
        if create_file == "y":
            write_config(server_ip, port)
            print(f"New configuration file created with IP = {server_ip}, Port = {port}")
        else:
            print("Exiting program.")
            exit()  # Thoát chương trình nếu người dùng không muốn tạo file
