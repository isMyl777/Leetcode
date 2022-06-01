...
输⼊ 0 6 word dd da dc dword d 输出 worddwordda 
说明： 先确定起始单词word 再确定d开头长度最长的单词dword 剩余
以d开头且长度最长的由 da dd dc 则取字典序最⼩的da 所以最后输出worddwordda 
⽰例⼆： 输⼊： 4 6 word dd da dc dword d 输
出： dwordda
...


k = 4
n = 6
ints = ['word','dd','da','dc','dword','d']
def long_word(nums):
    tmp_words = [[len(w), w] for w in nums]
    tmp_words = sorted(tmp_words, key=lambda x: (-1 * x[0], x[1]))
    new_words = [w[1] for w in tmp_words]
    return new_words[0]

res = ints[k]
new_res = res
key = True
while key:
    ints.remove(new_res)
    start_word = res[-1]
    new_ll = [x for x in ints if x[0] == start_word]
    if len(new_ll) ==0 :
        break
    else:
        print(new_ll)
        new_res = long_word(new_ll)
        print(new_res)
        res += new_res
print(res)
