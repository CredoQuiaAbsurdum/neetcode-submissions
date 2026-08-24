class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        if not intervals:
            return 0

        intervals.sort(key=lambda x: x[1])
        
        curr = intervals[0]
        count = 0
        for i in range(1, len(intervals)):
            if intervals[i][0] >= curr[1]:
                curr = intervals[i]
            else:
                count += 1
        
        return count


        
        