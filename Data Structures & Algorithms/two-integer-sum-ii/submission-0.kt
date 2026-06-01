class Solution {
    fun twoSum(numbers: IntArray, target: Int): IntArray {

        val map = numbers.withIndex().associate { it.value to it.index }

        for(i in numbers.indices) {
            val diff = target - numbers[i]
            if(diff in map) {
                return intArrayOf(i+1, map[diff]!! + 1)
            }
        }
        return intArrayOf(0, 0)
    }
}
