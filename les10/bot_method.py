import datetime
from pathlib import Path
import xml.etree.ElementTree as xml

def writeFile(mess, mess_id, id, name, l_name, date):
    root = xml.Element("userRequest")
    appt = xml.Element("Quest")
    root.append(appt)

    mes_id = xml.SubElement(appt, "mes_id")
    mes_id.text = mess_id

    message = xml.SubElement(appt, "message")
    message.text = mess

    uid = xml.SubElement(appt, "uid")
    uid.text = id

    fio = xml.SubElement(appt, "fio")
    fio.text = f"{name} {l_name}"

    date_data = xml.SubElement(appt, "date_data")
    date_data.text = f"{date.year}-{date.month}-{date.day}, {date.hour}:{date.minute}"

    request = xml.SubElement(appt, "request")

    tree = xml.ElementTree(root)
    path = Path("les10", "quest.xml")
    with open(path, 'w', encoding='utf-8') as file:
        tree.write(file)
