import tkinter as tk
from context import Context

# Unit is ms
DISPLAY_INTERVAL = 10


class Gui(object):
    def __init__(self):
        # window settings
        self.__window = tk.Tk()
        self.__window.title(u'Stop watch')
        self.__window.geometry('500x200')
        self.__window.resizable(width=False, height=False)

        # display elapsed time
        self.__frame_top = tk.Frame(self.__window)
        self.__frame_top.pack(expand=True, fill=tk.BOTH)
        self.__time_text = tk.StringVar()
        self.__time_text.set('00:00:00')
        self.__elapsed_time = tk.Label(self.__frame_top, textvariable=self.__time_text,
                                       font=("Osaka-Mono", "80", "bold"))
        self.__elapsed_time.pack(expand=True, fill=tk.X)

        # place buttons
        self.__frame_bottom = tk.Frame(self.__window)
        self.__frame_bottom.pack(expand=True, fill=tk.BOTH)
        self.__start_stop_button_text = tk.StringVar()
        self.__start_stop_button_text.set('Start')
        self.__start_stop_button = tk.Button(self.__frame_bottom, textvariable=self.__start_stop_button_text, width=5,
                                             font=("", "40", "bold"))

        self.__start_stop_button.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
        self.__reset_button = tk.Button(self.__frame_bottom, text=u'Reset', width=5, font=("", "40", "bold"))

        self.__reset_button.pack(side=tk.RIGHT, expand=True, fill=tk.BOTH)
        self.__ctx = Context(self)
        self.__start_stop_button.bind('<Button-1>', self.__ctx.on_click_start_stop_button)
        self.__reset_button.bind('<Button-1>', self.__ctx.on_click_reset_button)

        self.__window.after(DISPLAY_INTERVAL, self.update_time)
        self.__window.mainloop()

    def update_time(self):
        t = self.__ctx.get_elapsed_time()
        h = int(t / 3600)
        m = int((t / 60) % 60)
        s = int(t % 60)
        ten_ms = int((t - int(t)) * 100)
        self.__time_text.set('{:02d}:{:02d}:{:02d}.{:02d}'.format(h, m, s, ten_ms))
        if self.__ctx.need_display_update() is True:
            self.__window.after(DISPLAY_INTERVAL, self.update_time)

    def set_start_stop_button_text(self, s):
        self.__start_stop_button_text.set(s)

    def disable_reset_button(self):
        self.__reset_button['state'] = 'disabled'

    def enable_reset_button(self):
        self.__reset_button['state'] = 'normal'
