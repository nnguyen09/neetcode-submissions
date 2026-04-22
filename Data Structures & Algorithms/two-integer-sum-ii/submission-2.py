class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers)-1
        left = numbers[i]
        right = numbers[j]

        while (i < j):
            if ((left + right) > target):
                j-=1
                right = numbers[j] 
            elif ((left + right) < target):
                i+=1
                left = numbers[i] 
            else:
                return [i+1, j+1]
        