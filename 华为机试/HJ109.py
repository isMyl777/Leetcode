# 压缩字符串
a = 'cccddecc'
res = ''
pre = a[0]
count = 1
for i in range(1,len(a)):
    if a[i] == pre:
        count +=1
    if a[i] != pre:
        res = res + str(count) + pre
        count = 1
        pre = a[i]
res = res + str(count) + pre
if len(res) >len(a):
    print(a)
else:
    print(res)
