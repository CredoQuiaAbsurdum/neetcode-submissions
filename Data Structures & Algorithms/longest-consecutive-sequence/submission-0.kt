class Solution {
    fun longestConsecutive(nums: IntArray): Int {

        val hashset = nums.toHashSet()

        var result = 0

        for(n in hashset) {
            if(n - 1 in hashset) {
                continue
            }

            var end = n
            while(end + 1 in hashset) {
                end += 1
            }
            val length = end - n + 1

            result = maxOf(result, length)
        }

        return result 
    }
}
