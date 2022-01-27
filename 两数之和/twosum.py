nums = [2,7,11,15]
target = 9
def twosum():
  d = {}
  for i in range(len(nums)):
      x = target - nums[i]
      if nums[i] in d:
          return [d[nums[i]],i]
      else:
        d[x] = i
