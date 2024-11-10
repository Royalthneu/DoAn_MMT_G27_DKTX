from tkinter import Tk
from CL_controller import ClientController

def main():
    root = Tk()
    controller = ClientController(root)
    root.mainloop()

if __name__ == "__main__":
    main()
