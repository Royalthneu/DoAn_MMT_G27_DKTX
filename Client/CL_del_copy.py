import os
from Xuly_Chucnang.KetNoi_GiaoTiep import send_command, receive_response, replace_path


def del_copy(client_socket):
        
    while True:
        print("\n-- Xoa files ; Copy files tu may SERVER --")
        print("1. Xoa files")
        print("2. Copy files")   
        print("0. Quay lai menu chinh")
            
        choice = input("Dien lua chon: ")
    
        if choice == '1':
            file_path = input("Enter the full path of the file to delete on server: ")
            send_command(client_socket, f"DELETE_FILE {file_path}")        
            print(receive_response(client_socket))
        elif choice == '2':
            copy_file_from_server(client_socket)        
        elif choice == '0':
            break
        else:
            print("Chon khong dung. Chon lai.")
    

def copy_file_from_server(client_socket):
    # Nhập đường dẫn file từ server
    file_path = input("Dien duong dan file de copy tren Server: ").strip()
    replace_path(file_path)
    
    # Yêu cầu người dùng nhập vị trí dán file
    destination_folder = input("Dien duong dan folder de paste tren Client: ").strip()
    replace_path(file_path)
    
    # Kiểm tra nếu thư mục tồn tại
    if not os.path.exists(destination_folder):
        print("Folder tren may Client khong ton tai. Vui long thu lai.")
        return

    # Tạo tên file dựa trên đường dẫn từ server
    filename = os.path.basename(file_path)
    destination_path = os.path.join(destination_folder, filename)
        
    # Gửi yêu cầu copy file đến server với đường dẫn file đầy đủ
    send_command(client_socket, f"COPY_FILE {file_path}")
    
    # Nhận kích thước file
    file_size = int.from_bytes(client_socket.recv(4), byteorder='big')   
     
    if file_size == 0:
        # Nếu file co kich thuoc = 0 byte thi tạo một file rong
        with open(destination_path, 'wb') as f:
            pass  # Tạo file rỗng
        print(f"Dung luong file copy = 0. Tu dong tao file trong Folder {destination_path}.")
    else:
        # Nếu file có kích thước, sao chép dữ liệu xuống client
        with open(destination_path, 'wb') as f:
            data_received = 0
            while data_received < file_size:
                packet = client_socket.recv(4096)
                if not packet:
                    break
                f.write(packet)
                data_received += len(packet)
        print(f"Da copy file {filename} tu server den Folder {destination_path} cua Client.")
        
