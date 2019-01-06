# 299. Bulls and Cows

class Solution:
    # 遍历两个数组，如果对应位置的数字相同，则same加一，否则，用哈希表分别记录数字出现的此数
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        secret = list(secret)
        guess = list(guess)
        s = dict()
        g = dict()
        same = 0
        index = 0
        while index < len(guess):
            if secret[index] == guess[index]:
                same += 1
                del secret[index]
                del guess[index]
            else:
                s[secret[index]] = s.get(secret[index], 0) + 1
                g[guess[index]] = g.get(guess[index], 0) + 1
                index += 1
        count = 0
        for i in range(10):     # 遍历所有数字，取两个哈希表对应value的最小值
            count += min(s.get(str(i), 0), g.get(str(i), 0))

        return str(same) + "A" + str(count) + "B"