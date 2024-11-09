import tkinter as tk

import CL_UI

button_properties = {
            "activebackground": "#d9d9d9",
            "activeforeground": "black",
            "background": "#d9d9d9",
            "disabledforeground": "#a3a3a3",
            "font": "-family {Segoe UI} -size 9",
            "foreground": "#000000",
            "highlightbackground": "#d9d9d9",
            "highlightcolor": "#000000"        
            }

def create_button(self, relx, rely, height, width, text, command):
        btn = tk.Button(self.top)
        btn.place(relx=relx, rely=rely, height=height, width=width)
        btn.configure(text=text, command=command, **self.button_properties)
        return btn

def main(*args):
    '''Main entry point for the application.'''
    global root
    root = tk.Tk()
    root.protocol( 'WM_DELETE_WINDOW' , root.destroy)
    # Creates a toplevel widget.
    global _top1, _w1
    _top1 = root
    _w1 = CL_UI.run_Client(_top1)
    # Creates a toplevel widget.    
    global _top3, _w3
    _top3 = tk.Toplevel(root)
    _w3 = CL_UI.CL_app_process(_top3)
    # Creates a toplevel widget.
    global _top4, _w4
    _top4 = tk.Toplevel(root)
    _w4 = CL_UI.CL_monitor(_top4)
    # Creates a toplevel widget.
    global _top5, _w5
    _top5 = tk.Toplevel(root)
    _w5 = CL_UI.CL_shutdown_reset(_top5)
    # Creates a toplevel widget.
    global _top7, _w7
    _top7 = tk.Toplevel(root)
    _w7 = CL_UI.CL_services_process(_top7)
    # Creates a toplevel widget.
    global _top9, _w9
    _top9 = tk.Toplevel(root)
    _w9 = CL_UI.CL_keylogger(_top9)   
    
    global _top10, _w10
    _top10 = tk.Toplevel(root)
    _w10 = CL_UI.CL_del_copy(_top10)
    root.mainloop()

if __name__ == '__main__':
    CL_UI.start_up()



