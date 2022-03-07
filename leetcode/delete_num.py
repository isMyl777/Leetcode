#删除排序数组中的重复项
def removeDuplicates(nums):
        if not nums:
           return 0
        n = len(nums)
        fast = slow = 1
        while fast < n:
            if nums[fast] !=nums[fast-1]:
                nums[slow] = nums[fast]
                slow+=1
            fast+=1
        return slow
