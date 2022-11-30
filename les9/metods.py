enter = input("Введите выражение: ")
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

new_list = GetList(enter)      
print(new_list)
print(len(new_list))
count = len(new_list)//2
print("число итераций " +str(count))
while count != 0:
    res = 0
    for i in range(len(new_list)):
        if new_list[i] == "*":
            res = int(new_list[i - 1]) * int(new_list[i + 1])
            del new_list[i - 1:i + 1]
            new_list.append(res)
            res = 0
            count = count - 1
        if new_list[i] == "+":
            res = int(new_list[i - 1]) + int(new_list[i + 1])
            del new_list[i - 1:i + 1]
            new_list.append(res)
            res = 0
            count = count - 1
print(new_list)