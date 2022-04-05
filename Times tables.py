"""Times table task"""

from tkinter import*
import random

class Times:
    def __init__(self, parent):
        main_frame = Frame(parent, bg = "White")
        main_frame.grid()
        title = Label(main_frame, text = "Times table checker", font="Bold", bg="White")
        title.grid(row=0, column=3, sticky=E)

        self.ql = Label(main_frame, text = "", font="Arial")
        self.ql.grid(row=1, column=2)

        self.en = Entry(main_frame)
        self.en.grid(row=1, column=3)

        check_b = Button(main_frame, text = "Check Answer", command= self.check, bg="White")
        check_b.grid(row=3, column=2)
            
        self.next_b = Button(main_frame, text = "next", command= self.next, bg="White")
        self.next_b.grid(row=3, column=3)

        self.checkl = Label(main_frame, text = "", bg = "White")
        self.checkl.grid(row=1, column=4)

        self.next()

    def next(self):
        numb1 = random.randint(1,10)
        numb2 = random.randint(1,10)
        self.multiply = str(numb1*numb2)

        self.ql.configure(text = f"{numb1} x {numb2} = ", bg = "White")
        self.checkl.configure(text="", font="Arial")
   
    def check(self):
        if self.en.get() != self.multiply:
            self.checkl.configure(text="incorrect", font="Arial")
        
        else:
             self.checkl.configure(text="correct", font= "Arial")
        
        self.en.delete(0,END)


def main():
    root = Tk()
    Times(root)
    root.geometry("350x100")
    root.configure(bg="white")

    root.mainloop()

main()