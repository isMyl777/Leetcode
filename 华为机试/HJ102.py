# 字符统计
while True:
  try:
    s = input()
    ss = sorted(set(s))
    sss = sorted(ss,key = lambda x:s.count(x),reverse=True)
    print(''.join(sss))
  except:
    break
