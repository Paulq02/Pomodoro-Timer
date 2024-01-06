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
LONG_BREAK_MIN = 20
reps = 0
# ---------------------------- TIMER RESET ------------------------------- # 



# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps

    count_down(1 * 10)

    





# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count_input):
    minutes = count_input // 60
    seconds = count_input % 60
    if seconds < 10:
        seconds = f"0{seconds}"
        
    if count_input > 0:
        window.after(1000, count_down, count_input - 1)
        canvas.itemconfig(timer_canvas, text=f"{minutes}:{seconds}")
    
    if count_input == 0:
        global reps
        reps += 1
        checkmark_label = Label(text="✔", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 30))
        checkmark_label.grid(row=3, column=1)

        

    


        
        
    
    
    




      
        
    
       
       
    
       

    
    
    
    





# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.minsize(width=400, height=400)
window.title("Paul Pomodoro Timer")
window.config(bg=YELLOW)







timer_label = Label(text="Timer", fg=GREEN, font=(FONT_NAME,35, "bold" ), bg=YELLOW)
timer_label.grid(row=0, column=1, pady=20)


canvas = Canvas(width=202, height=224, bg=YELLOW, highlightthickness=0)
picture = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=picture)
timer_canvas = canvas.create_text(100,130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold") )
canvas.grid(row=1, column=1)






start_button = Button(text="Start", bg="white", fg="black", command=start_timer)
start_button.grid(row=2, column=0, padx=20)

reset_button = Button(text="Reset", bg="white", fg="black")
reset_button.grid(row=2, column=2, padx=20)




















     
window.mainloop()