class MedianFinder:

    def __init__(self):
        self.array = []
        

    def addNum(self, num: int) -> None:
        self.array.append(num)

    def findMedian(self) -> float:
        self.array.sort()
        n = len(self.array)
        if n % 2 == 1:
            return float(self.array[(n - 1) // 2])
        else:
            a = self.array[n // 2]
            b = self.array[n // 2 - 1]
            return float(a + b) / 2
