# 六一儿童节

# 题目描述
# 六一儿童节，老师带了很多好吃的巧克力到幼儿园。每块巧克力j的重量为w[j]，对于每个小朋友i，当他分到的巧克力大小达到h[i]
# (即w[j]>=h[i])，他才会上去表演节目。老师的目标是将巧克力分发给孩子们，使得最多的小孩上台表演。可以保证每个w[i]> 0且不
# 能将多块巧克力分给一个孩子或将一块分给多个孩子。

# 输入描述:
# 第一行：n，表示h数组元素个数
# 第二行：n个h数组元素
# 第三行：m，表示w数组元素个数
# 第四行：m个w数组元素

# 输出描述:
# 上台表演学生人数

if __name__ == '__main__':
    while True:
        try:
            n = int(input())
            h = list(map(lambda x: int(x), input().split()))
            m = int(input())
            w = list(map(lambda x: int(x), input().split()))
            # 将h与w从小到大排序，比较头节点的大小
            h.sort()
            w.sort()
            count = 0
            while h and w:
                if w[0] >= h[0]:    # 此时将糖果分给第一个人，人数加一
                    count += 1
                    del w[0]
                    del h[0]
                else:
                    del w[0]
            ####
            print(count)
        except:
            break