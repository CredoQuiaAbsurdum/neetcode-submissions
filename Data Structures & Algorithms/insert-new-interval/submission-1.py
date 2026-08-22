class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        if not intervals:
            return [newInterval]

        result = []
        curr = newInterval
        for i, interval in enumerate(intervals):
            if curr[1] < interval[0]:
                result.append(curr)
                return result + intervals[i:]
            if curr[0] > interval[1]:
                result.append(intervals[i])
            else:
                curr = [
                    min(curr[0], interval[0]),
                    max(curr[1], interval[1])
                ]
        result.append(curr)
        return result

