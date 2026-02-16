class Solution(object):
    def removeDuplicates(self, nums):
        unique = set(nums)
        nums_sorted = sorted(unique)
        
        for i in range(len(nums_sorted)):
            nums[i] = nums_sorted[i]
        return len(nums_sorted)    
      

            



        