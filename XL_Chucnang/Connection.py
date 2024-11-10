import random
import socket
import subprocess

def check_ip_address_valid(ip):
    try:
        socket.inet_aton(ip)
        return True
    except socket.error:
        return False
    
def check_port_valid(port):
    if 0 < int(port) <= 65535:
        return True
    else:
        return False
    
def check_port_open(port):
    # Kiểm tra xem cổng đã được mở hay chưa.
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        return s.connect_ex(('localhost', port)) == 0

def open_port(port):
    # Mở một cổng bằng PowerShell.
    try:
        command = f'New-NetFirewallRule -DisplayName "Open Port {port}" -Direction Inbound -LocalPort {port} -Protocol TCP -Action Allow'
        result = subprocess.run(
            ["powershell", "-Command", command],
            capture_output=True, text=True
        )
        if result.returncode == 0:
            print(f"Cổng {port} đã được mở thành công.")
        else:
            print(f"Lỗi khi mở cổng {port}:", result.stderr)
    except Exception as e:
        print("Lỗi khi thực thi lệnh PowerShell:", e)

def find_and_open_port():
    #Tìm một cổng bất kỳ từ 50000 đến 60000 và mở nó nếu cần.
    while True:
        # Chọn ngẫu nhiên một cổng trong khoảng 50000 - 60000
        port = random.randint(50000, 60000)
        
        # Kiểm tra xem cổng đã được mở chưa
        if check_port_open(port):
            print(f"Cổng {port} đã được mở.")
            break
        else:
            # Nếu cổng chưa mở, hỏi người dùng có muốn mở không
            response = input(f"Cổng {port} chưa mở. Bạn có muốn mở cổng {port} không? (y/n): ")
            if response.lower() == 'y':
                open_port(port)
                break
            else:
                print(f"Cổng {port} sẽ không được mở. Thử cổng khác...")

    # Trả về cổng đã mở
    return port

def input_ip_port(prompt_ip, prompt_port):
    while True:
        ip = input(prompt_ip)
        if not check_ip_address_valid(ip):
            print("IP address không hợp lệ. Vui lòng nhập lại.")
            continue
        
        try:
            port = int(input(prompt_port))
            if not check_port_valid(port):
                print("Port phải là số và nằm trong khoảng từ 1 đến 65535.")
                continue
        except ValueError:
            print("Port phải là dạng số nguyên.")
            continue
        
        return ip, port

# def verify_server_connection(server_ip, port):
#     # Kiểm tra xem server có chạy hay không
#     if not is_server_running(server_ip, port):
#         print(f"Server tại {server_ip}:{port} không thể kết nối.")
#         server_ip, port = input_ip_port("Nhập lại IP của server: ", "Nhập lại port của server: ")
        
#         # Kiểm tra lại kết nối với server sau khi nhập lại
#         if is_server_running(server_ip, port):
#             update_config(server_ip, port)
#             print(f"Đã kết nối thành công đến server {server_ip}:{port}!")
#         else:
#             print(f"Server tại {server_ip}:{port} vẫn không thể kết nối.")
#     else:
#         print(f"Đã kết nối thành công với server {server_ip}:{port}!")

# def is_server_running(server_ip, port):
#     try:
#         client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#         client_socket.settimeout(3)  # Đặt timeout kết nối là 3 giây
#         client_socket.connect((server_ip, port))
#         client_socket.close()
#         return True
#     except socket.error:
#         return False

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
         