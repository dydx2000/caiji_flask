from tkinter import *
from tkinter.filedialog import askopenfilename


class Application(Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.creatWidget()

    def creatWidget(self):
        self.btn01 = Button(root, pady=10, text="打开文件", width=20, height=1,
                            command=self.test1)

        self.btn01.pack()

    def test1(self):
        f = askopenfilename(title='上转文件',
                            initialdir=".\\", filetypes=[("python文件_", '.py')])


if __name__ == '__main__':
    root = Tk()
    root.geometry("400x100+200+300")
    app = Application(master=root)
    root.mainloop()
