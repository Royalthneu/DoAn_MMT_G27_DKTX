# main.py
import socket
import tkinter as tk

from CL_view import CL_View
from CL_model import CL_Model
from CL_controller import CL_Controller

def main():

    window = tk.Tk()
    server_ip = socket.gethostbyname(socket.gethostname())
    port = 8081
    
    view = CL_View(window)
    model = CL_Model(view)    
    controller = CL_Controller(model, view)
    
    # Gán sự kiện khi người dùng nhấn nút kết nối
    view.btn_connect.configure(command=controller.connect_to_server)  # Kết nối server khi nhấn nút
    
    window.mainloop()

if __name__ == "__main__":
    main()
