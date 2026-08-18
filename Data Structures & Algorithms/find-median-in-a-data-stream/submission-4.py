class MedianFinder:

    def __init__(self):
        self.small = [] # maxHeap
        self.large = [] # minHeap
        

    def addNum(self, num: int) -> None:
        if not self.small:
            heapq.heappush_max(self.small, num)
            return
        if num < self.small[0]:
            heapq.heappush_max(self.small, num)
        else:
            heapq.heappush(self.large, num)
        while len(self.small) - len(self.large) > 1:
            temp = heapq.heappop_max(self.small)
            heapq.heappush(self.large, temp)
        while len(self.large) - len(self.small) > 1:
            temp = heapq.heappop(self.large)
            heapq.heappush_max(self.small, temp)
    
    def findMedian(self) -> float:
        if len(self.small) == len(self.large):
            return float(self.small[0] + self.large[0]) / 2
        elif len(self.small) > len(self.large):
            return float(self.small[0])
        else:
            return float(self.large[0])
        
        