# 开发一个简单错误记录功能小模块，能够记录出错的代码所在的文件名称和行号。
# 处理:
# 1.记录最多8条错误记录，对相同的错误记录(即文件名称和行号完全匹配)只记录一条，错误计数增加；(文件所在的目录不同，文件名和行号相同也要合并)
# 2.超过16个字符的文件名称，只记录文件的最后有效16个字符；(如果文件名不同，而只是文件名的后16个字符和行号相同，也不要合并)
# 3.输入的文件可能带路径，记录文件名称不能带路径

import collections

dict = collections.OrderedDict()
while True:
    try:
        s = input().split("\\")
        file, num = s[-1].split(" ")
        if not dict.get((file, num)):
            dict[(file, num)] = 1
        else:
            dict[(file, num)] += 1
    except:
        break

dict = dict.items()
sort_dict = sorted(dict, key=lambda x:x[1], reverse=True)
count = 0
for k, v in sort_dict:
    count += 1
    if count <= 8:
        name = k[0]
        if len(name) > 16:
            name = name[-16:]
        print(" ".join([name, str(k[1]), str(v)]))
    else:
        break