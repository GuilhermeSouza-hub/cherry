# Lil' Pomodoro:Cherry v1.2.1
# time todo: 40 min. for 4 times
# small pause: 5 min, for 3 times
# pause: 15 min
import tkinter as tk
from datetime import timedelta

window = tk.Tk()
window.title('Cherry')
window.geometry("200x90")
frame = tk.Frame(window)
frame.pack()
labelmain = tk.Label(frame, textvariable='')
pause = tk.Button(frame, text="Pause")


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
    pause.pack(side="bottom")


def core(tempo: int, win=window):
    win.title(f"Cherry:{tempo}min")
    result = tk.StringVar()
    labelmain.configure(textvariable=result)
    labelmain.pack(pady=15)

    toggle = False
    term = timedelta(seconds=-1)

    setting_time = timedelta(minutes=tempo)

    count = 1

    def pause_btn():
        nonlocal toggle, term
        toggle = not toggle

        if toggle:
            term = timedelta(seconds=0)
            pause.configure(text="Continue")
        else:
            term = timedelta(seconds=-1)
            pause.configure(text="Pause")

    def timer():
        pause.configure(command=pause_btn)
        id_t = win.after(1000, timer)

        nonlocal setting_time
        if setting_time != timedelta(minutes=0):
            setting_time = setting_time + term
            result.set(setting_time)
        else:
            result.set("0:00:00")

            win.after_cancel(id_t)

            warning_window()
            nonlocal count
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


btn = tk.Button(frame, text="Start", command=start_pomodoro)
btn.pack(pady=30)

window.mainloop()
