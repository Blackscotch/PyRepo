import datetime
from pathlib import Path
import csv

def WriteFile(mess_id, mess, date, id, name, l_name, answer):
    path = Path("les10", "quest.csv")
    with open(path, 'a', encoding='utf-8') as file:
        file.write('{};{};{};{};{};{};{}\n'.format(mess_id, mess, date, id, name, l_name, answer))
