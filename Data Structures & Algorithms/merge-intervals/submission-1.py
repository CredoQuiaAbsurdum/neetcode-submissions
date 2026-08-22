class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        if len(intervals) < 2:
            return intervals
        
        intervals.sort()

        result = []
        curr = intervals[0]
        for i in range(1, len(intervals)):
            if curr[1] < intervals[i][0]:
                result.append(curr)
                curr = intervals[i]
            else:
                curr = [
                    min(curr[0], intervals[i][0]),
                    max(curr[1], intervals[i][1])
                ]
        result.append(curr)

        return result
        