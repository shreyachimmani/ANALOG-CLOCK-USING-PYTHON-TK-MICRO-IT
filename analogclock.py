import tkinter as tk
import math
from time import localtime

class AnalogClock(tk.Canvas):
    def __init__(self, parent, size=400):
        super().__init__(parent, width=size, height=size, bg='white', highlightthickness=0)
        self.size = size
        self.center = size // 2
        self.radius = self.center - 20

        # Initial colors (light mode)
        self.bg_color = 'white'
        self.face_color = '#a3d2ca'
        self.border_color = '#5eaaa8'
        self.hour_hand_color = '#056676'
        self.min_hand_color = '#028090'
        self.sec_hand_color = '#f95738'
        self.number_color = '#056676'

        self.pack()
        self.draw_clock_face()
        self.update_clock()

    def draw_clock_face(self):
        self.delete('all')

        # Clock background circle
        self.create_oval(10, 10, self.size - 10, self.size - 10,
                         width=6, fill=self.face_color, outline=self.border_color)

        # Hour marks (thicker lines)
        for i in range(12):
            angle = math.pi / 6 * i
            x_start = self.center + (self.radius - 25) * math.sin(angle)
            y_start = self.center - (self.radius - 25) * math.cos(angle)
            x_end = self.center + self.radius * math.sin(angle)
            y_end = self.center - self.radius * math.cos(angle)
            self.create_line(x_start, y_start, x_end, y_end, width=4, fill=self.border_color)

        # Draw numbers 1 to 12
        for i in range(1, 13):
            angle = math.pi / 6 * (i - 3)
            x = self.center + (self.radius - 50) * math.cos(angle)
            y = self.center + (self.radius - 50) * math.sin(angle)
            self.create_text(x, y, text=str(i), font=('Segoe UI', 18, 'bold'),
                             fill=self.number_color)

    def update_clock(self):
        self.delete('hands')

        t = localtime()
        sec = t.tm_sec + t.tm_sec / 10  # smooth movement with extra precision (optional)
        min = t.tm_min + sec / 60
        hr = t.tm_hour % 12 + min / 60

        # Calculate angles
        sec_angle = math.pi * 2 * (sec / 60) - math.pi / 2
        min_angle = math.pi * 2 * (min / 60) - math.pi / 2
        hr_angle = math.pi * 2 * (hr / 12) - math.pi / 2

        # Second hand
        sec_x = self.center + (self.radius - 40) * math.cos(sec_angle)
        sec_y = self.center + (self.radius - 40) * math.sin(sec_angle)
        self.create_line(self.center, self.center, sec_x, sec_y,
                         fill=self.sec_hand_color, width=2, tag='hands')

        # Minute hand
        min_x = self.center + (self.radius - 70) * math.cos(min_angle)
        min_y = self.center + (self.radius - 70) * math.sin(min_angle)
        self.create_line(self.center, self.center, min_x, min_y,
                         fill=self.min_hand_color, width=5, tag='hands')

        # Hour hand
        hr_x = self.center + (self.radius - 110) * math.cos(hr_angle)
        hr_y = self.center + (self.radius - 110) * math.sin(hr_angle)
        self.create_line(self.center, self.center, hr_x, hr_y,
                         fill=self.hour_hand_color, width=8, tag='hands')

        # Center circle
        self.create_oval(self.center - 12, self.center - 12,
                         self.center + 12, self.center + 12,
                         fill=self.border_color, tag='hands')

        self.after(100, self.update_clock)  # update every 100 ms for smooth seconds

    def toggle_mode(self):
        if self.bg_color == 'white':
            # Switch to dark mode
            self.bg_color = '#222831'
            self.face_color = '#393e46'
            self.border_color = '#00adb5'
            self.hour_hand_color = '#eeeeee'
            self.min_hand_color = '#00adb5'
            self.sec_hand_color = '#ff5722'
            self.number_color = '#eeeeee'
            self.configure(bg=self.bg_color)
        else:
            # Switch to light mode
            self.bg_color = 'white'
            self.face_color = '#a3d2ca'
            self.border_color = '#5eaaa8'
            self.hour_hand_color = '#056676'
            self.min_hand_color = '#028090'
            self.sec_hand_color = '#f95738'
            self.number_color = '#056676'
            self.configure(bg=self.bg_color)

        self.draw_clock_face()


if __name__ == '__main__':
    root = tk.Tk()
    root.title("Colorful Analog Clock")
    root.geometry("450x500")
    root.resizable(False, False)

    clock = AnalogClock(root, size=400)
    clock.pack(pady=20)

    # Toggle Button
    toggle_btn = tk.Button(root, text="Toggle Light/Dark Mode", command=clock.toggle_mode,
                           font=('Segoe UI', 12, 'bold'), bg='#00adb5', fg='white',
                           activebackground='#028090', activeforeground='white')
    toggle_btn.pack(pady=10)

    root.mainloop()
