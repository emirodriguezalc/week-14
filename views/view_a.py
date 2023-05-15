import tkinter as tk
from view_b import ViewB

class ViewA:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('View A')

        self.label = tk.Label(self.root, text='Hello, world!')
        self.label.pack()

        self.button = tk.Button(self.root, text='Go to View B', command=self.go_to_view_b)
        self.button.pack()

    def go_to_view_b(self):
        self.root.destroy()
        view_b = ViewB()
        view_b.run()

    def run(self):
        self.root.mainloop()
