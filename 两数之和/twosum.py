nums = [2,7,11,15]
target = 9
def twosum(nums,target):
  d = {}
  for i in range(len(nums)):
      x = target - nums[i]
      if nums[i] in d:
          return [d[nums[i]],i]
      else:
        d[x] = i
        
twosum(nums,target)
////////////////////////////////
nums = [2, 7, 11, 15]
target = 9
d = {}
for i, num in enumerate(nums):
    if target - num in d:
        print([d[target-num], i])
    else:
        d[num] = i
