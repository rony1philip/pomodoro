from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 15
reps = 0
my_timer = None


# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    global my_timer
    reps = 0
    window.after_cancel(my_timer)
    canvas.itemconfig(timer_text, text='00:00')
    timer.config(text='Timer')
    timer.place(x=105, y=0)
    check_marks.config(text='')


# ---------------------------- TIMER MECHANISM ------------------------------- # 


def start_timer():
    global reps
    reps +=1
    work_sec = WORK_MIN * 60
    short_break_sac = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    # if 1,3,5,7

    if reps%8 == 0:
        time_count(long_break_sec)
        timer.config(text= 'Long Break', fg=RED)
        timer.place(x=35, y=0)
    elif reps % 2 == 0:
        time_count(short_break_sac)
        timer.config(text='Short Break', fg=PINK)
        timer.place(x=25, y=0)
    else:
        time_count(work_sec)
        timer.config(text='Work time', fg=GREEN)
        timer.place(x=45, y=0)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 


def time_count(count):
    global my_timer
    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f'0{count_sec}'
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        my_timer= window.after(1000, time_count, count-1)
    else:
        marks = ''
        work_sessions = math.floor(reps/2)
        start_timer()
        for _ in range(work_sessions):
            marks += '✔'
            check_marks.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #






scenes = 0
scenes_s = '0'
minits = 0
minits_s = '0'
window = Tk()
window.title('pomodoro')
window.config(padx=100, pady=50, bg=YELLOW)
window.minsize(550, 450)



canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image = tomato_img )
timer_text = canvas.create_text(100,132, text=f"00:00", fill='white', font=(FONT_NAME, 33, 'bold'))
canvas.place(x = 80, y=70)

timer = Label(window, text='TIMER', fg= GREEN, highlightthickness=0,font=(FONT_NAME, 40))
timer.configure(bg=YELLOW)
timer.place(x=105, y=0)

start_button = Button(text='Start',command=start_timer, highlightthickness=0)
start_button.place(x=0, y=300)

reset_button = Button(text='Reset', command=reset_timer, highlightthickness=0)
reset_button.place(x=300, y=300)


check_marks = Label(fg=GREEN, bg=YELLOW, font=(35))
check_marks.place(x=155, y=300)
window.mainloop()


