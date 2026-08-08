class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        heapq.heapify_max(stones)

        while len(stones) > 1:
            x = heapq.heappop_max(stones)
            y = heapq.heappop_max(stones)
            diff = x - y
            if diff > 0:
                heapq.heappush_max(stones, diff)
        
        if not stones:
            return 0
        return stones[0]
        