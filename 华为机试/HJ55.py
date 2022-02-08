#挑7
while True:
    try:
        n = int(input())
        res = 0
        for i in range(1,n+1):
            if i % 7 ==0:
                res +=1
            elif str(i).count('7')> 0:
                res+=1
        print(res)
    except:
        break
