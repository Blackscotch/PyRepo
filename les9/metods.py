def GetList(some_text):
    list = []
    tmp = ""
    for i in range(len(some_text)):
        if some_text[i].isdigit():
            tmp += some_text[i]
            if i == len(some_text) - 1:
                list.append(tmp)
        else:
            if i == 0:
                tmp = "-"
            else:
                list.append(tmp)
                tmp = ""
                if i != len(some_text) - 1:
                    list.append(some_text[i])
    return list

def GetResult(new_list):
    count = len(new_list)//2
    while count != 0:
        res = 0
        if str(new_list).find("*") != -1 or str(new_list).find("/") != -1:
            index = index2 = 0
            if str(new_list).find("*") != -1:
                index = new_list.index("*")
            if str(new_list).find("/") != -1:
                index2 = new_list.index("/")
            if index != 0 and index2 != 0:
                if index < index2:
                    res = float(new_list[index - 1]) * float(new_list[index + 1])
                else:
                    index = index2
                    res = float(new_list[index - 1]) / float(new_list[index + 1])
            elif index == 0:
                index = index2
                res = float(new_list[index - 1]) / float(new_list[index + 1])
            else:
                res = float(new_list[index - 1]) * float(new_list[index + 1])
            del new_list[index - 1:index + 2]
            new_list.insert(index-1, res)
            res = 0
            count = count - 1
        elif str(new_list).find("+") != -1 or str(new_list).find("-") != -1:
            index = index2 = 0
            if str(new_list).find("+") != -1:
                index = new_list.index("+")
            if str(new_list).find("-") != -1:
                index2 = new_list.index("-")
            if index != 0 and index2 != 0:
                if index < index2:
                    res = float(new_list[index - 1]) + float(new_list[index + 1])
                else:
                    index = index2
                    res = float(new_list[index - 1]) - float(new_list[index + 1])
            elif index == 0:
                index = index2
                res = float(new_list[index - 1]) - float(new_list[index + 1])
            else:
                res = float(new_list[index - 1]) + float(new_list[index + 1])
            del new_list[index - 1:index + 2]
            new_list.insert(index-1, res)
            res = 0
            count = count - 1
    return new_list