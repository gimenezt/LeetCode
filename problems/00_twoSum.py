class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        num_dict = {}
        
        for idx, num in enumerate(nums):
            complement = target - num
            
            if complement in num_dict:
                return [num_dict[complement], idx]
            
            else:
                num_dict[num] = idx
        
        return []