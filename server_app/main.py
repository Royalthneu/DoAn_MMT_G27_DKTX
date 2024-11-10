# main.py

from SV_controller import SV_Controller

if __name__ == "__main__":
    # Khởi tạo controller và chạy ứng dụng
    server_controller = SV_Controller()
    server_controller.view.run()
