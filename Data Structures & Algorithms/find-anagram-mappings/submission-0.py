class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:

        order = {}
        for i, num in enumerate(nums2):
            order[num] = i
        
        result = []
        for num in nums1:
            result.append(order[num])

        return result
        