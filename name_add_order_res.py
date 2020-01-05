# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 18:30:58 2019

@author: Iida_Tetsuya
"""

import pyperclip

text = pyperclip.paste()

pyperclip.copy('お世話になっております。\n\n' + text +'様承りました。\n\n' + '何卒宜しくお願い申し上げます。')