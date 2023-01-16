import tkinter as tk
import tkinter.messagebox as mb
import random as rnd


class Window_start(tk.Tk):
    def __init__(self):
        super().__init__()
        self.protocol("WM_DELETE_WINDOW", self.confirm_delete)
        self.title("Greeting")
        self.geometry('500x250')
        self.frame_1 = tk.Frame(master=self)
        self.label = tk.Label(master=self.frame_1, text="Введите имя Игрока", font=("Arial Bold", 20))
        self.label.pack()
        self.frame_2 = tk.Frame(master=self)
        self.entry = tk.Entry(master=self.frame_2, width=40, font=("Arial Bold", 15))
        self.entry.pack()
        self.entry.focus()
        self.frame_3 = tk.Frame(master=self)
        self.button_exit = tk.Button(master=self.frame_3, text="Выход", command=self.clicked_exit, width=10, height=2, bg="IndianRed",
                                fg="white", font=("Arial Bold", 15))
        self.button_exit.grid(column=0, row=0, padx=10, pady=10, sticky="")
        self.button_2 = tk.Button(master=self.frame_3, text="Далее!", command=self.clicked_next, width=10, height=2, bg="DarkGreen",
                             fg="white", font=("Arial Bold", 15))
        self.button_2.grid(column=1, row=0, padx=10, pady=10, sticky="")
        self.frame_3.grid_columnconfigure([0, 1], weight=1, minsize=50)
        self.frame_3.grid_rowconfigure(0, weight=1, minsize=75)
        self.frame_1.pack(fill=tk.BOTH, side=tk.TOP, expand=True)
        self.frame_2.pack(fill=tk.BOTH, side=tk.TOP, expand=True)
        self.frame_3.pack(fill=tk.BOTH, side=tk.TOP, expand=True)

    def confirm_delete(self):
        message = "Вы уверены, что хотите закрыть это окно?"
        if mb.askyesno(message=message, parent=self):
            self.destroy()

    def clicked_exit(self):
        self.destroy()

    def clicked_next(self):
        self.name = self.entry.get()
        with open("name.txt", "w") as inf:
            inf.write(self.name)
        window_next = Window_next()
        window_next.grab_set()
        self.destroy()

class Window_next(tk.Tk):
    def __init__(self):
        super().__init__()
        self.protocol("WM_DELETE_WINDOW", self.confirm_delete)
        self.title("Guess the number")
        self.geometry('700x250')
        with open("name.txt", "r") as inf:
            self.name = inf.read()
        self.number_res = rnd.randint(0, 101)
        self.frame_1 = tk.Frame(master=self)
        self.label = tk.Label(master=self.frame_1, text=f"Добрый день, {self.name}, введите целое число от 0 до 100:", font=("Arial Bold", 20))
        self.label.pack()
        self.frame_2 = tk.Frame(master=self)
        self.entry = tk.Entry(master=self.frame_2, width=20, font=("Arial Bold", 15))
        self.entry.pack()
        self.entry.focus()
        self.frame_3 = tk.Frame(master=self)
        self.button = tk.Button(master=self.frame_3, text="Мне повезет!", command=self.clicked, width=15, height=2, bg="DarkGreen",
                               fg="white", font=("Arial Bold", 15))
        self.button.pack()
        self.number_try = 7
        self.frame_4 = tk.Frame(master=self)
        self.label_try = tk.Label(master=self.frame_4, text=f"Осталось попыток: {self.number_try}",
                              font=("Arial Bold", 20))
        self.label_try.pack()
        self.frame_1.pack(fill=tk.BOTH, side=tk.TOP, expand=True)
        self.frame_2.pack(fill=tk.BOTH, side=tk.TOP, expand=True)
        self.frame_3.pack(fill=tk.BOTH, side=tk.TOP, expand=True)
        self.frame_4.pack(fill=tk.BOTH, side=tk.TOP, expand=True)

    def clicked(self):
        self.number_in = self.entry.get()
        try:
            self.number_in = int(self.number_in)
            if self.number_in < 0 or self.number_in > 100:
                res = "Число не в указанном диапазоне"
            else:
                if self.number_in > self.number_res:
                    res = f"Искомое число меньше чем {self.number_in}"
                    self.number_try -= 1
                    if self.number_try == 0:
                        res = f"Сожалею, {self.name}, Вы проиграли :("
                        self.entry.configure(state='disabled')
                        self.button.configure(state='disabled')
                elif self.number_in < self.number_res:
                    res = f"Искомое число больше чем {self.number_in}"
                    self.number_try -= 1
                    if self.number_try == 0:
                        res = f"Сожалею, {self.name}, Вы проиграли :("
                        self.entry.configure(state='disabled')
                        self.button.configure(state='disabled')
                else:
                    res = f"Поздравляю, {self.name}! Вы угадали число!"
                    self.entry.configure(state='disabled')
                    self.button.configure(state='disabled')
        except ValueError:
            res = "Это не целое число"
        self.label.configure(text=res)
        self.label_try.configure(text=f"Осталось попыток: {self.number_try}")

    def confirm_delete(self):
        message = "Вы уверены, что хотите закрыть это окно?"
        if mb.askyesno(message=message, parent=self):
            self.destroy()

if __name__ == "__main__":
    window_start = Window_start()
    window_start.mainloop()

