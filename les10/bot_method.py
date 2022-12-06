import datetime
from pathlib import Path
import csv

def WriteFile(mess_id, mess, date, id, name, l_name):
    path = Path("les10", "quest.csv")
    with open(path, 'a', encoding='utf-8') as file:
        file.write('{};{};{};{};{};{}\n'.format(mess_id, mess, date, id, name, l_name))

def RewriteFile():
    path = Path("les10", "quest.csv")
    with open(path, 'w', encoding='utf-8') as file:
        file.write('')

def ReadFile():
    path = Path("les10", "quest.csv")
    list = []
    with open(path,'r', encoding='utf-8') as file:
        file_reader = csv.reader(file, delimiter=";")
        for row in file_reader:
            list.append(row)
        return list