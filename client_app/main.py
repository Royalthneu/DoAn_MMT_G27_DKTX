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
    model = CL_Model()    
    controller = CL_Controller(model, view)
    
    window.mainloop()

if __name__ == "__main__":
    main()
