class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        distances = {}
        for i in range(len(points)):
            xi = points[i][0]
            yi = points[i][1]
            key = xi ** 2 + yi ** 2
            if key not in distances:
                distances[key] = []
            distances[key].append([xi, yi])
        
        heap = []
        for key in distances:
            heapq.heappush(heap, key)
        
        result = []
        while len(result) < k:
            key = heapq.heappop(heap)
            for each in distances[key]:
                if len(result) < k:
                    result.append(each)
                else:
                    break
        
        return result
