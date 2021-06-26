from tkinter import *


class Application(Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.creatWidget()

    def creatWidget(self):
        self.label01 = Label(self, text="百战程序员", width=10,
                             height=2, bg="black", fg="white")
        self.label01.pack()

        self.label02 = Label(self, text="黑马程序员", width=12,
                             height=3, bg="white", fg="black")
        self.label02['text'] = '达达杀猪菜'
        self.label02.pack()

        global photo
        photo = PhotoImage(file="logo.gif", width=100, height=50)
        photo.zoom(x=1, )
        self.label03 = Label(self, image=photo)
        self.label03.pack()

        self.label04 = Label(self, text="北京尚学堂\n百战程序员", width=12,
                             height=3, borderwidth=1, relief="solid", justify="right", bg="white", fg="black",anchor='w')

        self.label04.pack()


if __name__ == '__main__':
    root = Tk()
    root.geometry("400x500+200+300")
    app = Application(master=root)
    root.mainloop()
