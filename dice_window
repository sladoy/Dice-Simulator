import webbrowser
from tkinter import Tk, Label, Entry, Button
import pygal

from die import Die


class WindowFunctions:
    def __init__(self, root):
        self.root = root
        self.dice = Die()

        self.label_sides = Label (self.root, text='Side number:')
        self.label_sides.pack()

        self.entry_side = Entry (self.root)
        self.entry_side.pack()

        self.label_throw = Label (self.root, text='Number of dice rolls:')
        self.label_throw.pack()

        self.entry_throw = Entry (self.root)
        self.entry_throw.pack()

        self.label_dice = Label (self.root, text='Number of dices:')
        self.label_dice.pack()

        self.entry_dice = Entry (self.root)
        self.entry_dice.pack()

        self.button_generate = Button(self.root, text='Generate', command=self.taking)
        self.button_generate.pack()

        self.button_show = Button(self.root, text='Show created File', command=self.show)
        self.button_show.pack()

    def taking(self):
        try:
            side_value = int(self.entry_side.get())
            throw_value = int(self.entry_throw.get())
            die_value = int(self.entry_dice.get())
        except(TypeError, ValueError):
            self.window_value()
        else:
            self.dice.generate_sides (side_value)
            result = self.dice.generate_results (throw_value, die_value)
            frequencies = self.dice.generate_frequencies (result)

            dies = self.dice.generate_dies()

            hist = pygal.Bar()

            hist.title = 'Results'
            hist.x_labels = self.dice.generate_labels( )
            hist.y_title = 'Frequencies'
            hist.x_title = 'Results'

            hist.add (dies, frequencies)
            hist.render_to_file ('die_visual.svg')

    def show(self):
        try:
            l = open('die_visual.svg')
        except FileNotFoundError:
            self.window_file()
        else:
            l.close()
            webbrowser.open ('die_visual.svg')

    def window_value(self):
        frame = Tk()
        frame.bind('<Escape>', quit)
        label = Label(frame, text="Something went wrong. Try to input integer values.")
        label.pack()
        button = Button(frame, text='Ok', command=frame.destroy)
        button.pack()
        frame.mainloop()

    def window_file(self):
        frame = Tk ( )
        frame.bind ('<Escape>', quit)
        label = Label (frame, text="File not found. Are you sure that you file is generated?")
        label.pack ( )
        button = Button (frame, text='Ok', command=frame.destroy)
        button.pack ( )
        frame.mainloop ( )


if __name__ == '__main__':
    root = Tk()
    root.bind('<Escape>', quit)
    root.title('Dice Simulator')
    root.geometry('300x200')
    window = WindowFunctions(root)

    root.mainloop()





