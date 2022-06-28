# 列表去重，保留顺序
```
l = [10, 2, 3, 21, 10, 3]

from collections import OrderedDict

print(list(OrderedDict.fromkeys(l).keys()))
```
