def lastIndex(n):
    list = []
    for i in range(n):
        list.append(i)

    index = 2
    while list:
        print(list)
        length = len(list)
        index = delete(list, index)
        if length != 1:
            index = index + 3 - length

    return index


def delete(list, i):
    if list and len(list) == 1:
        temp = list[0]
        del list[0]
        return temp
    while i < len(list):
        del list[i]
        i += 2


lastIndex(8)