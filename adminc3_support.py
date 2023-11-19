#! /usr/bin/env python3
#  -*- coding: utf-8 -*-
#

import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *
import adminc3
import functapp


_debug = False# Отключение отдадочной онформации из функций обратного вызова

def main(*args):
    '''Главная точка входа приложения'''
    global root
    root = tk.Tk()
    root.protocol( 'WM_DELETE_WINDOW' , root.destroy)
    # Creates a toplevel widget.
    global _top1, _w1
    _top1 = root
    _w1 = adminc3.Toplevel1(_top1)#переменная объекта главного окна
    root.mainloop()

if __name__ == '__main__':
    adminc3.start_up()




