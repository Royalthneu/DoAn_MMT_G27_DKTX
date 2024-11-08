import socket
import cv2
import numpy as np
import struct
from XuLyFileConfig import read_config

# Hàm nhận đủ dữ liệu từ client
def receive_all(sock, count):
    buf = b''
    while count:
        newbuf = sock.recv(count)
        if not newbuf: return None
        buf += newbuf
        count -= len(newbuf)
    return buf

# Hàm gửi ảnh dưới dạng byte stream
def send_frame(client_socket, frame):
    # Nén ảnh và chuyển thành byte stream
    encoded_frame = cv2.imencode('.jpg', frame)[1].tobytes()
    message_size = struct.pack(">L", len(encoded_frame))  # Lưu kích thước ảnh
    client_socket.sendall(message_size)  # Gửi kích thước ảnh
    client_socket.sendall(encoded_frame)  # Gửi dữ liệu ảnh

# Hàm hiển thị màn hình của server
def monitor(client_socket):
    # Lấy IP và cổng từ config
    server_ip, port = read_config()
    
    # Tạo socket server
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((server_ip, port))
    server_socket.listen(1)
    print(f"Server is listening at {server_ip}:{port}")

    # Chấp nhận kết nối từ client
    client_socket, addr = server_socket.accept()
    print(f"Connection from: {addr}")

    try:
        while True:
            # Chụp ảnh màn hình của server (ở đây tôi giả sử bạn đã có hàm chụp màn hình)
            screenshot = np.array(cv2.imread('screenshot.png'))  # Thay đổi theo cách bạn chụp màn hình
            send_frame(client_socket, screenshot)

            # Delay (có thể điều chỉnh để không quá nhanh hoặc quá chậm)
            cv2.waitKey(100)

    except Exception as e:
        print(f"Unexpected error: {e}")
    finally:
        client_socket.close()
        server_socket.close()

