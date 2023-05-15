import tkinter as tk
from view_a import ViewA

class ViewB:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('View B')

        self.label = tk.Label(self.root, text='Welcome to View B!')
        self.label.pack()

        self.button = tk.Button(self.root, text='Go back to View A', command=self.go_to_view_a)
        self.button.pack()

    def go_to_view_a(self):
        self.root.destroy()
        view_a = ViewA()
        view_a.run()

    def run(self):
        self.root.mainloop()
