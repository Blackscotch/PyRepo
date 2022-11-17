from pathlib import Path
import csv

def ReadFile():
    path = Path("les7", "dict.csv")
    list = []
    with open(path,'r', encoding='utf-8') as file:
        file_reader = csv.reader(file, delimiter=";")
        for row in file_reader:
            list.append(row)
        return list

def get_rgb(rgb):
    return "#%02x%02x%02x" % rgb

def WriteFile(data):
    path = Path("les7", "dict.csv")
    with open(path, 'a', encoding='utf-8') as file:
        file.write('{};{};{}\n'.format(data[0], data[1], data[2]))

def CheckFile(data):
    new_dict = ReadFile()
    for item in new_dict:
        if str(item) == str(data):
            return True
    
def GetToHtml():
    path = Path("les7", "index.html")
    contacts = ReadFile()
    style = 'style="font-size: 22px"'
    html = '<html>\n <head></head>\n <body>\n'
    for item in contacts:
        html += '<p{}>{} {} - {}</p>\n'.format(style, item[0], item[1], item[2])
    html += '</body>\n</html>'
    with open(path, 'w', encoding='utf-8') as page:
        page.write(html)