nums = ['word', 'dab', 'da', 'dc', 'dword', 'd']
start = 0
flag = nums[start][-1]
# print(flag)
tem_nums = []
for i in nums:
    if i[0] == flag:
        tem_nums.append(i)
# print(tem_nums)
list1 = [[len(x), x]for x in tem_nums]
# print(list1)
list1 = sorted(list1, key=lambda x : [-1 * x[0], x[1]])
# print(list1)
if nums[start][0] == flag:
    res = list1[0][1] + list1[1][1]
else:
    res = nums[start]+list1[0][1] + list1[1][1]
print(res)
