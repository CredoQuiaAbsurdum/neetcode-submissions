class Solution {
    fun characterReplacement(s: String, k: Int): Int {

        var result = 0
        var left = 0
        var maxFreq = 0

        var map = mutableMapOf<Int, Int>()

        for(right in s.indices) {

            val index = s[right] - 'A'
            map[index] = (map[index] ?: 0) + 1
            maxFreq = maxOf(map[index]!!, maxFreq)

            var windowSize = right - left + 1
            
            while(windowSize - maxFreq > k) {
                val leftIndex = s[left] - 'A'
                map[leftIndex] = map[leftIndex]!! - 1
                left ++
                windowSize = right - left + 1
            }

            result = maxOf(right - left + 1, result)
        }
        return result
    }
}
