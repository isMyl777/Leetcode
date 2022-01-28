#提取不重复的整数
a = input()
aa = [int(i) for i in a][::-1]
d = []
for i in aa:
    if i not in d:
        d.append(i)
res = ''.join([str(i) for i in d])
print(res)
