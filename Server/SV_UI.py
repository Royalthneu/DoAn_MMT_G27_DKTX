from tkinter import Tk
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *

# Tạo cửa sổ chính
window = Tk()

# Cấu hình cửa sổ
window.geometry("369x83+24+119")
window.minsize(120, 1)
window.maxsize(5564, 1901)
window.resizable(0, 0)
window.title("RUN SERVER")
window.configure(background="#d9d9d9", highlightbackground="#d9d9d9", highlightcolor="#000000")

# Labels
labels_config = [
    {"text": "Server IP:", "relx": 0.041, "rely": 0.289, "width": 93},
    {"text": "0.0.0.0", "relx": 0.22, "rely": 0.241, "width": 119},
    {"text": "Port:", "relx": 0.054, "rely": 0.602, "width": 64},
    {"text": "8081", "relx": 0.217, "rely": 0.602, "width": 34}
]

for config in labels_config:
    lbl = tk.Label(window, text=config["text"], background="#d9d9d9", foreground="#000000",
                   font="-family {Segoe UI} -size 9", anchor='w', activebackground="#d9d9d9",
                   activeforeground="black", disabledforeground="#a3a3a3")
    lbl.place(relx=config["relx"], rely=config["rely"], height=13, width=config["width"])

# Buttons
btn_sv_open = tk.Button(window, text="Open Server", background="#d9d9d9", foreground="#000000",
                        font="-family {Segoe UI} -size 9", activebackground="#d9d9d9",
                        activeforeground="black", disabledforeground="#a3a3a3")
btn_sv_open.place(relx=0.678, rely=0.12, height=26, width=97)

btn_sv_close = tk.Button(window, text="Close Server", background="#d9d9d9", foreground="#000000",
                         font="-family {Segoe UI} -size 9", activebackground="#d9d9d9",
                         activeforeground="black", disabledforeground="#a3a3a3")
btn_sv_close.place(relx=0.678, rely=0.602, height=26, width=97)

# Menu
menubar = tk.Menu(window, font="TkMenuFont", bg="#d9d9d9", fg="#000000")
window.configure(menu=menubar)

# Bắt đầu vòng lặp chính
window.mainloop()
