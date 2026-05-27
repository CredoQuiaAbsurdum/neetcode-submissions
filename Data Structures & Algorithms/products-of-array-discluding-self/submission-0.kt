class Solution {
    fun productExceptSelf(nums: IntArray): IntArray {

        val result = IntArray(nums.size) { 1 }
        val n = nums.size

        var leftProduct = 1 
        for(i in 0 until n) {
            result[i] = leftProduct
            leftProduct *= nums[i]
        }

        var rightProduct = 1 
        for(i in n-1 downTo 0) {
            result[i] *= rightProduct
            rightProduct *= nums[i]
        }

        return result
    }
}
