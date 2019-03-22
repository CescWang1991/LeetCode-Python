while True:
    try:
        line = input().split("[")[1]
        line = line.split("]")[0]
        nums = list(map(int, line.split(",")))
        ret = 0
        last = 0
        curr = 0
        for i in range(len(nums)):
            if i > last:
                last = curr
                ret += 1
            curr = max(curr, i + nums[i])
        print(ret)
    except:
        break