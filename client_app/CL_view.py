# views/main_view.py

import tkinter as tk
from tkinter import ttk, messagebox

class CL_View:
    def __init__(self, window):        
        self.window = window   
        self.window.title("RUN CLIENT")
        self.window.geometry("375x529+100+100")
        self.window.resizable(0, 0)
        self.window.configure(background="#d9d9d9")
        
        self.widget_factory = WidgetFactory(window)
        self.create_widgets()

    def create_widgets(self):
        # Labels
        self.label_title = self.widget_factory.create_label("ĐỒ ÁN ĐIỀU KHIỂN MÁY TÍNH TỪ XA", 0.08, 0.019, 248, 26)
        self.label_ip = self.widget_factory.create_label("Nhập IP của server", 0.08, 0.149, 111, 26)
        self.label_port = self.widget_factory.create_label("Nhập Port của Server", 0.08, 0.206, 121, 26)
        self.label_info = self.widget_factory.create_label("Sinh viên: Nguyễn Thế Trung - MSSV: 23880092", 0.08, 0.057, 255, 26)

        # Entry fields
        self.entry_ip = self.widget_factory.create_entry(0.4, 0.149, 0.491, 20)
        self.entry_port = self.widget_factory.create_entry(0.4, 0.206, 0.491, 20)

        # Buttons
        self.btn_connect = self.widget_factory.create_button("Kết nối Server", 0.32, 0.261, 107, 26)
        self.btn_applications = self.widget_factory.create_button("1. List / Start / Stop các Applications", 0.08, 0.378, 317, 36)
        self.btn_services = self.widget_factory.create_button("2. List / Start / Stop các Services", 0.08, 0.469, 317, 36)
        self.btn_shutdown_reset = self.widget_factory.create_button("3. Shutdown / Reset máy SERVER", 0.08, 0.561, 317, 36)
        self.btn_view_screen = self.widget_factory.create_button("4. Xem màn hình hiện thời của máy SERVER", 0.08, 0.654, 317, 36)
        self.btn_keylogger = self.widget_factory.create_button("5. Khóa / Bật phím (keylogger)", 0.08, 0.749, 317, 36)
        self.btn_file_operations = self.widget_factory.create_button("6. Xóa files ; Copy files từ SERVER", 0.08, 0.843, 317, 36)

        # Separators
        self.widget_factory.create_separator(0.027, 0.113)
        self.widget_factory.create_separator(0.027, 0.34)
        
class CL_app_process:
    def __init__(self, top):
        '''This class configures and populates the toplevel window.'''
        self.top = top
        self.top.geometry("399x300+427+120")
        self.top.minsize(120, 1)
        self.top.maxsize(5564, 1901)
        self.top.resizable(0, 0)
        self.top.title("APPLICATIONS PROCESS")
        self.top.configure(background="#d9d9d9", highlightbackground="#d9d9d9", highlightcolor="#000000")
        
        # Create an instance of WidgetFactory
        self.widget_factory = WidgetFactory(top)
        self.create_widgets()

    def create_widgets(self):
        '''This method creates all the widgets for the "APPLICATIONS PROCESS" window.'''

        # Treeview configuration
        self.tree_app = ScrolledTreeView(self.top, columns="Col1")
        self.tree_app.place(relx=0.05, rely=0.2, relheight=0.753, relwidth=0.892)
        self.tree_app.heading("#0", text="PID", anchor="center")
        self.tree_app.column("#0", width=169, minwidth=20, stretch=1, anchor="w")
        self.tree_app.heading("Col1", text="Application Name", anchor="center")
        self.tree_app.column("Col1", width=170, minwidth=20, stretch=1, anchor="w")
        self.tree_app.heading("Col2", text="Count Thread", anchor="center")
        self.tree_app.column("Col2", width=170, minwidth=20, stretch=1, anchor="w")

        # Button configuration
        self.btn_list_app = self.widget_factory.create_button("LIST APPS", 0.05, 0.043, 77, 36)
        self.btn_start_app = self.widget_factory.create_button("START APP", 0.301, 0.043, 77, 36)
        self.btn_stop_app = self.widget_factory.create_button("STOP APP", 0.551, 0.043, 77, 36)
        self.btn_thoat_app = self.widget_factory.create_button("THOAT", 0.802, 0.043, 57, 36)

class CL_services_process:
    def __init__(self, top=None):
        self.top = top
        self.top.geometry("420x300+853+120")
        self.top.minsize(120, 1)
        self.top.maxsize(5564, 1901)
        self.top.resizable(0, 0)
        self.top.title("SERVICES PROCESS")
        self.top.configure(background="#d9d9d9", highlightbackground="#d9d9d9", highlightcolor="#000000")

        # Create an instance of WidgetFactory
        self.widget_factory = WidgetFactory(self.top)
        self.create_widgets()

    def create_widgets(self):
        # Treeview configuration
        self.tree_app_1 = ScrolledTreeView(self.top, columns="Col1")
        self.tree_app_1.place(relx=0.05, rely=0.2, relheight=0.753, relwidth=0.893)
        self.tree_app_1.heading("#0", text="Name", anchor="center")
        self.tree_app_1.column("#0", width=179, minwidth=20, stretch=1, anchor="w")
        self.tree_app_1.heading("Col1", text="Col1", anchor="center")
        self.tree_app_1.column("Col1", width=179, minwidth=20, stretch=1, anchor="w")
        self.tree_app.heading("Col2", text="Count Thread", anchor="center")
        self.tree_app.column("Col2", width=170, minwidth=20, stretch=1, anchor="w")

        # Button configuration
        self.btn_list_service = self.widget_factory.create_button("LIST SERVICES", 0.05, 0.043, 87, 36)
        self.btn_start_service = self.widget_factory.create_button("START SERVICE", 0.3, 0.043, 87, 36)
        self.btn_stop_service = self.widget_factory.create_button("STOP SERVICES", 0.55, 0.043, 87, 36)
        self.btn_thoat_service = self.widget_factory.create_button("THOAT", 0.802, 0.043, 57, 36)

class CL_shutdown_reset:
    def __init__(self, top=None):
        self.top = top
        self.top.geometry("374x110+13+884")
        self.top.minsize(120, 1)
        self.top.maxsize(5564, 1901)
        self.top.resizable(0, 0)
        self.top.title("SHUTDOWN RESET SERVER")
        self.top.configure(background="#d9d9d9", highlightbackground="#d9d9d9", highlightcolor="#000000")

        # Create an instance of WidgetFactory
        self.widget_factory = WidgetFactory(self.top)
        self.create_widgets()

    def create_widgets(self):
        # Button configuration
        self.btn_cl_shutdown_sv = self.widget_factory.create_button("SHUT DOWN SERVER", 0.246, 0.091, 167, 36)
        self.btn_cl_reset_sv = self.widget_factory.create_button("RESET SERVER", 0.246, 0.545, 167, 36)

class CL_view_screen:
    def __init__(self, top=None):
        self.top = top
        self.top.geometry("858x510+423+480")
        self.top.minsize(120, 1)
        self.top.maxsize(5564, 1901)
        self.top.resizable(0, 0)
        self.top.title("VIEW SERVER SCREEN")
        self.top.configure(background="#d9d9d9", highlightbackground="#d9d9d9", highlightcolor="#000000")

        # Create an instance of WidgetFactory
        self.widget_factory = WidgetFactory(self.top)
        self.create_widgets()

    def create_widgets(self):
        '''This method creates all the widgets for the "VIEW SERVER SCREEN" window.'''

        # Label configuration
        self.Label5 = self.widget_factory.create_label("SNAPSHOT TIME:", 0.268, 0.02, 138, 28)
        self.lbl_time = self.widget_factory.create_label("DD/MM/YYYY hh:mm:ss", 0.42, 0.02, 158, 28)

class CL_keylogger:
    def __init__(self, top=None):
        self.top = top
        self.top.geometry("637x489+1307+122")
        self.top.minsize(120, 1)
        self.top.maxsize(5564, 1901)
        self.top.resizable(0,  0)
        self.top.title("KEYLOGGER")
        self.top.configure(background="#d9d9d9", highlightbackground="#d9d9d9", highlightcolor="#000000")

        # Create an instance of WidgetFactory
        self.widget_factory = WidgetFactory(self.top)
        self.create_widgets()

    def create_widgets(self):
        # Button configuration using WidgetFactory
        self.btn_clear = self.widget_factory.create_button("CLEAR", 0.738, 0.041, 97, 36)
        self.btn_print_keylogger = self.widget_factory.create_button("IN KEYLOGGER", 0.488, 0.043, 127, 36)
        self.btn_stop_keylogger = self.widget_factory.create_button("TAT KEYLOGGER", 0.27, 0.043, 107, 36)
        self.btn_start_keylogger = self.widget_factory.create_button("BAT KEYLOGGER", 0.05, 0.043, 107, 36)
    

class CL_del_copy:
    def __init__(self, top=None):
        self.top = top
        self.top.geometry("637x207+1315+693")
        self.top.minsize(120, 1)
        self.top.maxsize(5564, 1901)
        self.top.resizable(1, 1)
        self.top.title("DELETE-COPY")
        self.top.configure(background="#d9d9d9", highlightbackground="#d9d9d9", highlightcolor="#000000")

        # Create an instance of WidgetFactory
        self.widget_factory = WidgetFactory(self.top)
        self.create_widgets()

    def create_widgets(self):
        # Separator
        self.TSeparator3 = ttk.Separator(self.top)
        self.TSeparator3.place(relx=0.0, rely=0.391, relwidth=1.008)

        # Label configuration
        self.Label4 = self.widget_factory.create_label("PATH FILE", 0.016, 0.193, 66, 16)
        self.Label4_1 = self.widget_factory.create_label("SOURCE FILE", 0.016, 0.483, 76, 16)
        self.Label4_1_1 = self.widget_factory.create_label("DESTINATION", 0.016, 0.725, 82, 16)
        self.Label4_1_1_1 = self.widget_factory.create_label("FOLDER", 0.031, 0.821, 53, 16)

        # Entry configuration
        self.entry_paste = self.widget_factory.create_entry(0.157, 0.725, 0.666, 40)
        self.entry_copy = self.widget_factory.create_entry(0.157, 0.435, 0.666, 40)
        self.entry_del = self.widget_factory.create_entry(0.126, 0.145, 0.697, 40)

        # Button configuration with custom cursor
        self.btn_paste_destination = self.widget_factory.create_button("PASTE", 0.848, 0.725, 87, 36)
        self.btn_copy_file = self.widget_factory.create_button("COPY", 0.848, 0.435, 87, 36)
        self.btn_del_file = self.widget_factory.create_button("DELETE", 0.848, 0.145, 87, 36)

        
class WidgetFactory:
    def __init__(self, window):
        self.window = window

    def create_label(self, text, relx, rely, width, height):
        label = tk.Label(self.window, text=text, background="#d9d9d9", foreground="#000000", anchor='w')
        label.place(relx=relx, rely=rely, width=width, height=height)
        return label

    def create_entry(self, relx, rely, relwidth, height):
        entry = tk.Entry(self.window, background="white", foreground="#000000")
        entry.place(relx=relx, rely=rely, relwidth=relwidth, height=height)
        return entry

    def create_button(self, text, relx, rely, width, height):
        button = tk.Button(self.window, text=text, background="#d9d9d9", foreground="#000000")
        button.place(relx=relx, rely=rely, width=width, height=height)
        return button

    def create_separator(self, relx, rely, relwidth=0.946):
        separator = ttk.Separator(self.window, orient="horizontal")
        separator.place(relx=relx, rely=rely, relwidth=relwidth)

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
