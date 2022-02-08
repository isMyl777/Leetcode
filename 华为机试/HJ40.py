# 统计字符
while True:
    try:
        n = input()
        l = [0,0,0]
        for i in n:
            l[0]+=int(i.isalpha())
            l[1]+=int(i==' ')
            l[2]+=int(i.isnumeric())
        print(l[0])
        print(l[1])
        print(l[2])
        print(len(n)-l[0]-l[1]-l[2])
    except:
        break
