class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # text = "".join(str d for d in digits)
        num = int(text)
        num += 1
        new_list = list(map(int,str(num)))

        return new_list
