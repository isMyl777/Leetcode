# 字符串排序
# 输入Type 输出epTy
while True:
  try:
    a = input()
    b = ''
    for i in a:
      if i.isalpha():
        b+=i
    s = sorted(b,key = str.upper)
    l = ''
    index = 0
    for i in range(len(a)):
      if a[i].isalpha():
        l+=s[index]
        index+=1
      else:
        l+=a[i]
    print(l)
  except:
    break
