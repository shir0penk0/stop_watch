import tkinter as tk


def on_click_start_stop_button(event):
    print('clicked')

if __name__ == '__main__':
    window = tk.Tk()
    window.geometry('600x600')
    elapsed_time = tk.Label(text=u'00:00:00')
    elapsed_time.pack()
    start_stop_button = tk.Button(text=u'Start', width=5)
    start_stop_button.bind('<Button-1>', on_click_start_stop_button)
    start_stop_button.pack()
    reset_button = tk.Button(text=u'Reset', width=5)
    reset_button.pack()

    window.title(u'Stop watch')
    window.mainloop()
