class Solution:
    def hammingWeight(self, n: int) -> int:
        
        curr = n
        count = 0
        while curr > 0:
            remain = curr % 2
            if curr % 2 == 1:
                count += 1
            curr = curr // 2

        return count