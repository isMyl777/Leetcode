# 单词倒排
n = input()
for i in n:
  if not i.isalpha():
        a = a.replace(i,' ')
b = a.split()
print(*b[::-1])
