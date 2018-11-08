def ReverseSentence(s):
    # write code here
    if not s:
        return s

    list = s.split(' ')

    return " ".join(reversed(list))


print(ReverseSentence("I am a student."))