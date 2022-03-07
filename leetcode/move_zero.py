#移动零
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        left = right = 0
        while left < n:
            if nums[left] != 0:
                nums[left],nums[right] = nums[right],nums[left]
                right +=1
            left+=1
        return nums
