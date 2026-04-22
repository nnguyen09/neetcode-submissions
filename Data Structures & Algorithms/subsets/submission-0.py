class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [] # store all the subset 
        subset = [] # subset we building 
        
        def dfs(i):
            # BASE CASE 
            # if we've looked at all the elements 
            if i >= len(nums):
                res.append(subset.copy()) # save a copy of current subset
                return 

            # choice 1: take nums[i]
            subset.append(nums[i]) # add current number
            dfs(i+1)               # move to the next index

            # backtrack (undo)
            subset.pop()           # remove last added number

            # choice 2: skip nums[i]
            dfs(i+1)               # move to next index without adding it 
        
        dfs(0)
        return res
        