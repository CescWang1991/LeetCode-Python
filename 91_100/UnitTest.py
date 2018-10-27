class UnitTest:

    def test_solution(self):
        str = "We are happy"
        list = str.split(" ")
        return "%20".join(list)


print(UnitTest().test_solution())