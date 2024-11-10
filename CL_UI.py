import sys
import tkinter as tk
from tkinter import messagebox
import tkinter.ttk as ttk
from tkinter.constants import *
import os.path

_location = os.path.dirname(__file__)

from Client.CL_UI_app_process import close_socket
import CL_UI_CRUD

_bgcolor = '#d9d9d9'
_fgcolor = '#000000'
_tabfg1 = 'black' 
_tabfg2 = 'white' 
_bgmode = 'light' 
_tabbg1 = '#d9d9d9' 
_tabbg2 = 'gray40' 

_style_code_ran = 0
def _style_code():
    global _style_code_ran
    if _style_code_ran: return        
    try: CL_UI_CRUD.root.tk.call('source',
                os.path.join(_location, 'themes', 'default.tcl'))
    except: pass
    style = ttk.Style()
    style.theme_use('default')
    style.configure('.', font = "TkDefaultFont")
    if sys.platform == "win32":
       style.theme_use('winnative')    
    _style_code_ran = 1

def test_btn_click():
    messagebox.showinfo(title= "TEST CLICK BUTTON", message="Thành công")

class run_Client:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''

        top.geometry("375x529+11+283")
        top.minsize(120, 1)
        top.maxsize(5564, 1901)
        top.resizable(0,  0)
        top.title("RUN CLIENT")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="#000000")

        self.top = top

        # Button definitions
        buttons = [
            (0.32, 0.261, 26, 107, "Ket noi Server", test_btn_click),
            (0.08, 0.378, 36, 317, "1. List / Start / Stop cac Applications dang chay SERVER", lambda: CL_UI_CRUD.show_window("APPLICATIONS_PROCESS", CL_UI_CRUD.create_app_process_window)),            
            (0.08, 0.469, 36, 317, "2. List / Start / Stop cac Services dang chay SERVER", lambda: CL_UI_CRUD.show_window("SERVICES_PROCESS", CL_UI_CRUD.create_sevices_window)),
            (0.08, 0.561, 36, 317, "3. Shutdown / Reset may SERVER", lambda: CL_UI_CRUD.show_window("SHUTDOWN_RESET_SERVER", CL_UI_CRUD.create_sd_rs_window)),
            (0.08, 0.654, 36, 317, "4. Xem man hinh hien thoi cua may SERVER", lambda: CL_UI_CRUD.show_window("VIEW_SERVER_SCREEN", CL_UI_CRUD.create_view_screen_window)),
            (0.08, 0.749, 36, 317, "5. Khoa / Bat phim nhan (keylogger) o may SERVER", lambda: CL_UI_CRUD.show_window("KEYLOGGER", CL_UI_CRUD.create_keylogger_window)),
            (0.08, 0.843, 36, 317, "6. Xoa files ; Copy files tu may SERVER", lambda: CL_UI_CRUD.show_window("DEL_COPY", CL_UI_CRUD.create_del_copy_window)),            
            
        ]

        for relx, rely, height, width, text, command in buttons:
            btn = tk.Button(self.top)
            btn.place(relx=relx, rely=rely, height=height, width=width)
            btn.configure(activebackground="#d9d9d9", activeforeground="black", background="#d9d9d9",
                        disabledforeground="#a3a3a3", font="-family {Segoe UI} -size 9",
                        foreground="#000000", highlightbackground="#d9d9d9", highlightcolor="#000000", text=text, command=command)

        # Label definitions
        labels = [
            (0.08, 0.206, 26, 121, "Nhập Port của Server"),
            (0.08, 0.149, 26, 111, "Nhập IP của server"),
            (0.08, 0.019, 26, 248, "ĐỒ ÁN ĐIỀU KHIỂN MÁY TÍNH TỪ XA")
        ]

        for relx, rely, height, width, text in labels:
            lbl = tk.Label(self.top)
            lbl.place(relx=relx, rely=rely, height=height, width=width)
            lbl.configure(activebackground="#d9d9d9", activeforeground="black", anchor='w', background="#d9d9d9",
                        compound='left', disabledforeground="#a3a3a3", font="-family {Segoe UI} -size 9",
                        foreground="#000000", highlightbackground="#d9d9d9", highlightcolor="#000000", text=text)

        # Entry definitions
        self.Entry_IP_address = tk.Entry(self.top, background="#ffffff", font="-family {Courier New} -size 10", foreground="#000000")
        self.Entry_IP_address.place(relx=0.4, rely=0.149, height=20, relwidth=0.491)

        self.Entry_Port = tk.Entry(self.top, background="#ffffff", font="-family {Courier New} -size 10", foreground="#000000")
        self.Entry_Port.place(relx=0.4, rely=0.206, height=20, relwidth=0.491)

        # Separator definitions
        separators = [(0.027, 0.113), (0.027, 0.34)]
        for relx, rely in separators:
            sep = ttk.Separator(self.top)
            sep.place(relx=relx, rely=rely, relwidth=0.933)

        # Label definition
        self.Label3 = tk.Label(self.top, background="#d9d9d9", foreground="#000000", font="-family {Segoe UI} -size 9",
                            text="Sinh viên: Nguyễn Thế Trung - MSSV: 23880092", anchor='w', activebackground="#d9d9d9",
                            activeforeground="black", disabledforeground="#a3a3a3", compound='left')
        self.Label3.place(relx=0.08, rely=0.057, height=26, width=255)

import tkinter as tk

def create_button(parent, text, relx, rely, width, height, font="-family {Segoe UI} -size 9", cursor=None):
    btn = tk.Button(parent, text=text, background="#d9d9d9", foreground="#000000", font=font,
                    activebackground="#d9d9d9", activeforeground="black", disabledforeground="#a3a3a3", 
                    highlightbackground="#d9d9d9", highlightcolor="#000000", cursor=cursor)
    btn.place(relx=relx, rely=rely, width=width, height=height)
    return btn

def create_label(parent, text, relx, rely, width, height, font="-family {Segoe UI} -size 9"):
    lbl = tk.Label(parent, text=text, background="#d9d9d9", foreground="#000000", font=font,
                   anchor='w', compound='left', disabledforeground="#a3a3a3",
                   highlightbackground="#d9d9d9", highlightcolor="#000000")
    lbl.place(relx=relx, rely=rely, width=width, height=height)
    return lbl

# Hàm tạo Entry
def create_entry(parent, relx, rely, relwidth, height):
    entry = tk.Entry(parent)
    entry.place(relx=relx, rely=rely, relwidth=relwidth, height=height)
    entry.configure(background="white", disabledforeground="#a3a3a3", font="-family {Courier New} -size 10",
                    foreground="#000000", highlightbackground="#d9d9d9", highlightcolor="#000000", insertbackground="#000000",
                    selectbackground="#d9d9d9", selectforeground="black")
    return entry

class CL_app_process:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.'''
        top.geometry("399x300+427+120")
        top.minsize(120, 1)
        top.maxsize(5564, 1901)
        top.resizable(0, 0)
        top.title("APPLICATIONS PROCESS")
        top.configure(background="#d9d9d9", highlightbackground="#d9d9d9", highlightcolor="#000000")
        self.top = top

         # Treeview configuration
        self.tree_app = ScrolledTreeView(self.top, columns="Col1")
        self.tree_app.place(relx=0.05, rely=0.2, relheight=0.753, relwidth=0.892)
        self.tree_app.heading("#0", text="PID", anchor="center")
        self.tree_app.column("#0", width=169, minwidth=20, stretch=1, anchor="w")
        self.tree_app.heading("Col1", text="Application Name", anchor="center")
        self.tree_app.column("Col1", width=170, minwidth=20, stretch=1, anchor="w")

        # Button configuration
        btn_list_app = create_button(self.top, "LIST APPS", 0.05, 0.043, 77, 36, command=self.list_apps_running)
        btn_start_app = create_button(self.top, "START APP", 0.301, 0.043, 77, 36, command=self.start_app_by_path)
        btn_stop_app = create_button(self.top, "STOP APP", 0.551, 0.043, 77, 36, command=self.stop_app_running_by_PID)
        btn_thoat_app = create_button(self.top, "THOAT", 0.802, 0.043, 57, 36, command=self.quit_app)
        
        def list_apps_running(self):
            list_apps_running(self.client_socket, self.tree_app)

        def stop_app_running_by_PID(self):
            stop_app_running_by_PID(self.client_socket, self.tree_app)

        def start_app_by_path(self):
            start_app_by_path(self.client_socket, self.tree_app)

        def quit_app(self):
            close_socket(self.client_socket)
            self.top.quit()

class CL_monitor:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.'''
        top.geometry("858x510+423+480")
        top.minsize(120, 1)
        top.maxsize(5564, 1901)
        top.resizable(0, 0)
        top.title("VIEW SERVER SCREEN")
        top.configure(background="#d9d9d9", highlightbackground="#d9d9d9", highlightcolor="#000000")
        self.top = top

        self.Label5 = create_label(self.top, "SNAPSHOT TIME:", 0.268, 0.02, 138, 28)
        self.lbl_time = create_label(self.top, "DD/MM/YYYY hh:mm:ss", 0.42, 0.02, 158, 28)

class CL_shutdown_reset:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.'''
        top.geometry("374x110+13+884")
        top.minsize(120, 1)
        top.maxsize(5564, 1901)
        top.resizable(0, 0)
        top.title("SHUTDOWN RESET SERVER")
        top.configure(background="#d9d9d9", highlightbackground="#d9d9d9", highlightcolor="#000000")
        self.top = top

        self.btn_cl_shutdown_sv = create_button(self.top, "SHUT DOWN SERVER", 0.246, 0.091, 167, 36, cursor="fleur")
        self.btn_cl_reset_sv = create_button(self.top, "RESET SERVER", 0.246, 0.545, 167, 36, cursor="fleur")

class CL_del_copy:
    def __init__(self, top=None):
        top.geometry("637x207+1315+693")
        top.minsize(120, 1)
        top.maxsize(5564, 1901)
        top.resizable(1, 1)
        top.title("DELETE-COPY")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="#000000")

        self.top = top
        _style_code()
        self.TSeparator3 = ttk.Separator(self.top)
        self.TSeparator3.place(relx=0.0, rely=0.391, relwidth=1.008)

        # Sử dụng create_label để tạo các Label
        self.Label4 = create_label(self.top, "PATH FILE", 0.016, 0.193, 66, 16)
        self.Label4_1 = create_label(self.top, "SOURCE FILE", 0.016, 0.483, 76, 16)
        self.Label4_1_1 = create_label(self.top, "DESTINATION", 0.016, 0.725, 82, 16)
        self.Label4_1_1_1 = create_label(self.top, "FOLDER", 0.031, 0.821, 53, 16)

        # Sử dụng create_entry để tạo các Entry
        self.entry_paste = create_entry(self.top, 0.157, 0.725, 0.666, 40)
        self.entry_copy = create_entry(self.top, 0.157, 0.435, 0.666, 40)
        self.entry_del = create_entry(self.top, 0.126, 0.145, 0.697, 40)

        # Sử dụng create_button để tạo các Button
        self.btn_paste_destination = create_button(self.top, "PASTE", 0.848, 0.725, 87, 36, cursor="fleur")
        self.btn_copy_file = create_button(self.top, "COPY", 0.848, 0.435, 87, 36, cursor="fleur")
        self.btn_del_file = create_button(self.top, "DELETE", 0.848, 0.145, 87, 36, cursor="fleur")

class CL_services_process:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.'''
        top.geometry("420x300+853+120")
        top.minsize(120, 1)
        top.maxsize(5564, 1901)
        top.resizable(0,  0)
        top.title("SERVICES PROCESS")
        top.configure(background="#d9d9d9", highlightbackground="#d9d9d9", highlightcolor="#000000")

        self.top = top
        _style_code()
        self.tree_app_1 = ScrolledTreeView(self.top)
        self.tree_app_1.place(relx=0.05, rely=0.2, relheight=0.753, relwidth=0.893)
        self.tree_app_1.configure(columns="Col1")
        self.tree_app_1.heading("#0", text="Tree", anchor="center")
        self.tree_app_1.column("#0", width=179, minwidth=20, stretch=1, anchor="w")
        self.tree_app_1.heading("Col1", text="Col1", anchor="center")
        self.tree_app_1.column("Col1", width=179, minwidth=20, stretch=1, anchor="w")

        # Buttons
        self.create_button(self.top, "THOAT", 0.802, 0.043, 57, 36, "btn_service_thoat")
        self.create_button(self.top, "LIST SERVICES", 0.05, 0.043, 87, 36, "btn_services_list")
        self.create_button(self.top, "STOP SERVICES", 0.55, 0.043, 87, 36, "btn_service_stop")
        self.create_button(self.top, "START SERVICE", 0.3, 0.043, 87, 36, "btn_ap_start")

    def create_button(self, parent, text, relx, rely, width, height, name):
        button = tk.Button(parent)
        button.place(relx=relx, rely=rely, width=width, height=height)
        button.configure(text=text, activebackground="#d9d9d9", activeforeground="black", background="#d9d9d9", 
                         font="-family {Segoe UI} -size 9", foreground="#000000", highlightbackground="#d9d9d9", 
                         highlightcolor="#000000")
        setattr(self, name, button)


class CL_keylogger:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.'''
        top.geometry("637x489+1307+122")
        top.minsize(120, 1)
        top.maxsize(5564, 1901)
        top.resizable(0,  0)
        top.title("KEYLOGGER")
        top.configure(background="#d9d9d9", highlightbackground="#d9d9d9", highlightcolor="#000000")

        self.top = top
        self.tb_keylogger = tk.Text(self.top)
        self.tb_keylogger.place(relx=0.047, rely=0.164, relheight=0.765, relwidth=0.854)
        self.tb_keylogger.configure(background="white", font="TkTextFont", foreground="black", highlightbackground="#d9d9d9", 
                                    highlightcolor="#000000", insertbackground="#000000", selectbackground="#d9d9d9", 
                                    selectforeground="black", wrap="word")

        # Buttons
        self.create_button(self.top, "CLEAR", 0.738, 0.041, 97, 36, "btn_clear", "fleur")
        self.create_button(self.top, "IN KEYLOGGER", 0.488, 0.043, 127, 36, "btn_print_keylogger", "fleur")
        self.create_button(self.top, "TAT KEYLOGGER", 0.27, 0.043, 107, 36, "btn_stop_keylogger")
        self.create_button(self.top, "BAT KEYLOGGER", 0.05, 0.043, 107, 36, "btn_start_keylogger")

    def create_button(self, parent, text, relx, rely, width, height, name, cursor=""):
        button = tk.Button(parent)
        button.place(relx=relx, rely=rely, width=width, height=height)
        button.configure(text=text, activebackground="#d9d9d9", activeforeground="black", background="#d9d9d9", 
                         font="-family {Segoe UI} -size 9", foreground="#000000", highlightbackground="#d9d9d9", 
                         highlightcolor="#000000", cursor=cursor)
        setattr(self, name, button)


# The following code is added to facilitate the Scrolled widgets you specified.
class AutoScroll(object):
    '''Configure the scrollbars for a widget.'''
    def __init__(self, master):
        #  Rozen. Added the try-except clauses so that this class
        #  could be used for scrolled entry widget for which vertical
        #  scrolling is not supported. 5/7/14.
        try:
            vsb = ttk.Scrollbar(master, orient='vertical', command=self.yview)
        except:
            pass
        hsb = ttk.Scrollbar(master, orient='horizontal', command=self.xview)
        try:
            self.configure(yscrollcommand=self._autoscroll(vsb))
        except:
            pass
        self.configure(xscrollcommand=self._autoscroll(hsb))
        self.grid(column=0, row=0, sticky='nsew')
        try:
            vsb.grid(column=1, row=0, sticky='ns')
        except:
            pass
        hsb.grid(column=0, row=1, sticky='ew')
        master.grid_columnconfigure(0, weight=1)
        master.grid_rowconfigure(0, weight=1)
        # Copy geometry methods of master  (taken from ScrolledText.py)
        methods = tk.Pack.__dict__.keys() | tk.Grid.__dict__.keys() \
                  | tk.Place.__dict__.keys()
        for meth in methods:
            if meth[0] != '_' and meth not in ('config', 'configure'):
                setattr(self, meth, getattr(master, meth))

    @staticmethod
    def _autoscroll(sbar):
        '''Hide and show scrollbar as needed.'''
        def wrapped(first, last):
            first, last = float(first), float(last)
            if first <= 0 and last >= 1:
                sbar.grid_remove()
            else:
                sbar.grid()
            sbar.set(first, last)
        return wrapped

    def __str__(self):
        return str(self.master)

def _create_container(func):
    '''Creates a ttk Frame with a given master, and use this new frame to
    place the scrollbars and the widget.'''
    def wrapped(cls, master, **kw):
        container = ttk.Frame(master)
        container.bind('<Enter>', lambda e: _bound_to_mousewheel(e, container))
        container.bind('<Leave>', lambda e: _unbound_to_mousewheel(e, container))
        return func(cls, container, **kw)
    return wrapped

class ScrolledTreeView(AutoScroll, ttk.Treeview):
    '''A standard ttk Treeview widget with scrollbars that will
    automatically show/hide as needed.'''
    @_create_container
    def __init__(self, master, **kw):
        ttk.Treeview.__init__(self, master, **kw)
        AutoScroll.__init__(self, master)

import platform
def _bound_to_mousewheel(event, widget):
    child = widget.winfo_children()[0]
    if platform.system() == 'Windows' or platform.system() == 'Darwin':
        child.bind_all('<MouseWheel>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Shift-MouseWheel>', lambda e: _on_shiftmouse(e, child))
    else:
        child.bind_all('<Button-4>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Button-5>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Shift-Button-4>', lambda e: _on_shiftmouse(e, child))
        child.bind_all('<Shift-Button-5>', lambda e: _on_shiftmouse(e, child))

def _unbound_to_mousewheel(event, widget):
    if platform.system() == 'Windows' or platform.system() == 'Darwin':
        widget.unbind_all('<MouseWheel>')
        widget.unbind_all('<Shift-MouseWheel>')
    else:
        widget.unbind_all('<Button-4>')
        widget.unbind_all('<Button-5>')
        widget.unbind_all('<Shift-Button-4>')
        widget.unbind_all('<Shift-Button-5>')

def _on_mousewheel(event, widget):
    if platform.system() == 'Windows':
        widget.yview_scroll(-1*int(event.delta/120),'units')
    elif platform.system() == 'Darwin':
        widget.yview_scroll(-1*int(event.delta),'units')
    else:
        if event.num == 4:
            widget.yview_scroll(-1, 'units')
        elif event.num == 5:
            widget.yview_scroll(1, 'units')

def _on_shiftmouse(event, widget):
    if platform.system() == 'Windows':
        widget.xview_scroll(-1*int(event.delta/120), 'units')
    elif platform.system() == 'Darwin':
        widget.xview_scroll(-1*int(event.delta), 'units')
    else:
        if event.num == 4:
            widget.xview_scroll(-1, 'units')
        elif event.num == 5:
            widget.xview_scroll(1, 'units')
def start_up():
    CL_UI_CRUD.main()

if __name__ == '__main__':
    CL_UI_CRUD.main()




