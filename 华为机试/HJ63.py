#DNA序列
while True:
    try:
        a = input()
        b = int(input())
        max_count = 0
        res = ''
        for i in range(len(a)-b+1):
            ll = a[i:i+b].count('C') + a[i:i+b].count('G')
            if ll > max_count:
                max_count = ll
                res = a[i:i+b]
        print(res)
    except:
        break
