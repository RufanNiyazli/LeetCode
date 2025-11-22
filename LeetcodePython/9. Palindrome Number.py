class Solution:
    def isPalindrome(self, x: int) -> bool:
        list_num = list(str(x))
        sec_num = []

        if x < 0:
            return False
        for i in range(len(list_num) - 1, -1, -1):
            sec_num.append(list_num[i])

        if list_num == sec_num:
            return True
        return False

       
