# User-interfase
from tkinter import *
from tkinter import ttk
import tkinter as tk
from model import *

new_dict = None
error_name = 0
error_tel = 0
error_contact = 0
messege_info = None

def NewCount():
    new_dict = ReadFile()
    count = len(new_dict)
    dict_lable['text'] = f'Контактов в справочнике: {count}'
    contact_listbox.destroy()
    scrollbar.destroy()
    GetContactsList(new_dict)

def GetContactsList(data):
    new_data = []
    for item in data:
        item = list(filter(lambda x: x != "", item))
        new_data.append(item) 
    global contact_listbox
    global scrollbar
    count = len(new_data)
    contact_var = Variable(value=new_data)
    contact_listbox = Listbox(frame4, listvariable=contact_var, background='#0a0a0a',
        fg=get_rgb((220, 20, 60)), font='Arial 13 normal', highlightcolor=get_rgb((245, 243, 242)),
        selectbackground='#0a0a0a', highlightthickness=0, height=20, relief=FLAT
    )
    contact_listbox.pack(padx=20, pady=5, side=LEFT, fill=BOTH, expand=1)
    scrollbar = ttk.Scrollbar(frame4, orient="vertical", command=contact_listbox.yview)
    if count > 20:
        scrollbar.pack(side=RIGHT, fill=Y)
    else:
        scrollbar.pack_forget()
    contact_listbox["yscrollcommand"]=scrollbar.set

def SetWindowAdd():
    global entry_contact
    global entry2_contact
    global frame_contact
    global btn_contact
    global window1
    window1 = tk.Tk()
    window1.title("Новый контакт")
    window1.geometry("300x400")
    window1['bg'] = '#0a0a0a'

    frame_contact = Frame(window1, padx=20, pady=30, background='#0a0a0a')
    frame_contact.pack(fill=X, pady=(0, 10))

    label_1_contact = tk.Label(master=frame_contact, background='#0a0a0a', fg=get_rgb((245, 243, 242)), 
    width=300, font='Arial 13 normal', text="Введите имя и фамилию")
    label_1_contact.pack(padx=20, pady=(0,10))

    entry_contact = tk.Entry(master=frame_contact, name="ghd", width=300, font='Arial 13 normal', justify='center')
    entry_contact.bind('<Button>', lambda e, f = "1": SetActive(e, f))
    entry_contact.pack(padx=20, pady=(0, 20))

    label_2_contact = tk.Label(master=frame_contact, background='#0a0a0a', fg=get_rgb((245, 243, 242)), 
    width=300, font='Arial 13 normal', text="Введите номер телефона")
    label_2_contact.pack(padx=20, pady=(0,10))

    entry2_contact = tk.Entry(master=frame_contact, width=300, font='Arial 13 normal', justify='center')
    entry2_contact.bind('<Button>', lambda e, f = "2": SetActive(e, f))
    entry2_contact.pack(padx=20, pady=(0, 20))

    btn_contact = tk.Button(master=frame_contact, text="Добавить контакт", cursor='hand2',
        border=0, bg=get_rgb((255, 158, 181)), font='Arial 13 normal', fg=get_rgb((30, 30, 30)),
        padx=30, pady=5, command=GetNewContact
    )
    btn_contact.pack(pady=(10, 0))

    window1.mainloop()

def create():
    global window
    global new_dict
    global frame4
    global dict_lable
    
    window = tk.Tk() 
    window.title("Справочник")
    window.geometry("400x700")
    window['bg'] = '#0a0a0a'
    
    frame1 = Frame(window, background=get_rgb((22, 26, 30)), padx=20, pady=10)
    frame1.pack(fill=X, pady=(0, 10))
    search_logo = PhotoImage(file="les7/logo1.png")

    label = ttk.Label(master=frame1, image=search_logo, background=get_rgb((22, 26, 30)), width=30)
    label.pack(side=LEFT)

    label_1 = tk.Label(master=frame1, background=get_rgb((22, 26, 30)), fg=get_rgb((245, 243, 242)), 
    width=540, font=(13), text="Поиск по справочнику")
    label_1.pack(padx=20, pady=(0,10))

    entry = tk.Entry(master=frame1, width=540, font=(14), name='search', justify='center')
    entry.pack(side=LEFT, padx=20)

    frame2 = Frame(window, background='#0a0a0a', padx=20, pady=10)
    frame2.pack(fill=X, pady=(10, 0))
    btn = tk.Button(master=frame2, text="Добавить новый контакт", cursor='hand2',
        border=0, bg=get_rgb((255, 158, 181)), font=(13), fg=get_rgb((30, 30, 30)),
        padx=20, pady=5, command=SetWindowAdd
    )
    btn.pack()

    new_dict = ReadFile()
    frame3 = Frame(window, background='#0a0a0a', padx=0, pady=0)
    frame3.pack(fill=X, pady=(20, 10))
    count = len(new_dict)
    
    dict_lable = tk.Label(master=frame3, background=get_rgb((220, 20, 60)), fg=get_rgb((245, 243, 242)), 
        font=(13), text=f"Контактов в справочнике:  {count}")
    dict_lable.pack(ipady=3, fill=X)

    frame4 = Frame(window, background='#0a0a0a', padx=0, pady=0)
    frame4.pack(fill=X, pady=(0, 10))
    
    GetContactsList(new_dict)

    frame5 = Frame(window, background='#0a0a0a', padx=0, pady=0)
    frame5.pack(fill=X, side=BOTTOM)
    btn_push = tk.Button(master=frame5, text="Выгрузить справочник в Html", cursor='hand2',
        border=0, background=get_rgb((220, 20, 60)), font='Arial 13 normal', fg=get_rgb((245, 243, 242)),
        padx=5, pady=0, command=GetToHtml
    )
    btn_push.pack(fill=X, side=BOTTOM, ipady=10)

    window.mainloop()

def SetActive(event, num):
    global error_name
    global error_tel
    global error_contact
    if num == "2" and error_tel > 0:
        error_tel = 0
        label_error_tel.pack_forget()
    if num == "1" and error_name > 0:
        error_name = 0
        label_error_fio.pack_forget()
    if error_contact > 0:
        error_contact = 0
        label_error_contakt.pack_forget()
    if error_name == 0 and error_tel == 0 and error_contact == 0:
        btn_contact['state'] = ['normal']

def GetNewContact():
    global label_error_tel
    global label_error_fio
    global label_error_contakt
    global error_name
    global error_tel
    global error_contact
    global messege_info
    error_name = 0
    error_tel = 0
    error_contact = 0
    info = None
    contact_person = []
    contact_name = entry_contact.get()
    contact_tel = entry2_contact.get()
    if contact_name != "":
        if contact_name.find(" ") != -1:
            contact_person = contact_name.split()
        else:
            contact_person.append(contact_name)
            contact_person.append("")      
    else:
        error_name += 1
        
    if contact_tel != "":
        if contact_tel.isdigit() and len(contact_tel) < 12:
            contact_person.append(contact_tel)
        else:
            error_tel += 1
            info = 'Разрешены только цифры \n(не более 11)'
    else:
        error_tel += 1
        info = 'Поле Номер телефона не может быть\nпустым'
    

    if error_name != 0 or error_tel != 0:
        btn_contact['state'] = ['disabled']
        if error_name != 0:
            label_error_fio = tk.Label(master=frame_contact, width=300, font='Arial 9 normal',
                    bg='#0a0a0a', fg=get_rgb((246, 74, 70)),
                    text='Поле Имя и Фамилия не может быть\nпустым'
                )
            label_error_fio.pack(padx=20, pady=(15,0))
        if error_tel != 0:
            label_error_tel = tk.Label(master=frame_contact, width=300, font='Arial 9 normal',
                    bg='#0a0a0a', fg=get_rgb((246, 74, 70)),
                    text=str(info)
                )
            label_error_tel.pack(padx=20, pady=(15,0))
    else:
        if CheckFile(contact_person) == True:
            error_contact += 1
            btn_contact['state'] = ['disabled']
            label_error_contakt = tk.Label(master=frame_contact, width=300, font='Arial 9 normal',
                    bg='#0a0a0a', fg=get_rgb((246, 74, 70)),
                    text='Такой контакт уже существует.'
                )
            label_error_contakt.pack(padx=20, pady=(15,0))
        else:
            WriteFile(contact_person)
            window1.destroy()
            messege_info = "Контакт успешно сохранен."
            InfoMess(messege_info)

def InfoMess(name):
    global new_window
    global new_dict
    new_window = Toplevel()
    new_window.title("Информационное сообщение")
    new_window.geometry("400x100")
    new_window['bg'] = '#0a0a0a'
    new_window.protocol("WM_DELETE_WINDOW", lambda: Dismiss(new_window))
    info_lable = tk.Label(new_window, background='#0a0a0a', fg=get_rgb((245, 243, 242)), font='Arial 13 normal', text=name)
    info_lable.pack(padx=20, pady=[15, 10])
    close_btn = tk.Button(new_window, text="Понятно", cursor='hand2', border=0, bg=get_rgb((255, 158, 181)),
        font='Arial 13 normal', fg=get_rgb((30, 30, 30)), padx=30, pady=5, command=lambda: Dismiss(new_window)
    )
    close_btn.pack(pady=(0, 10))
    new_window.grab_set()
    new_window.mainloop()

def Dismiss(window):
    window = new_window
    window.grab_release()
    window.destroy()
    NewCount()





