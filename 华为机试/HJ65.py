#最长公共子串
while True:
    try:
        a = input()
        b = input()
        if len(a) > len(b):
            a,b = b,a
        res = ''
        for i in range(len(a)):
            for j in range(i+1,len(a)):
                if a[i:j+1] in b and j+1 -i >len(res):
                    res = a[i:j+1]
        print(res)
    except:
        break
