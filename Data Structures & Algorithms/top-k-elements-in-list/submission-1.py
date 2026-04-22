class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for n in nums:
            count[n] = count.get(n,0) + 1 
        sort_dict = dict(sorted(count.items(), key=lambda item:item[1]))
        print(sort_dict)
        res = list(sort_dict.keys())[-k:]
        return res
    
