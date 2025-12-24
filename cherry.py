# Lil' Pomodoro:Cherry v1.0.1
# time todo: 40 min. for 4 times
# small pause: 5 min, for 3 times
# pause: 15 min
import tkinter as tk
from datetime import timedelta

window = tk.Tk()
window.title('Cherry')
window.geometry("200x90")
labelmain = tk.Label(window, textvariable='')

count = 1


def vanish_btn(botao):
    btn.config(state="disabled")
    btn.pack_forget()


def warning_window():
    warnw = tk.Tk()
    warnw.title('ACABOU O TEMPO')
    warnw.geometry("1366x764")
    wl = tk.Label(warnw, text="ACABOU O TEMPO")
    wl.pack(pady=300)
    warnw.after(500)


def start_pomodoro():
    vanish_btn(btn)
    core(40)


def core(tempo: int, win=window):
    win.title(f"Cherry:{tempo}min")
    result = tk.StringVar()
    labelmain.configure(textvariable=result)
    labelmain.pack(pady=35)

    setting_time = timedelta(minutes=tempo)
    minus = timedelta(seconds=-1)

    def timer():
        id_t = win.after(1000, timer)
        nonlocal setting_time
        if setting_time != timedelta(minutes=0):
            setting_time = setting_time + minus
            result.set(setting_time)
        else:
            result.set("0:00:00")

            win.after_cancel(id_t)

            warning_window()
            global count
            match tempo:
                case 40:
                    if count < 4:
                        count += 1
                        core(5)
                    else:
                        count = 1
                        core(15)
                case _:
                    core(40)

    timer()


btn = tk.Button(window, text="Start", command=start_pomodoro)
btn.pack(pady=35)

window.mainloop()
