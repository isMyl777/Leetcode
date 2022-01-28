#句子逆序
a = input().split(' ')
n = len(a)-1
d = ''
while n>=0:
    d = d+a[i]+" "
    n = n-1
print(d)
