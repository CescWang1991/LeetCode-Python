# 293. Flip Game

# You are playing the following Flip Game with your friend: Given a string that contains only these two characters: +
# and -, you and your friend take turns to flip two consecutive "++" into "--". The game ends when a person can no longer
# make a move and therefore the other person will be the winner.
#
# Write a function to compute all possible states of the string after one valid move.
#
# For example, given s = "++++", after one move, it may become one of the following states:
# [
#   "--++",
#   "+--+",
#   "++--"
# ]
# If there is no valid move, return an empty list [].

class Solution:
    def generatePossibleNextMoves(self, s):
        """
        :type s: str
        :rtype: list[str]
        """
        ans = []
        if not s or len(s) < 1:
            return ans
        for i in range(1, len(s)):
            if s[i] == "+" and s[i-1] == "+":
                ans.append(s[:i-1]+"--"+s[i+1:])
        return ans

# 294. Flip Game II

# You are playing the following Flip Game with your friend: Given a string that contains only these two characters: +
# and -, you and your friend take turns to flip two consecutive "++" into "--". The game ends when a person can no longer
# make a move and therefore the other person will be the winner.

# Write a function to determine if the starting player can guarantee a win.

# Example:
# Input: s = "++++"
# Output: true
# Explanation: The starting player can guarantee a win by flipping the middle "++" to become "+--+".
# Follow up:
# Derive your algorithm's runtime complexity.

class Solution2:
    # 采用回溯算法，我们从1开始遍历字符串，将连续的两个"+"flip，然后将递归调用flip，如果返回false，我们则返回true
    def canWin(self, s):
        """
        :type s: str
        :rtype: bool
        """
        for i in range(1, len(s)):
            if s[i-1] == "+" and s[i] == "+":
                flip = s[:i-1] + "--" + s[i+1:]
                if not self.canWin(flip):
                    return True
        return False