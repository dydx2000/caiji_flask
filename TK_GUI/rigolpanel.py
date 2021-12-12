# -*- coding: utf-8 -*-
"""
 @Time : 2021/12/12 下午1:24
 @Author : PeterYang
 @File : rigolpanel.py
"""
from tkinter import *
from tkinter import ttk

root = Tk()

la1_1 = Label(root, text='通      道', font=14)
la1_1.grid(row=0, column=0, sticky=W, pady=(15, 0), padx=(15, 15), )  # 0行0列

cmb = ttk.Combobox(root, width=12,font=14)
cmb['value'] = ('CH1', 'CH2', 'CH3')
cmb.current(0)
cmb.grid(row=0, column=1, pady=(20, 0), padx=(15, 15), sticky="w")

# 当前电压
la2_1 = Label(root, text='当前电压', font=14)
la2_1.grid(row=1, column=0, sticky=W, pady=15, padx=(15, 15), )  # 0行0列

# 电压输入输出
current_volt = Entry(root, font=14,width =14, )
# current_volt.delete(0, "end")
# current_volt.insert(0, "30")
current_volt.grid(row=1, column=1, sticky=W, pady=(20, 0), padx=(15, 15), )

# 电压单位
la2_2 = Label(root, text="V")
la2_2.grid(row=1, column=2, sticky=W, pady=(20, 0), padx=(0, 15), )

# 查询
querycv = Button(root, text="查询", width=5, font=14)
querycv.grid(row=2, column=1, pady=10, padx=(15, 0), sticky=W)

# 设置
query_v = Button(root, text="设置", width=5, font=14)
query_v.grid(row=2, column=1, pady=10, padx=(45, 0))

# 当前电流
la3_1 = Label(root, text='当前电流', font=14)
la3_1.grid(row=3, column=0, sticky=W, pady=(20, 0), padx=(15, 15), )

# 电流输入输出
current_curr = Entry(root,font=14,width=14)
# current_curr.delete(0, "end")
# current_curr.insert(0, "3.1")
current_curr.grid(row=3, column=1, sticky=W, pady=(20, 0), padx=(15, 15), )

# 电流单位
la3_2 = Label(root, text="A", )
la3_2.grid(row=3, column=2, sticky=W, pady=(20, 0), )

# 查询
query_c = Button(root, text="查询", width=5, font=14)
query_c.grid(row=4, column=1, pady=10, padx=(15, 0), sticky=W)

# 设置
query_v = Button(root, text="设置", width=5, font=14)
query_v.grid(row=4, column=1, pady=10, padx=(45, 0))

# 电源开关
la3_1 = Label(root, text='电源开关', font=14)
la3_1.grid(row=5, column=0, sticky=W, pady=10, padx=(15, 15), )

switch_on = Button(root, text="开", width=5, font=14)
switch_on.grid(row=5, column=1, pady=10, padx=(15, 0), sticky=W)

switch_off = Button(root, text="关", width=5, font=14)
switch_off.grid(row=5, column=1, pady=10, padx=(45, 0))

root.mainloop()
