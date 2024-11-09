import tkinter as tk

# Hàm tạo Label
def create_label(window, text, relx, rely, width):
    return tk.Label(window, text=text, background="#d9d9d9", foreground="#000000",
                     font="-family {Segoe UI} -size 9", anchor='w', activebackground="#d9d9d9",
                     activeforeground="black", disabledforeground="#a3a3a3").place(
                     relx=relx, rely=rely, height=13, width=width)

# Hàm tạo Button
def create_button(window, text, relx, rely, command=None):
    return tk.Button(window, text=text, background="#d9d9d9", foreground="#000000",
                     font="-family {Segoe UI} -size 9", activebackground="#d9d9d9",
                     activeforeground="black", disabledforeground="#a3a3a3", command=command).place(
                     relx=relx, rely=rely, height=26, width=97)

# Hàm xử lý cho nút Open Server
def open_server():
    label_status.config(text="Server is opening...")
    print("Server is opening")

# Hàm xử lý cho nút Close Server
def close_server():
    label_status.config(text="Server is closing...")
    print("Server is closing")

# Tạo cửa sổ chính
window = tk.Tk()

# Cấu hình cửa sổ
window.geometry("369x83+24+119")
window.minsize(120, 1)
window.maxsize(5564, 1901)
window.resizable(0, 0)
window.title("RUN SERVER")
window.configure(background="#d9d9d9", highlightbackground="#d9d9d9", highlightcolor="#000000")

# Labels cấu hình
labels_config = [
    {"text": "Server IP:", "relx": 0.041, "rely": 0.289, "width": 93},
    {"text": "0.0.0.0", "relx": 0.22, "rely": 0.241, "width": 119},
    {"text": "Port:     8081", "relx": 0.054, "rely": 0.602, "width": 80},    
]

for config in labels_config:
    create_label(window, config["text"], config["relx"], config["rely"], config["width"])


# Labels hiển thị trạng thái
label_status = tk.Label(window, text="Server is closing", background="#d9d9d9", foreground="#000000", 
                        font="-family {Segoe UI} -size 9", anchor='w')
label_status.place(relx=0.300, rely=0.58, height=20, width=300)

# Buttons với command
create_button(window, "Open Server", 0.678, 0.12, command=open_server)
create_button(window, "Close Server", 0.678, 0.602, command=close_server)

# Menu
menubar = tk.Menu(window, font="TkMenuFont", bg="#d9d9d9", fg="#000000")
window.configure(menu=menubar)

# Bắt đầu vòng lặp chính
window.mainloop()
