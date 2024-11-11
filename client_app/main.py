import tkinter as tk
from CL_controller import ServerController

def main():
    window = tk.Tk()
    controller = ServerController(window)
    window.mainloop()

if __name__ == "__main__":
    main()
