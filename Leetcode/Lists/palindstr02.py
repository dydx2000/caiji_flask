# -*- coding: utf-8 -*-
"""
 @Time : 2021/8/17 22:29
 @Author : PeterYang
 @File : palindstr02.py
 """


def huiwen2(string):
    def isPalind(i, j):
        while i < j:
            if string[i] != string[j]:
                return False
            i += 1
            j -= 1
        return True

    string = list(string)
    i = 0
    j = len(string) - 1
    while i < j:
        if string[i] != string[j]:
            return isPalind(i + 1, j) or isPalind(i, j - 1)

        i += 1
        j -= 1
    return True


if __name__ == '__main__':
    print(huiwen2("abce2e34cba"))
