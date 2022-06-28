# 列表去重，保留顺序
```
l = [10, 2, 3, 21, 10, 3]

from collections import OrderedDict

print(list(OrderedDict.fromkeys(l).keys()))
```
# 魔术冒泡，参考代码风格
```
def magic_bubble_sort(numbers):
    """有魔力的冒泡排序算法，默认所有的偶数都比奇数大

    :param numbers: 需要排序的列表，函数将会直接修改原始列表
    """
    stop_position = len(numbers) - 1
    while stop_position > 0:
        for i in range(stop_position):
            current, next_ = numbers[i], numbers[i + 1] 
            current_is_even, next_is_even = current % 2 == 0, next_ % 2 == 0
            should_swap = False

            # 交换位置的两个条件：
            # - 前面是偶数，后面是奇数
            # - 前面和后面同为奇数或者偶数，但是前面比后面大
            if current_is_even and not next_is_even:
                should_swap = True
            elif current_is_even == next_is_even and current > next_:
                should_swap = True

            if should_swap:
                numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
        stop_position -= 1
    return numbers
```
# 最长重复子串
```
s = 'nddemdereeeffetcssssfggddregg'

def maxRepeatStr(str1):
    if not str1:
        return str1
    # 去重后的每个元素的重复字符串可能的最大长度
    len_up_border = len(str1) - len(set(str1)) + 1
    # print(len_up_border)
    # print(set(str1))
    # 缓存遍历，最大长度和当前元素（分别初始化为1和最大ASCII码对应的字符）
    max_len = 1
    res = {}
    # 长度反向遍历的跳出标识
    flag = False
    for i in range(len_up_border, 0, -1):
        for s in set(str1):
            spt = s * i
            # print(spt)
            splited = str1.split(spt)
            print(splited)
            if len(splited) > 1:
                max_len = max(max_len, i)
                res[i] = s
                flag = True
        if flag:
            break
    print(res)
    output = [v * k for k, v in res.items()]
    print(output)
    print(output[0])

maxRepeatStr(s)
```
