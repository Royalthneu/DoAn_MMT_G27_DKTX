import sys
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import QTimer
from PIL import Image
import io
from module_support import send_command

def monitor(client_socket):
    app = QApplication(sys.argv)
    window = QMainWindow()
    window.setWindowTitle("Xem man hinh Client thoi gian thuc 50FPS")
    window.setGeometry(100, 100, 800, 600)
    
    label = QLabel(window)
    label.setGeometry(0, 0, 800, 600)
       
    # Gửi lệnh yêu cầu bật chức năng xem màn hình
    send_command(client_socket, "VIEW_MONITOR")
    
    # Thiết lập timer để nhận dữ liệu hình ảnh liên tục
    timer = QTimer()
    timer.timeout.connect(lambda: update_screen(client_socket, label))
    timer.start(10)  # Tốc độ cập nhật khoảng 100 FPS
    
    window.show()
    sys.exit(app.exec_())

    # Đóng kết nối socket khi tắt ứng dụng.
    client_socket.close()

def update_screen(client_socket, label):
    #Cập nhật màn hình từ dữ liệu nhận được từ server
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
        
        # Chuyển đổi dữ liệu ảnh thành QPixmap và hiển thị
        screen_image = Image.open(io.BytesIO(screen_data))
        screen_image = screen_image.resize((800, 600))  # Điều chỉnh kích thước nếu cần
        
        qimage = QImage(screen_image.tobytes(), screen_image.width, screen_image.height, QImage.Format_RGB888)
        pixmap = QPixmap.fromImage(qimage)
        label.setPixmap(pixmap)
    except Exception as e:
        print("Error updating screen:", e)

