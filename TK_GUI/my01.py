from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("我的第一个GUI程序")
root.geometry("500x300+200+100")


def songhua():
    messagebox.showinfo("Message", "送你一朵小花")
    print("give you a flower.")


btn = Button(root, text='hello',command=songhua)
btn.pack()



mainloop()
