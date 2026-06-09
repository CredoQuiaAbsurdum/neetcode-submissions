class Solution {
    fun findMin(nums: IntArray): Int {

        if(nums.size == 1) {
            return nums[0]
        }
        if(nums.size == 2) {
            return minOf(nums[0], nums[1])
        }

        var left = 0
        var right = nums.size - 1
        var min = Int.MAX_VALUE

        while(left <= right) {
            val mid = left + (right - left) / 2 
            if(nums[mid] < min) {
                min = nums[mid]
            }
            if(nums[mid] >= nums[left] && nums[mid] > nums[right]) {
                left = mid + 1
            } else {
                right = mid - 1
            }
        }

        return min

    }
}
