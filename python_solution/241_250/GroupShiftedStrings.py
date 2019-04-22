# 249. Group Shifted Strings

# Given a string, we can "shift" each of its letter to its successive letter, for example: "abc" -> "bcd". We can keep
# "shifting" which forms the sequence:

# "abc" -> "bcd" -> ... -> "xyz"
# Given a list of strings which contains only lowercase alphabets, group all strings that belong to the same shifting sequence.

# For example, given: ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"],
# Return:
# [
#   ["abc","bcd","xyz"],
#   ["az","ba"],
#   ["acef"],
#   ["a","z"]
# ]

class Solution:
    # 建立hash表，将strings中的每个str平移为"a"开头的字符串，并作为key加入到hash表。
    def groupStrings(self, strings):
        """
        :type strings: list[str]
        :rtype: list[list[str]]
        """
        if not strings:
            return []

        dict = {}
        for elem in strings:
            shift = ord(elem[0]) - ord("a")
            key = ['a'] * len(elem)
            for i in range(len(elem)):
                newElem = ord(elem[i]) - shift
                key[i] = chr(newElem) if newElem >= 97 else chr(newElem + 26)
            if not dict.get("".join(key)):
                dict["".join(key)] = [elem]
            else:
                dict["".join(key)].append(elem)

        res = []
        for list in dict.values():
            list.sort()
            res.append(list)

        return res