'''
给你一个整数数组 nums ，数组中的元素 互不相同 。返回该数组所有可能的子集（幂集）。

解集 不能 包含重复的子集。你可以按 任意顺序 返回解集。
'''
nums = [1,2,3]
d = [[]]
for i in range(len(nums)):
  for j in range(len(d)):
    d.append(d[j] + [nums[i]])
print(d)
