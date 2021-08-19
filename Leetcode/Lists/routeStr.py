# -*- coding: utf-8 -*-
"""
 @Time : 2021/8/17 23:11
 @Author : PeterYang
 @File : routeStr.py
"""
def routestr(string,tarstr):
    if len(string)!= len(tarstr):
        return False
    dobstr = string*2
    print(dobstr)
    return tarstr in dobstr



print(routestr("abcde", "abcd"))