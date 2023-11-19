#Модуль с фунциями для обработки действия пользователя

import subprocess
import tkinter.messagebox as msgbox
import tkinter.filedialog as fdialog
import tkinter as tk
import adminc3
import adminc3_support
import re

def exit_app():
  '''Выход Exit'''
  exit(0)
#===

def show_about():
  '''показ блока About'''
  msgbox.showinfo("О программе","AdminCentr 1.0  - массовая проверка доступности IP-адресов и открытых портов на них")
#===


def app_ping():
  '''пинг хостов из списка'''
  if len(adminc3_support._w1.ping_storage) > 0:
    for i in range(len(adminc3_support._w1.ping_storage)):
      ping_string = 'ping -c 3 '+ adminc3_support._w1.ping_storage[i]
      p = subprocess.Popen(ping_string, shell=True, stdout=subprocess.PIPE)
      out = p.stdout.readlines()
      for line in out:
        adminc3_support._w1.Text1.insert(tk.END,'\n'+line.strip().decode())
#===


def app_scanp():
  '''скан хостов из списка'''
  if len(adminc3_support._w1.scan_storage) > 0:
    for i in range(len(adminc3_support._w1.scan_storage)):
      scan_string = 'sudo nmap '+ adminc3_support._w1.scan_storage[i]
      p = subprocess.Popen(scan_string, shell=True, stdout=subprocess.PIPE)
      out = p.stdout.readlines()
      for line in out:
        adminc3_support._w1.Text1.insert(tk.END,'\n'+line.strip().decode())

#===


def app_ping_scanp():
  '''Выбор ping или scan в зависимости от выбраной сейчас вкладки'''
  if adminc3_support._w1.TNotebook1.tabs().index(adminc3_support._w1.TNotebook1.select()) == 0:
    app_ping()
  else:
    app_scanp()
#===

def save_report():
  '''Сохранение отчета в файл'''
  file_name = fdialog.asksaveasfilename(filetypes=(("TXT files","*.txt"),("All files", "*.*") ))
  f = open(file_name, 'w') #Открываем файл для записи
  s = adminc3_support._w1.Text1.get(1.0, tk.END) #Считываем информацию из текстового поля
  f.write(s) #Записываем считанную информацию в файл
  f.close() #Закрываем файл

#===

def add_1_ip_ping():
  '''Добавление одного ip адреса в список для пинга и показной'''
  #поверяем ip, если корректный, то добавляем, иначе - сообщение и ничего не делаем
  if check_ip_host(adminc3_support._w1.Entry1.get()):
    adminc3_support._w1.Listbox1.insert(tk.END, adminc3_support._w1.Entry1.get()+'\n')
    #добавление адреса в массив-список
    adminc3_support._w1.ping_storage.append(adminc3_support._w1.Entry1.get())
    #
    #очистка поля ввода
    adminc3_support._w1.Entry1.delete(0, tk.END)
  else:
    msgbox.showwarning("Ошибка !","Недопустимый IP адрес хоста.")
#===

def add_99_ip_ping():
  '''Добавление группы ip адресов в список для пинга'''
  net_begin=adminc3_support._w1.Entry2.get()#начальный адрес группы
  net_end=adminc3_support._w1.Entry3.get()#конечный адрес
  nbegin = net_begin.split('.')
  nend = net_end.split('.')

  #если 3 октета начального и конечного адресов совпадают(одна сеть)
  #то создаем список, иначе - сообщение об ошибке
  #if nbegin[0]==nend[0] and nbegin[1]==nend[1] and nbegin[2]==nend[2]and len(nbegin)==4 and len(nend)==4:
  if nbegin[0]==nend[0] and nbegin[1]==nend[1] and nbegin[2]==nend[2]:
    #
    for i in range(int(nbegin[3]), int(nend[3])+1):
      #список для пинга
      adminc3_support._w1.ping_storage.append(nbegin[0]+'.'+nbegin[1]+'.'+nbegin[2]+'.'+str(i))
      #список для вида (для показа пользователю)
      adminc3_support._w1.Listbox1.insert(tk.END, nbegin[0]+'.'+nbegin[1]+'.'+nbegin[2]+'.'+str(i)+'\n')
    #
  else:
    msgbox.showwarning("Ошибка !","Начальный и конечный адреса списка должны быть из одной сети! Адреса должны быть заданы как x.x.x.x")
#===

def add_1_ip_scan():
  '''Добавление одного ip адреса в список для сканирования'''
  #поверяем ip, если корректный, то добавляем, иначе - сообщение и ничего не делаем
  if check_ip_host(adminc3_support._w1.Entry1_1.get()):
    #adminc3_support._w1.Entry1_1
    adminc3_support._w1.Listbox1_1.insert(tk.END, adminc3_support._w1.Entry1_1.get()+'\n')
    #добавление адреса в массив-список
    adminc3_support._w1.scan_storage.append(adminc3_support._w1.Entry1_1.get())
    #очистка поля ввода
    adminc3_support._w1.Entry1_1.delete(0, tk.END)
  else:
    msgbox.showwarning("Ошибка !","Недопустимый IP адрес хоста.")
#===

def add_99_ip_scan():
  '''Добавление группы ip адреов в список для сканирования'''
  net_begin=adminc3_support._w1.Entry2_1.get()#начальный адрес группы
  net_end=adminc3_support._w1.Entry3_1.get()#конечный адрес
  nbegin = net_begin.split('.')
  nend = net_end.split('.')

  #если 3 октета начального и конечного адресов совпадают(одна сеть)
  #то создаем список, иначе - сообщение об ошибке
  #if nbegin[0]==nend[0] and nbegin[1]==nend[1] and nbegin[2]==nend[2]and len(nbegin)==4 and len(nend)==4:
  if nbegin[0]==nend[0] and nbegin[1]==nend[1] and nbegin[2]==nend[2]:
    #
    for i in range(int(nbegin[3]), int(nend[3])+1):
      #список для пинга
      adminc3_support._w1.scan_storage.append(nbegin[0]+'.'+nbegin[1]+'.'+nbegin[2]+'.'+str(i))
      #список для вида (для показа пользователю)
      adminc3_support._w1.Listbox1_1.insert(tk.END, nbegin[0]+'.'+nbegin[1]+'.'+nbegin[2]+'.'+str(i)+'\n')
    #
  else:
    msgbox.showwarning("Ошибка !","Начальный и конечный адреса списка должны быть из одной сети! Адреса должны быть заданы как x.x.x.x")
#===


def clean_ping_list():
  '''Очистка списка хостов для пинга tk.Text()'''
  adminc3_support._w1.Listbox1.delete('1.0', tk.END)
  #очистка массива-списока адресов
  adminc3_support._w1.ping_storage = []
#===

def clean_scan_list():
  '''Очистка списка хостов для сканирования'''
  adminc3_support._w1.Listbox1_1.delete('1.0', tk.END)
  adminc3_support._w1.scan_storage = []
#===

def check_ip_host(ip):
  '''применение регулярного выражения для проверки октетов ip адреса хоста'''
  ip_pattern = r'^[1-9]{1,1}[0-9]{0,1}[0-9]{0,1}[.]{1,1}[0-9]{0,1}[0-9]{0,1}[0-9]{0,1}[.]{1,1}[0-9]{0,1}[0-9]{0,1}[0-9]{0,1}[.]{1,1}[0-9]{0,1}[0-9]{0,1}[0-9]{0,1}$'
  p=re.compile(ip_pattern)

  m = p.search(ip)

  if m:
    return True
  else:
    return False
#===

