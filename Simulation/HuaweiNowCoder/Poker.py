# 扑克牌游戏大家应该都比较熟悉了，一副牌由54张组成，含3~A，2各4张，小王1张，大王1张。牌面从小到大用如下字符和字符串表示
# （其中，小写joker表示小王，大写JOKER表示大王）:)
# 3 4 5 6 7 8 9 10 J Q K A 2 joker JOKER
# 输入两手牌，两手牌之间用“-”连接，每手牌的每张牌以空格分隔，“-”两边没有空格，如：4 4 4 4-joker JOKER
# 请比较两手牌大小，输出较大的牌，如果不存在比较关系则输出ERROR

# 基本规则：
# （1）输入每手牌可能是个子，对子，顺子（连续5张），三个，炸弹（四个）和对王中的一种，不存在其他情况，由输入保证两手牌都是合法的，顺子已经从小到大排列；
# （2）除了炸弹和对王可以和所有牌比较之外，其他类型的牌只能跟相同类型的存在比较关系（如，对子跟对子比较，三个跟三个比较），不考虑拆牌情况（如：将对子拆分成个子）
# （3）大小规则跟大家平时了解的常见规则相同，个子，对子，三个比较牌面大小；顺子比较最小牌大小；炸弹大于前面所有的牌，炸弹之间比较牌面大小；对王是最大的牌；
# （4）输入的两手牌不会出现相等的情况。

def level(poker):
    length = len(poker.split(" "))
    if length == 1:
        return 1
    elif length == 2:
        if poker.split(" ")[0] in ["joker", "JOKER"]:
            return 6
        else:
            return 2
    elif length == 3:
        return 3
    elif length == 4:
        return 5
    elif length == 5:
        return 4

def compare(left, right):
    dict = {"3": 1, "4": 2, "5": 3, "6": 4, "7": 5, "8": 6, "9": 7, "10": 8, "J": 9, "Q": 10, "K": 11, "A": 12, "2": 13,
            "joker": 14, "JOKER": 15}
    level1 = level(left)
    level2 = level(right)
    if level1 not in [5, 6] and level2 not in [5, 6]:
        if level1 != level2:
            return "ERROR"
        else:
            return left if dict[str(left.split(" ")[0])] > dict[str(right.split(" ")[0])] else right
    else:
        if level1 > level2:
            return left
        elif level1 < level2:
            return right
        else:
            return left if dict[str(left.split(" ")[0])] > dict[str(right.split(" ")[0])] else right

while True:
    try:
        left, right = input().split("-")
        print(compare(left, right))
    except:
        break