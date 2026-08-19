class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq = {}
        for num in nums:
            if num not in freq:
                freq[num] = 0
            freq[num] += 1
        
        heap = []
        for num in freq:
            heapq.heappush(heap, (freq[num], num))
            while len(heap) > k:
                heapq.heappop(heap)
        
        result = []
        while len(heap) > 0:
            count, num = heapq.heappop(heap)
            result.append(num)
        
        return result


