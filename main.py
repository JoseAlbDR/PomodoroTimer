from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0


# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    timers = {1: short_break_sec, 0: work_sec, 8: long_break_sec}
    n = reps % 2
    count_down(timers[n])


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    global reps
    count_minute = int(count / 60)
    count_seconds = count % 60

    if len(str(count_seconds)) == 1:
        format_seconds = f"0{count_seconds}"
    else:
        format_seconds = count_seconds

    timer = f"{count_minute}:{format_seconds}"
    canvas.itemconfig(timer_text, text=timer)
    if count > 0:
        window.after(1000, count_down, count - 1)
    else:
        reps += 1
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #

# Window
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# Check
check = "✓"

# Canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 132, text="00:00", fill="white", font=(FONT_NAME, 32, "bold"))
canvas.grid(column=1, row=1)

# Text labels
timer_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 28, "bold"))
timer_label.grid(column=1, row=0)

check_label = Label(text=check, fg=GREEN, bg=YELLOW)
check_label.grid(column=1, row=3)

# Buttons
start_button = Button(text="Start", command=start_timer)
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset")
reset_button.grid(row=2, column=2)

window.mainloop()
