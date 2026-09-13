import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Useless Alarm Clock")
root.geometry("400x300")

seconds = 0
timer = None


def start_alarm():
    global seconds, timer

    try:
        seconds = int(entry.get())

        if seconds <= 0:
            messagebox.showerror("Error", "Enter a positive number.")
            return

        countdown()

    except ValueError:
        messagebox.showerror("Error", "Please enter seconds.")


def countdown():
    global seconds, timer

    if seconds > 0:
        minutes = seconds // 60
        remaining_seconds = seconds % 60

        timer_label.config(
            text=f"{minutes:02d}:{remaining_seconds:02d}"
        )

        seconds -= 1
        timer = root.after(1000, countdown)

    else:
        timer_label.config(text="WAKE UP!")
        messagebox.showinfo("ALARM!", "🔊 WAKE UP! 🔊")


title_label = tk.Label(
    root,
    text="⏰ USELESS ALARM CLOCK",
    font=("Arial", 18, "bold")
)
title_label.pack(pady=20)

instruction = tk.Label(
    root,
    text="Enter seconds until you want the alarm:"
)
instruction.pack()

entry = tk.Entry(root, font=("Arial", 14))
entry.pack(pady=10)

start_button = tk.Button(
    root,
    text="START",
    command=start_alarm,
    font=("Arial", 12)
)
start_button.pack(pady=10)

timer_label = tk.Label(
    root,
    text="00:00",
    font=("Arial", 30, "bold")
)
timer_label.pack(pady=10)

root.mainloop()