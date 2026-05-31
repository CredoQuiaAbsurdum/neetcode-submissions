class Solution {
    fun characterReplacement(s: String, k: Int): Int {

        var left = 0
        var result = 0
        var maxFreq = 0

        val map = IntArray(26)

        for (right in s.indices) {

            val idx = s[right] - 'A'
            map[idx]++
            maxFreq = maxOf(maxFreq, map[idx])

            while (right - left + 1 - maxFreq > k) {
                map[s[left] - 'A']--
                left++
            }

            result = maxOf(result, right - left + 1)
        }

        return result
    }
}