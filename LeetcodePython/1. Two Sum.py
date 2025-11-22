class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        new_list = []

        for i in nums:
            f_num = target - i
            if f_num in nums:
                new_list.append(nums.index(i))
                first_index = nums.index(i)
                new_list.append(nums.index(f_num, first_index + 1))
                break
        return new_list
