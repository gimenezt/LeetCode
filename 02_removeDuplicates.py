class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        lenght = len(nums)

        # Varre list do fim para início
        for i in range(lenght-1, 0, -1):
            if nums[i]==nums[i-1]:
                nums.pop(i)
                
        return len(nums)
