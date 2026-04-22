class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = {}
        l = []
        for i , n in enumerate(nums):
            value = target - n
            if value in m:
                return [m[value],i]
            m[n] = i

    