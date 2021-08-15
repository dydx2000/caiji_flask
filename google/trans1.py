# -*- coding: utf-8 -*-
"""
 @Time : 2021/7/8 20:31
 @Author : PeterYang
 @File : trans1.py
"""
from googletrans import Translator
translator = Translator()

def detect(str):
    result = translator.detect(str)
    print(result)

detect("how are you")
