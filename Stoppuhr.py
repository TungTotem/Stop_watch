import tkinter as tk
from datetime import datetime

class Stopwatch:
    def __init__(self, master):
        self.master = master
        self.master.title("Stopwatch")

        self.is_running = False
        self.start_time = None
        self.elapsed_time = 0

        self.time_label = tk.Label(self.master, text="00:00:00.000", font=("Helvetica", 24))
        self.time_label.pack(pady=20)

        self.start_button = tk.Button(self.master, text="Start", command=self.start)
        self.start_button.pack(pady=10)

        self.pause_button = tk.Button(self.master, text="Pause", command=self.pause)
        self.pause_button.pack(pady=10)
        self.pause_button.config(state="disabled")

        self.reset_button = tk.Button(self.master, text="Reset", command=self.reset)
        self.reset_button.pack(pady=10)
        self.reset_button.config(state="disabled")

    def start(self):
        if not self.is_running:
            self.is_running = True
            self.start_time = datetime.now()
            self.update_timer()

            self.start_button.config(state="disabled")
            self.pause_button.config(state="normal")
            self.reset_button.config(state="normal")

    def pause(self):
        if self.is_running:
            self.is_running = False
            self.elapsed_time += (datetime.now() - self.start_time).total_seconds()

            self.start_button.config(state="normal")
            self.pause_button.config(state="disabled")

    def reset(self):
        self.is_running = False
        self.start_time = None
        self.elapsed_time = 0
        self.time_label.config(text="00:00:00.000")

        self.start_button.config(state="normal")
        self.pause_button.config(state="disabled")
        self.reset_button.config(state="disabled")

    def update_timer(self):
        if self.is_running:
            elapsed_time = self.elapsed_time + (datetime.now() - self.start_time).total_seconds()
            hours = int(elapsed_time // 3600)
            minutes = int((elapsed_time % 3600) // 60)
            seconds = int(elapsed_time % 60)
            milliseconds = int((elapsed_time % 1) * 1000)

            time_str = "{:02d}:{:02d}:{:02d}.{:03d}".format(hours, minutes, seconds, milliseconds)
            self.time_label.config(text=time_str)

        self.master.after(50, self.update_timer)

root = tk.Tk()
stopwatch = Stopwatch(root)
root.mainloop()
