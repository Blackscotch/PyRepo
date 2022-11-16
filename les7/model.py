# Задача 1. Создайте телефонный справочник с возможностью импорта и экспорта данных в нескольких форматах.
# Предусмотрите следующие функции для справочника:
# - новая запись;
# - вывод всего справочника;
# - поиск по имени;
# - экспорт справочника в форматы html, xml;
# - чтение данных из файла !;
# Требуется реализовать минимум 3 инструмента для работы со справочником.
from pathlib import Path
import csv

def WriteFile():
    path = Path("les7", "dict.csv")
    list = []
    with open(path,'r', encoding='utf-8') as file:
        file_reader = csv.reader(file, delimiter=";")
        for row in file_reader:
            list.append(row)
        return list


# frame2 = Frame(window)
    # frame2.pack()

    # label1 = tk.Label(master=frame1, 
    #     width=400, height=2,
    #     bg='#CD5C5C', 
    #     fg='#FFFFFF', 
    #     font=("Arial", 14),
    #     bd=4, 
    #     text=f"Записей в справочнике: {count}"
    # ).pack()



    # list_var = Variable(value=new_dict)
    # list_box = Listbox(listvariable=list_var, 
    #                 bg='#696969',
    #                 bd=0,
    #                 font=("Arial", 14),
    #                 fg='#FFFFFF',
    #                 highlightcolor='#FA8072',
    #                 height=5,
    #                 width=100,
    #                 selectbackground='#CD5C5C',
    #                 # yscrollcommand='yes'
    #             )
    # list_box.pack(ipadx=10, ipady=5, pady=5)