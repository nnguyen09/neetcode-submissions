class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = {}
        l = []
        for i , n in enumerate(nums):
            m[n] = i

        for i, k in enumerate(nums):
            value = target - k
            if value in m and m[value] != i:
                return [i, m[value]]
        return []