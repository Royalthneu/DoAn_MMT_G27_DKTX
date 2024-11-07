import pyautogui
import io
import time
import socket
from module_support import receive_response, send_message

def capture_screen():
    # Chụp ảnh màn hình và trả về dữ liệu dưới dạng byte.
    screenshot = pyautogui.screenshot()
    byte_io = io.BytesIO()
    screenshot.save(byte_io, format="JPEG", quality=50)  # Giảm chất lượng để tăng tốc độ
    return byte_io.getvalue()

def monitor(client_socket):
    command = receive_response(client_socket).strip()
    if command == "VIEW_MONITOR":
        try:
            while True:
                screen_data = capture_screen()
                data_length = len(screen_data).to_bytes(4, byteorder="big")

                # Gửi kích thước dữ liệu trước, sau đó gửi dữ liệu ảnh
                client_socket.sendall(data_length + screen_data)
                time.sleep(0.05)  # Gửi hình ảnh mới mỗi 200ms (20 FPS)
        finally:
            client_socket.close()

if __name__ == "__main__":
    # Thiết lập server
    server_ip = "0.0.0.0"
    server_port = 8080

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((server_ip, server_port))
    server_socket.listen(1)
    print(f"Server đang lắng nghe tại {server_ip}:{server_port}")

    client_socket, addr = server_socket.accept()
    print(f"Client kết nối từ {addr}")

    monitor(client_socket)
