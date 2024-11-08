import os
from CRUD import send_command

def delete_file(client_socket, file_path):
    # Xóa file tại đường dẫn được chỉ định trên server.
    if os.path.exists(file_path):
        try:
            os.remove(file_path)
            response = "Xoa file thanh cong."
        except Exception as e:
            response = f"Loi: xoa file: {e}"
    else:
        response = "File khong ton tai tren may Server."  
          
    send_command(client_socket, response)

def copy_file(client_socket, file_path):
    #Sao chép file tại đường dẫn được chỉ định trên server và gửi tới client.
    if os.path.exists(file_path):        
        # Lấy kích thước file
        file_size = os.path.getsize(file_path)
        
        # Gửi kích thước file đến client
        client_socket.sendall(file_size.to_bytes(4, byteorder='big'))
        
        # Gửi file tới client
        with open(file_path, 'rb') as f:
            while (chunk := f.read(4096)):
                client_socket.sendall(chunk)
    else:
        # Nếu file không tồn tại, gửi kích thước 0 để báo lỗi
        client_socket.sendall((0).to_bytes(4, byteorder='big'))

