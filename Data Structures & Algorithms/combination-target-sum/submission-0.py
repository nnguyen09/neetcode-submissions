class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        path = []

        def dfs(i, total):
            # BASE CASE
            if total == target:
                res.append(path.copy()) # found valid combo 
                return
            
            if i >= len(nums) or total > target: # invalid
                return 

            # 2 choice 
            # choice 1: take num[i]
            path.append(nums[i])
            dfs(i, total + nums[i])

            # choice 2: skip num[i]
            path.pop()
            dfs(i+1, total)
        dfs(0,0)
        return res


