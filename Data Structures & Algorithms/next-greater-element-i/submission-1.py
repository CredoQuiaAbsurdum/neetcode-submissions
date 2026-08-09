class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        stack = []
        greater = {}

        for num in nums2:
            while len(stack) > 0 and stack[-1] < num:
                curr = stack.pop()
                greater[curr] = num
            stack.append(num)

        while stack:
            curr = stack.pop()
            greater[curr] = -1
        
        result = []
        for num in nums1:
            result.append(greater[num])
        
        return result
        