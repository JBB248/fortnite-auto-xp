from tkinter import *

class TaskWindow(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)

        self.wm_title("Fortnite AFK XP Bot")

        menu = Menu(self)
        task_menu = Menu(menu)
        task_menu.add_command(label="New task")
        help_menu = Menu(menu)
        help_menu.add_command(label="Report issue")
        menu.add_cascade(label="Task", menu=task_menu)
        menu.add_cascade(label="Help", menu=help_menu)
        self.config(menu=menu)

        container = Frame(self, width=400)
        container.pack(expand=True)

        frame = PromptFrame(container, self)
        frame.tkraise()

class PromptFrame(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        mode = IntVar(value=1)
        self.mode = mode
        Label(text="Mode").pack(anchor=W)
        Radiobutton(text="LEGO Fortnite", variable=mode, value=1).pack(anchor=W, pady=2.5)
        Radiobutton(text="Fortnite Jam Festival", variable=mode, value=2).pack(anchor=W, pady=2.5)

        Label(text="").pack(anchor=W)

        duration = IntVar(value=1)
        self.duration = duration
        Label(text="Duration").pack(anchor=W)
        Radiobutton(text="30 minutes", variable=duration, value=1).pack(anchor=W, pady=2.5)
        Radiobutton(text="1 hour", variable=duration, value=2).pack(anchor=W, pady=2.5)
        Radiobutton(text="3 hours (Time till max XP)", variable=duration, value=3).pack(anchor=W, pady=2.5)
        Radiobutton(text="Custom", justify=LEFT, variable=duration, value=4).pack(anchor=W, pady=2.5)
        Entry().pack(anchor=W, padx=20)
        Label(text="Format: HOUR:MIN:SEC (ex. 2:30:00)").pack(anchor=W, padx=17)

        button = Button(text="Start bot").pack(anchor=W, padx=10, pady=10)

window = TaskWindow()
window.mainloop()