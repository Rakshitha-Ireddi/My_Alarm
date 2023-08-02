import tkinter as tk
import time
import winsound

app = tk.Tk()
app.title("My Alarm🕧")
app.geometry("400x200")

# Load the background image using PhotoImage
background_image = tk.PhotoImage(file="background.gif")

# Create a label to display the background image
background_label = tk.Label(app, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Customize the font and color of the labels and buttons
current_time_label = tk.Label(app, text="", font=("Helvetica", 24), fg="white", bg="black")
current_time_label.pack(pady=20)

alarm_time_label = tk.Label(app, text="Set Alarm Time⏱️ (HH:MM):", font=("Helvetica", 12), fg="white", bg="#8a65f0")
alarm_time_label.pack()

alarm_time_entry = tk.Entry(app, font=("Helvetica", 18), fg="black", bg="white", width=10)
alarm_time_entry.pack(pady=10)

def update_time():
    current_time = time.strftime("%H:%M:%S")
    current_time_label.config(text=current_time)
    app.after(1000, update_time)

def check_alarm():
    alarm_time = alarm_time_entry.get()
    current_time = time.strftime("%H:%M")
    if current_time == alarm_time:
        winsound.Beep(1000, 2000)

def snooze_alarm():
    winsound.Beep(0, 0)  # Beep with frequency 0 to stop the alarm
    app.after(300000, check_alarm)  # Resume checking for the alarm after 5 minutes

snooze_button = tk.Button(app, text="Snooze", font=("Helvetica", 14), command=snooze_alarm, fg="white", bg="pink", activebackground="lightgreen")
snooze_button.pack(side="bottom", pady=5)

set_alarm_button = tk.Button(app, text="Set Alarm", font=("Helvetica", 14), command=check_alarm, fg="white", bg="grey", activebackground="lightblue")
set_alarm_button.pack(side="bottom", pady=10)

update_time()
app.mainloop()