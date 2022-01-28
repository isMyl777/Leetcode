#数字颠倒
a = input()
aa = [i for i in a][::-1]
print(''.join([str(i)for i in aa]))
