class Solution {
    fun permute(nums: IntArray): List<List<Int>> {

        if (nums.size == 1) {
            return listOf(listOf(nums[0]))
        }

        val subperms = permute(nums.sliceArray(1 until nums.size))
        val result = mutableListOf<List<Int>>()
        for(p in subperms) {
            for(i in 0..p.size) {
                val pCopy = p.toMutableList()
                pCopy.add(i, nums[0])
                result.add(pCopy)
            }
        }

        return result
    }
}
