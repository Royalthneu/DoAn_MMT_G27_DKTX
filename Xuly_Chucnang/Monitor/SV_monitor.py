import pyautogui
import io
import time
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
                time.sleep(0.02)  # Gửi hình ảnh mới mỗi 50ms (50 FPS)
        finally:
            client_socket.close()                  
    else:
        send_message(client_socket, "Lenh khong hop le.\n")      
    

if __name__ == "__main__":
    monitor()
