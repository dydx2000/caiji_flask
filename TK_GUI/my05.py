from tkinter import *
from tkinter import messagebox


class Application(Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.creatWidget()


    def creatWidget(self):

        f1 =Frame(root)
        root.grid_rowconfigure(1, weight=1, minsize=80)
        root.grid_columnconfigure(0, weight=1, minsize=96)
        self.label01 = Label(f1, text='用户名').pack(side='left')
        self.v1 = StringVar()
        self.v1.set('admin')
        self.user_entry = Entry(f1, textvariable=self.v1)
        self.user_entry.pack(side='left')
        f1.pack()

        f2 = Frame(root)
        self.lbbbel02 = Label(f2, text="密码").pack(side='left',pady =10)
        self.pass_entry = Entry(f2, show='*').pack(side='right')
        f2.pack()

        self.btn01 = Button(root, text="确定",  height=1,pady=5,
                            anchor="sw", command=self.login).pack()

    def login(self):
        print(self.user_entry.get())
        print(self.v1.get())
        if self.v1.get() == 'admin':

            messagebox.showinfo("自学GUI", "登录成功,开始学习.")
        else:
            messagebox.showinfo("警告.","登录失败")


if __name__ == '__main__':
    root = Tk()
    # root.geometry("200x200+200+300")
    app = Application(master=root)
    root.mainloop()
