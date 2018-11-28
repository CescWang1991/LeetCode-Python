# 漂流船问题
# 公司组织团建活动，到某漂流圣地漂流，现有如下情况：
# 员工各自体重不一，第i个人的体重为 people[i]，每艘漂流船可以承载的最大重量为 limit。
# 每艘船最多可同时载两人，但条件是这些人的重量之和最多为 limit。
# 为节省开支，麻烦帮忙计算出载到每一个人所需的最小船只数(保证每个人都能被船载)。
#
# 输入描述：
# 第一行输入参与漂流的人员对应的体重数组
# 第二行输入漂流船承载的最大重量
#
# 输出描述：
# 所需最小船只数

def minNum(people, limit):
    people.sort()
    ships = 0
    while people:
        weight = limit - people[0]
        if len(people) > 1:
            for i in reversed(range(1, len(people))):
                if people[i] <= weight:
                    del people[i]
                    break
        ships += 1
        del people[0]

    return ships

while True:
    try:
        line = input()
        people = list(map(lambda x:int(x), line.split(" ")))
        limit = int(input())
        print(minNum(people, limit))
    except:
        break