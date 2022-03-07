#加一
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        b = ''.join([str(i) for i in digits])
        c = int(b) + 1
        return [int(i) for i in str(c)]
