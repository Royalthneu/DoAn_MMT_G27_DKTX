import socket
import sys
from tkinter import Tk, Label
from PIL import Image, ImageTk
import io
from module_support import send_command

def monitor(client_socket):
    # Tạo cửa sổ Tkinter
    root = Tk()
    root.title("Xem màn hình Client thời gian thực")
    root.geometry("800x600")

    label = Label(root)
    label.pack(fill="both", expand=True)

    # Gửi lệnh yêu cầu bật chức năng xem màn hình
    send_command(client_socket, "VIEW_MONITOR")

    # Cập nhật màn hình mỗi khi nhận được hình ảnh từ server
    def update_screen():
        try:
            # Đọc kích thước dữ liệu ảnh (4 byte đầu tiên)
            data_length = int.from_bytes(client_socket.recv(4), byteorder="big")

            # Đọc dữ liệu ảnh theo kích thước đã nhận
            screen_data = b""
            while len(screen_data) < data_length:
                packet = client_socket.recv(data_length - len(screen_data))
                if not packet:
                    return
                screen_data += packet

            # Chuyển đổi dữ liệu ảnh thành hình ảnh Pillow
            screen_image = Image.open(io.BytesIO(screen_data))
            screen_image = screen_image.resize((800, 600))  # Điều chỉnh kích thước nếu cần

            # Chuyển đổi ảnh thành định dạng có thể hiển thị trong Tkinter
            photo = ImageTk.PhotoImage(screen_image)
            label.config(image=photo)
            label.image = photo  # Cần giữ tham chiếu đến ảnh để tránh bị mất

        except Exception as e:
            print("Error updating screen:", e)
        
        # Lặp lại sau 50ms (~20 FPS)
        root.after(50, update_screen)

    # Bắt đầu cập nhật màn hình
    update_screen()

    # Khởi động vòng lặp sự kiện Tkinter
    root.mainloop()

    # Đóng kết nối socket khi tắt ứng dụng.
    client_socket.close()

if __name__ == "__main__":
    # Kết nối đến server và bắt đầu theo dõi màn hình
    server_ip = "127.0.0.1"  # Thay thế IP và Port nếu cần
    server_port = 8080

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_ip, server_port))

    monitor(client_socket)
