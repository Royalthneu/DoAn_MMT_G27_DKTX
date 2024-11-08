import socket
import cv2
import numpy as np
import struct
from XuLyFileConfig import read_config

# Hàm nhận đủ dữ liệu từ server
def receive_all(sock, count):
    buf = b''
    while count:
        newbuf = sock.recv(count)
        if not newbuf: return None
        buf += newbuf
        count -= len(newbuf)
    return buf

# Hàm hiển thị màn hình từ server
def monitor(client_socket):
    cv2.namedWindow('Received', cv2.WINDOW_NORMAL)  # Khởi tạo cửa sổ hiển thị ảnh

    try:
        while True:
            # Nhận kích thước dữ liệu ảnh từ server
            message_size = receive_all(client_socket, struct.calcsize(">L"))
            if not message_size:
                break
            message_size = struct.unpack(">L", message_size)[0]

            # Nhận dữ liệu ảnh từ server
            frame_data = receive_all(client_socket, message_size)
            if not frame_data:
                break

            # Chuyển đổi dữ liệu ảnh từ byte thành ảnh
            frame = np.frombuffer(frame_data, dtype=np.uint8)
            frame = cv2.imdecode(frame, cv2.IMREAD_COLOR)
            if frame is None:
                print("Error decoding frame.")
                continue

            # Hiển thị ảnh nhận được từ server
            cv2.imshow('Received', frame)

            # Đảm bảo giao diện không bị "Not responding"
            key = cv2.waitKey(1) & 0xFF
            if key == ord('q'):
                break

    except Exception as e:
        print(f"Unexpected error: {e}")
    finally:
        cv2.destroyAllWindows()
        client_socket.close()

