from tkinter import *
from tkinter import filedialog
import json
from tkinter.ttk import Combobox
import tkinter.font
from tkinter.colorchooser import *
from tkinter import messagebox


class Paint(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.object_id = []
        self.parent = parent
        self.figure = IntVar()
        self.initUI()
        self.figure.set(0)
        self.size = 10
        self.fill_color = "#000000"
        self.outline_color = '#000000'
        self.start_x = 0
        self.start_y = 0
        self.object = None
        self.text = ""

    def draw(self, event):
        if self.figure.get() == 6:
            pass
        elif self.figure.get():
            self.resize_Elements(event)
        elif self.figure.get() == 0:
            self.canv.create_oval(event.x - self.size,
                                  event.y - self.size,
                                  event.x + self.size,
                                  event.y + self.size,
                                  fill=self.fill_color, outline=self.fill_color)


    def set_size(self, size):
        self.size = size

    def initUI(self):
        self.pack(fill=BOTH, expand=1)

        self.columnconfigure(9, weight=1)
        self.rowconfigure(2, weight=1)

        self.canv = Canvas(self, bg="white")
        self.canv.grid(row=2, column=0, columnspan=10, padx=5, pady=5, sticky=E + W + S + N)
        self.canv.bind("<B1-Motion>", self.draw)
        self.canv.bind("<Button-1>", self.startDraw)
        self.bind_all("<Key>", self.appendChar)
        self.bind_all("<Return>", self.clearString)

        self.fill_btn = Button(self, text='Fill', bg='Black', fg='White', width=10, height=2, command=self.setColorFill)
        self.fill_btn.grid(row=1, column=0, sticky=W)

        self.out_fill_btn = Button(self, text='OutFill', width=10, height=2, command=self.setColorOutline)
        self.out_fill_btn.grid(row=1, column=1 )

        self.btn_clear = Button(self, text="Clear", width=10, height=2, fg='red', command=lambda: self.canv.delete("all"))
        self.btn_clear.grid(row=1, column=3, sticky=W)

        self.void= Label(self, width=20)
        self.void.grid(row=1, column=5)

        self.save_btn=Button(self, text='Save as', width=10, height=2, bg='Black', fg='yellow', command=self.save_file)
        self.save_btn.grid(row=1, column=7)

        self.open_btn = Button(self, text='Open File', width=10, height=2, bg='Black', fg='yellow', command=self.open_file)
        self.open_btn.grid(row=1, column=8, sticky=E)


        def active_spin():
            self.void.grid_forget()
            self.lb=Label(self, text='Rangers Arc:')
            self.start_SpinBox = Spinbox(self, from_=0, to=359, width=4, value=0)
            self.over_SpinBox = Spinbox(self, from_=0, to=359, width=4, value=358)
            self.start_SpinBox.grid(row=1, column=5)
            self.over_SpinBox.grid(row=1, column=6)
            self.lb.grid(row=1, column=4)

        def nonactive_spin():
            self.start_SpinBox.grid_forget()
            self.over_SpinBox.grid_forget()
            self.lb.grid_forget()
            self.void = Label(self, width=20)
            self.void.grid(row=1, column=5)

        var = IntVar()
        var.set(0)
        Radiobutton(text="Кисть", variable=self.figure, indicator=0,width=5, command=nonactive_spin, value=0).pack(side='left')
        Radiobutton(text="Arc", variable=self.figure,indicator=0,width=5, command=active_spin, value=1).pack(side='left')
        Radiobutton(text="Oval", variable=self.figure,indicator=0,width=5, command=nonactive_spin, value=2).pack(side='left')
        Radiobutton(text="Text", variable=self.figure,indicator=0,width=5 ,command=nonactive_spin, value=3).pack(side='left')
        Radiobutton(text="Rect", variable=self.figure,indicator=0,width=5 ,command=nonactive_spin, value=4).pack(side='left')
        Radiobutton(text="Line", variable=self.figure,indicator=0,width=5, command=nonactive_spin, value=5).pack(side='left')

    def setColorFill(self):
        color = askcolor()[1]
        print(self.object_id)
        self.fill_color = color

    def setColorOutline(self):
        color = askcolor()[1]
        self.outline_color = color

    def startDraw(self, event):
        self.start_x = event.x
        self.start_y = event.y
        if self.figure.get() == 1:
            try:
                startAng = int(self.start_SpinBox.get())
                delta = int(self.over_SpinBox.get()) - startAng
                self.object = self.canv.create_arc(event.x, event.y,
                                                   event.x, event.y,
                                                   start=startAng, extent=delta,
                                                   style=ARC, outline=self.outline_color, fill = self.fill_color)
            except ValueError:
                messagebox.showinfo('ValueError', 'Please type num')

        elif self.figure.get() == 2:
            self.object = self.canv.create_oval(event.x, event.y,
                                                event.x, event.y,
                                                outline=self.outline_color,fill = self.fill_color)
        elif self.figure.get() == 3:
            self.object = self.canv.create_text(event.x, event.y, font='Verdana', fill=self.fill_color, anchor = SW)
        elif self.figure.get() == 4:
            self.object = self.canv.create_rectangle(event.x, event.y,
                                                     event.x, event.y,
                                                     outline=self.outline_color,fill= self.fill_color)
        elif self.figure.get() == 5:
            self.object = self.canv.create_line(event.x, event.y,
                                                event.x, event.y,
                                                fill=self.fill_color)


    def resize_Elements(self, event):
        self.canv.coords(self.object, self.start_x, self.start_y, event.x, event.y)

    def appendChar(self, event):
        if self.figure.get() == 3:
            if self.object:
                self.text = self.text + str(event.char)
                self.canv.itemconfigure(self.object, text=self.text)

    def clearString(self, event):
        self.object = None
        self.text = ""

    def save_file(self):
        ftypes = (("Файл", ""),)
        file = filedialog.asksaveasfilename(title="Открыть файл", initialdir="/",
                                            filetypes=ftypes)
        with open(file, 'w') as file:
            for item in self.canv.find_all():
                print(json.dumps({
                    'type': self.canv.type(item),
                    'coords': self.canv.coords(item),
                    'options': {key: val[-1] for key, val in self.canv.itemconfig(item).items()}
                }), file=file)

    def open_file(self):
        ftypes = (("Файл", ""),)
        file = filedialog.askopenfilename(title="Открыть файл", filetypes=ftypes)
        funcs = {
            'arc': self.canv.create_arc,
            'line': self.canv.create_line,
            'oval': self.canv.create_oval,
            'rectangle': self.canv.create_rectangle,
            'text': self.canv.create_text,
        }
        with open(file) as f:
            for line in f:
                item = json.loads(line)
                if item['type'] in funcs:
                    funcs[item['type']](item['coords'], **item['options'])


if __name__ == "__main__":
    root = Tk()
    root.title('КБ-191')
    root.geometry("1000x600+100+100")
    app = Paint(root)
    root.mainloop()