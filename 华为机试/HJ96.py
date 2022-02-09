# 表示数字
while True:
    try:
        n = input()
        res = ''
        pre = ''
        for i in n:
            if i.isdigit():
                if pre.isdigit()!= True:
                    res+='*'
            else:
                if pre.isdigit():
                    res+='*'
            res += i
            pre = i
        if i.isdigit():
            res+='*'
        print(res)
    except:
        break
