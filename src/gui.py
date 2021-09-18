import tkinter as tk
from context import Context

# Unit is ms
DISPLAY_INTERVAL = 10


class Gui(object):
    def __init__(self):
        # window settings
        self.window = tk.Tk()
        self.window.title(u'Stop watch')
        self.window.geometry('500x200')
        self.window.resizable(width=False, height=False)

        # display elapsed time
        self.frame_top = tk.Frame(self.window, borderwidth=10, relief='sunken')
        self.frame_top.pack(expand=True, fill=tk.BOTH)
        self.time_text = tk.StringVar()
        self.time_text.set('00:00:00')
        self.elapsed_time = tk.Label(self.frame_top, textvariable=self.time_text, font=("Osaka-Mono", "80", "bold"))
        self.elapsed_time.pack(expand=True, fill=tk.X)

        # place buttons
        self.frame_bottom = tk.Frame(self.window, borderwidth=10, relief='sunken')
        self.frame_bottom.pack(expand=True, fill=tk.BOTH)
        self.start_stop_button_text = tk.StringVar()
        self.start_stop_button_text.set('Start')
        self.start_stop_button = tk.Button(self.frame_bottom, textvariable=self.start_stop_button_text, width=5,
                                           font=("", "40", "bold"))
        self.ctx = Context(self)
        self.start_stop_button.bind('<Button-1>', self.ctx.on_click_start_stop_button)
        self.start_stop_button.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
        self.reset_button = tk.Button(self.frame_bottom, text=u'Reset', width=5, font=("", "40", "bold"))
        self.reset_button.bind('<Button-1>', self.ctx.on_click_reset_button)
        self.reset_button.pack(side=tk.RIGHT, expand=True, fill=tk.BOTH)

        self.window.after(DISPLAY_INTERVAL, self.__update_time)
        self.window.mainloop()

    def __update_time(self):
        t = self.ctx.get_elapsed_time()
        h = int(t / 3600)
        m = int((t / 60) % 60)
        s = int(t % 60)
        ms = int((t - int(t)) * 100)
        self.time_text.set('{:02d}:{:02d}:{:02d}.{:02d}'.format(h, m, s, ms))
        self.window.after(DISPLAY_INTERVAL, self.__update_time)

    def set_start_stop_button_text(self, s):
        self.start_stop_button_text.set(s)
