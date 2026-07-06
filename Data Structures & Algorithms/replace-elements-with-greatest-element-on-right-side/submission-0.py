class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:

        if not arr:
            return []
        
        maxValue = arr[-1]
        arr[-1] = -1
        position = 2

        while position <= len(arr):
            temp = arr[-position]
            arr[-position] = maxValue
            maxValue = max(maxValue, temp)
            position += 1
        
        return arr
                
            
            
            



        