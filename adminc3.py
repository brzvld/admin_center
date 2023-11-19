#! /usr/bin/env python3
#  -*- coding: utf-8 -*-
#

import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *
import os.path
import adminc3_support
import functapp
import tkinter.messagebox as msgbox
from tkinter.scrolledtext import ScrolledText



_script = sys.argv[0]
_location = os.path.dirname(_script)

#назначение цветовым переменным значений
_bgcolor = '#d9d9d9'  # X11 color: 'gray85'
_fgcolor = '#000000'  # X11 color: 'black'
_compcolor = 'gray40' # X11 color: #666666
_ana1color = '#c3c3c3' # Closest X11 color: 'gray76'
_ana2color = 'beige' # X11 color: #f5f5dc
_tabfg1 = 'black' 
_tabfg2 = 'black' 
_tabbg1 = 'grey75' 
_tabbg2 = 'grey89' 
_bgmode = 'light' 

_style_code_ran = 0
def _style_code():
    global _style_code_ran
    if _style_code_ran:
       return
    style = ttk.Style()
    if sys.platform == "win32":
       style.theme_use('winnative')
    style.configure('.',background=_bgcolor)
    style.configure('.',foreground=_fgcolor)
    style.configure('.',font='TkDefaultFont')
    style.map('.',background =
       [('selected', _compcolor), ('active',_ana2color)])
    if _bgmode == 'dark':
       style.map('.',foreground =
         [('selected', 'white'), ('active','white')])
    else:
       style.map('.',foreground =
         [('selected', 'black'), ('active','black')])
    style.map('TNotebook.Tab', background =
            [('selected', _bgcolor), ('active', _tabbg1),
            ('!active', _ana2color)], foreground =
            [('selected', _fgcolor), ('active', _tabfg1), ('!active',  _tabfg2)])
    _style_code_ran = 1

class Toplevel1:
    def __init__(self, top=None):
        '''Класс окна верхнего уровня(top)'''

        top.geometry("585x458+364+390")
        top.minsize(1, 1)
        top.maxsize(1265, 994)
        top.resizable(1,  1)
        top.title("AdminCentr")
        top.configure(highlightcolor="black")

        self.top = top

        self.menubar = tk.Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)

        self.sub_menu = tk.Menu(self.menubar, activebackground='beige'
                ,activeforeground='black', tearoff=0)
        self.menubar.add_cascade(compound='left', label='Файл', menu=self.sub_menu
                ,)
        self.sub_menu.add_command(compound='left', label='Сохранить отчет как..', command=functapp.save_report)

        self.sub_menu.add_command(compound='left',label='Выход', command=functapp.exit_app)
        self.sub_menu1 = tk.Menu(self.menubar, activebackground='beige'
                ,activeforeground='black', tearoff=0)
        self.menubar.add_cascade(compound='left', label='Справка'
                ,menu=self.sub_menu1, )
        self.sub_menu1.add_command(compound='left',label='О программе',command=functapp.show_about)
        _style_code()
        self.TNotebook1 = ttk.Notebook(self.top)
        self.TNotebook1.place(relx=0.017, rely=0.0, relheight=0.493
                , relwidth=0.961)
        self.TNotebook1.configure(takefocus="")
        self.TNotebook1_t1 = tk.Frame(self.TNotebook1)
        self.TNotebook1.add(self.TNotebook1_t1, padding=3)
        self.TNotebook1.tab(0, text='''Ping''', compound="left"
                ,underline='''-1''', )
        self.TNotebook1_t2 = tk.Frame(self.TNotebook1)
        self.TNotebook1.add(self.TNotebook1_t2, padding=3)
        self.TNotebook1.tab(1, text='''Scan''', compound="left"
                ,underline='''-1''', )
        self.Listbox1 = ScrolledText(self.TNotebook1_t1)
        self.Listbox1.place(relx=0.018, rely=0.2, relheight=0.43, relwidth=0.204)

        self.Listbox1.configure(background="white")
        self.Listbox1.configure(font="TkFixedFont")
        self.Listbox1.configure(selectbackground="#c4c4c4")
        self.Label2 = tk.Label(self.TNotebook1_t1)
        self.Label2.place(relx=0.036, rely=0.05, height=21, width=105)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(anchor='w')
        self.Label2.configure(compound='left')
        self.Label2.configure(text='''Список хостов''')
        self.Button2 = tk.Button(self.TNotebook1_t1)
        self.Button2.place(relx=0.036, rely=0.7, height=33, width=98)
        self.Button2.configure(activebackground="beige")
        self.Button2.configure(borderwidth="2")
        self.Button2.configure(compound='left')
        self.Button2.configure(text='''Очистить''',command=functapp.clean_ping_list)
        self.Entry1 = tk.Entry(self.TNotebook1_t1)
        self.Entry1.place(relx=0.339, rely=0.2, height=23, relwidth=0.207)
        self.Entry1.configure(background="white")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(selectbackground="#c4c4c4")
        self.Label3 = tk.Label(self.TNotebook1_t1)
        self.Label3.place(relx=0.393, rely=0.05, height=21, width=36)
        self.Label3.configure(activebackground="#f9f9f9")
        self.Label3.configure(anchor='w')
        self.Label3.configure(compound='left')
        self.Label3.configure(text='''Хост''')
        self.Label4 = tk.Label(self.TNotebook1_t1)
        self.Label4.place(relx=0.75, rely=0.05, height=21, width=105)
        self.Label4.configure(activebackground="#f9f9f9")
        self.Label4.configure(anchor='w')
        self.Label4.configure(compound='left')
        self.Label4.configure(text='''Группа хостов''')
        self.Entry2 = tk.Entry(self.TNotebook1_t1)
        self.Entry2.place(relx=0.661, rely=0.2, height=23, relwidth=0.154)
        self.Entry2.configure(background="white")
        self.Entry2.configure(font="TkFixedFont")
        self.Entry2.configure(selectbackground="#c4c4c4")
        self.Entry3 = tk.Entry(self.TNotebook1_t1)
        self.Entry3.place(relx=0.661, rely=0.4, height=23, relwidth=0.154)
        self.Entry3.configure(background="white")
        self.Entry3.configure(font="TkFixedFont")
        self.Entry3.configure(selectbackground="#c4c4c4")
        self.Label5 = tk.Label(self.TNotebook1_t1)
        self.Label5.place(relx=0.839, rely=0.2, height=21, width=57)
        self.Label5.configure(activebackground="#f9f9f9")
        self.Label5.configure(anchor='w')
        self.Label5.configure(compound='left')
        self.Label5.configure(text='''первый''')
        self.Label6 = tk.Label(self.TNotebook1_t1)
        self.Label6.place(relx=0.839, rely=0.4, height=21, width=82)
        self.Label6.configure(activebackground="#f9f9f9")
        self.Label6.configure(anchor='w')
        self.Label6.configure(compound='left')
        self.Label6.configure(text='''Последний''')
        self.Button4 = tk.Button(self.TNotebook1_t1)
        self.Button4.place(relx=0.661, rely=0.7, height=33, width=151)
        self.Button4.configure(activebackground="beige")
        self.Button4.configure(borderwidth="2")
        self.Button4.configure(compound='left')
        self.Button4.configure(state='active')
        self.Button4.configure(text='''Добавить в список''', command=functapp.add_99_ip_ping)
        self.Button4_2 = tk.Button(self.TNotebook1_t1)
        self.Button4_2.place(relx=0.304, rely=0.7, height=33, width=151)
        self.Button4_2.configure(activebackground="beige")
        self.Button4_2.configure(borderwidth="2")
        self.Button4_2.configure(compound='left')
        self.Button4_2.configure(text='''Добавить в список''', command=functapp.add_1_ip_ping)
        self.Listbox1_1 = ScrolledText(self.TNotebook1_t2)
        self.Listbox1_1.place(relx=0.018, rely=0.2, relheight=0.43
                , relwidth=0.204)
        self.Listbox1_1.configure(background="white")
        self.Listbox1_1.configure(font="TkFixedFont")
        self.Listbox1_1.configure(selectbackground="#c4c4c4")
        self.Label2_1 = tk.Label(self.TNotebook1_t2)
        self.Label2_1.place(relx=0.036, rely=0.05, height=21, width=105)
        self.Label2_1.configure(activebackground="#f9f9f9")
        self.Label2_1.configure(anchor='w')
        self.Label2_1.configure(compound='left')
        self.Label2_1.configure(text='''Список хостов''')
        self.Button2_1 = tk.Button(self.TNotebook1_t2)
        self.Button2_1.place(relx=0.036, rely=0.7, height=33, width=98)
        self.Button2_1.configure(activebackground="beige")
        self.Button2_1.configure(borderwidth="2")
        self.Button2_1.configure(compound='left')
        self.Button2_1.configure(text='''Очистить''', command=functapp.clean_scan_list)
        self.Label3_1 = tk.Label(self.TNotebook1_t2)
        self.Label3_1.place(relx=0.393, rely=0.05, height=21, width=36)
        self.Label3_1.configure(activebackground="#f9f9f9")
        self.Label3_1.configure(anchor='w')
        self.Label3_1.configure(compound='left')
        self.Label3_1.configure(text='''Хост''')
        self.Entry1_1 = tk.Entry(self.TNotebook1_t2)
        self.Entry1_1.place(relx=0.339, rely=0.2, height=23, relwidth=0.207)
        self.Entry1_1.configure(background="white")
        self.Entry1_1.configure(font="TkFixedFont")
        self.Entry1_1.configure(selectbackground="#c4c4c4")
        self.Label4_1 = tk.Label(self.TNotebook1_t2)
        self.Label4_1.place(relx=0.75, rely=0.05, height=21, width=105)
        self.Label4_1.configure(activebackground="#f9f9f9")
        self.Label4_1.configure(anchor='w')
        self.Label4_1.configure(compound='left')
        self.Label4_1.configure(text='''Группа хостов''')
        self.Button4_1 = tk.Button(self.TNotebook1_t2)
        self.Button4_1.place(relx=0.661, rely=0.7, height=33, width=151)
        self.Button4_1.configure(activebackground="beige")
        self.Button4_1.configure(borderwidth="2")
        self.Button4_1.configure(compound='left')
        self.Button4_1.configure(text='''Добавить в список''', command=functapp.add_99_ip_scan)
        self.Entry2_1 = tk.Entry(self.TNotebook1_t2)
        self.Entry2_1.place(relx=0.661, rely=0.2, height=23, relwidth=0.154)
        self.Entry2_1.configure(background="white")
        self.Entry2_1.configure(font="TkFixedFont")
        self.Entry2_1.configure(selectbackground="#c4c4c4")
        self.Entry3_1 = tk.Entry(self.TNotebook1_t2)
        self.Entry3_1.place(relx=0.661, rely=0.4, height=23, relwidth=0.154)
        self.Entry3_1.configure(background="white")
        self.Entry3_1.configure(font="TkFixedFont")
        self.Entry3_1.configure(selectbackground="#c4c4c4")
        self.Label5_1 = tk.Label(self.TNotebook1_t2)
        self.Label5_1.place(relx=0.839, rely=0.2, height=21, width=57)
        self.Label5_1.configure(activebackground="#f9f9f9")
        self.Label5_1.configure(anchor='w')
        self.Label5_1.configure(compound='left')
        self.Label5_1.configure(text='''первый''')
        self.Label6_1 = tk.Label(self.TNotebook1_t2)
        self.Label6_1.place(relx=0.839, rely=0.4, height=21, width=82)
        self.Label6_1.configure(activebackground="#f9f9f9")
        self.Label6_1.configure(anchor='w')
        self.Label6_1.configure(compound='left')
        self.Label6_1.configure(text='''Последний''')
        self.Button4_1_1 = tk.Button(self.TNotebook1_t2)
        self.Button4_1_1.place(relx=0.304, rely=0.7, height=33, width=151)
        self.Button4_1_1.configure(activebackground="beige")
        self.Button4_1_1.configure(borderwidth="2")
        self.Button4_1_1.configure(compound='left')
        self.Button4_1_1.configure(text='''Добавить в список''', command=functapp.add_1_ip_scan)
        self.Text1 = ScrolledText(self.top)
        self.Text1.place(relx=0.017, rely=0.611, relheight=0.249, relwidth=0.968)
        self.Text1.configure(background="white")
        self.Text1.configure(font="TkTextFont")
        self.Text1.configure(selectbackground="#c4c4c4")
        self.Text1.configure(wrap="word")
        self.Button1 = tk.Button(self.top)
        self.Button1.place(relx=0.427, rely=0.895, height=33, width=116)
        self.Button1.configure(activebackground="beige")
        self.Button1.configure(borderwidth="2")
        self.Button1.configure(compound='left')
        self.Button1.configure(text='''Старт ping/scan''',command=functapp.app_ping_scanp)
        self.Label1 = tk.Label(self.top)
        self.Label1.place(relx=0.462, rely=0.546, height=21, width=47)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(anchor='w')
        self.Label1.configure(compound='left')
        self.Label1.configure(text='''Отчет''')
        #список для хранения адресов для пинга
        self.ping_storage = []
        #список для хранения адресов для сканирования
        self.scan_storage = []

def start_up():
    adminc3_support.main()

if __name__ == '__main__':
    adminc3_support.main()




