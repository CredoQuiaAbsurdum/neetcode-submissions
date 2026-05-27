class Solution {
    fun twoSum(nums: IntArray, target: Int): IntArray {
        
        val map = nums.withIndex().associate { it.value to it.index }

        for(i in 0 until nums.size) {
            val j = map[target - nums[i]]
            if(j != null && j != i) {
                return intArrayOf(i, j)
            }
        }

        return intArrayOf()

    }
}
