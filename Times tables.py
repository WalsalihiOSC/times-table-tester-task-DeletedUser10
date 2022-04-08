"""Times table task"""

from tkinter import*
import random

class Interface:
    def __init__(self, parent):
        self.times = Times()

        main_frame = Frame(parent, bg = "White")
        main_frame.grid()
        title = Label(main_frame, text = "Times Table Checker", font="Bold", bg="White")
        title.grid(row=0, column=3, sticky=E)

        self.ql = Label(main_frame, text = "", font="Arial")
        self.ql.grid(row=1, column=2)

        self.en = Entry(main_frame)
        self.en.grid(row=1, column=3)

        check_b = Button(main_frame, text = "Check Answer", command= self.check, bg="White")
        check_b.grid(row=3, column=3)
            
        self.next_b = Button(main_frame, text = "Next",command=self.next, bg="White")
        self.next_b.grid(row=3, column=4)

        self.checkl = Label(main_frame, text = "", bg = "White")
        self.checkl.grid(row=1, column=4)

        self.next()

    def check(self):
        if self.times.check_ans(self.en.get()):
            self.checkl.configure(text = "Correct", font = "Arial")
        else:
             self.checkl.configure(text = "Incorrect", font = "Arial")
        
        self.en.delete(0,END)

    def next(self):
        self.times.moreq()
        self.ql.configure(text = f"{self.times.numb1} x {self.times.numb2} = ", bg = "White")
        self.checkl.configure(text="", font="Arial")

        

class Times:
    def __init__(self):
        self.numb1 = random.randint(1,10)
        self.numb2 = random.randint(1,10)
    def moreq(self):
        self.numb1 = random.randint(1,10)
        self.numb2 = random.randint(1,10)

    """Method that returns multiplication of the random numbers """
    def check_ans(self, multiply):
        return multiply == str(self.numb1*self.numb2)  



def main():
    root = Tk()
    Interface(root)
    root.geometry("360x100")
    root.title("Times Table Checker")
    root.configure(bg="white")

    root.mainloop()

main()