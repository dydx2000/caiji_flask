from tkinter import *
from tkinter import messagebox


class Application(Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.creatWidget()

    def creatWidget(self):
        self.w1 = Text(root,width=40,height=12,bg="gray")
        self.w1.pack()
        self.w1.insert(1.0,"锄禾日当午,汗 滴禾下土.\n粒粒皆辛苦.")


    def login(self):
        print(self.user_entry.get())
        print(self.v1.get())
        if self.v1.get() == 'admin':

            messagebox.showinfo("自学GUI", "登录成功,开始学习.")
        else:
            messagebox.showinfo("警告.","登录失败")


if __name__ == '__main__':
    root = Tk()
    root.geometry("200x200+200+300")
    app = Application(master=root)
    root.mainloop()
