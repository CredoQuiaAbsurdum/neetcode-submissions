class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        stack = []
        nums1set = set(nums1)
        greater = {}
        result = []

        for num in nums2:
            while len(stack) > 0 and stack[-1] < num:
                curr = stack.pop()
                greater[curr] = num
            if num in nums1set:
                stack.append(num)

        while len(stack) > 0:
            curr = stack.pop()
            greater[curr] = -1
        
        for num in nums1:
            result.append(greater[num])
        
        return result
        