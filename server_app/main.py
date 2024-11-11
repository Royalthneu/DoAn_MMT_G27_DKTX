# main.py
import socket
import tkinter as tk

from SV_view import SV_View
from SV_model import SV_Model
from SV_controller import SV_Controller

def main():

    window = tk.Tk()
    server_ip = socket.gethostbyname(socket.gethostname())
    port = 8081
    
    view = SV_View(window)
    model = SV_Model(server_ip, port)    
    controller = SV_Controller(model, view)
    
    window.mainloop()

if __name__ == "__main__":
    main()
