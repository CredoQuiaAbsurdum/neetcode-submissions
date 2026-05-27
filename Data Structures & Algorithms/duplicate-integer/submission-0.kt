class Solution {
    fun hasDuplicate(nums: IntArray): Boolean {

        return if(nums.toSet().size < nums.size) {
            true
        } else {
            false
        }
    }
}
