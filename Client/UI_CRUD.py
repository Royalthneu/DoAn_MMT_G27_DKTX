import tkinter as tk

import CL_UI

window_status = {}

def main(*args):
    '''Main entry point for the application.'''
    global root
    root = tk.Tk()
    root.protocol( 'WM_DELETE_WINDOW' , root.destroy)
    # Creates a toplevel widget.
    global _top1, _w1
    _top1 = root
    _w1 = CL_UI.run_Client(_top1)
    
    root.mainloop()


if __name__ == '__main__':
    CL_UI.start_up()

# Hàm tạo cửa sổ con 1
def create_app_process_window():
    create_window("APPLICATION_PROCESS", CL_UI.CL_app_process)
    
# Hàm tạo cửa sổ con 2
def create_sevices_window():
    create_window("SERVICES_PROCESS", CL_UI.CL_services_process)    
    
# Hàm tạo cửa sổ con 3
def create_sd_rs_window():
    create_window("SHUTDOWN_RESET_SERVER", CL_UI.CL_shutdown_reset)    

# Hàm tạo cửa sổ con 4
def create_view_screen_window():
    create_window("VIEW_SERVER_SCREEN", CL_UI.CL_monitor)

# Hàm tạo cửa sổ con 5
def create_keylogger_window():
    create_window("KEYLOGGER", CL_UI.CL_keylogger)    

# Hàm tạo cửa sổ con 6
def create_del_copy_window():
    create_window("DEL_COPY", CL_UI.CL_del_copy)    

#Hàm show wd
def show_window(window_name, create_window_func):
    '''Hiển thị cửa sổ con và quản lý việc mở lại cửa sổ'''
    global root
    # Kiểm tra nếu cửa sổ con đã bị đóng (bị xóa khỏi window_status)
    if window_name not in window_status or not window_status[window_name].winfo_exists():
        # Nếu cửa sổ chưa được mở hoặc đã đóng, tạo cửa sổ mới và khóa cửa sổ cha
        window = create_window_func()
        window.grab_set()  # Khóa cửa sổ cha cho đến khi cửa sổ con đóng
        window_status[window_name] = window
    else:
        # Nếu cửa sổ vẫn mở, chỉ cần kích hoạt nó
        window_status[window_name].lift()  # Đưa cửa sổ con lên trên

def close_window(window_name, window):
    '''Đóng cửa sổ và xóa khỏi window_status'''
    window.destroy()  # Đảm bảo cửa sổ được đóng
    if window_name in window_status:
        window_status.pop(window_name)

def create_window(window_name, create_func):
    '''Tạo cửa sổ con và xử lý sự kiện đóng cửa sổ'''
    top = tk.Toplevel(root)
    create_func(top)
    # Xử lý khi đóng cửa sổ con
    top.protocol("WM_DELETE_WINDOW", lambda: close_window(window_name, top))
    return top





