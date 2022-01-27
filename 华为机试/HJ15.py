#求int型正整数在内存中存储时1的个数
a = input()
print(bin(a).count('1'))
bin() 返回一个整数 int 或者长整数 long int 的二进制表示。
