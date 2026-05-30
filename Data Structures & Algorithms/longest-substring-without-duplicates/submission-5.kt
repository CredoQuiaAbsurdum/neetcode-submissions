class Solution {
    fun lengthOfLongestSubstring(s: String): Int {

        var longest = 0

        var left = 0 
        var right = 1

        while(right <= s.length) {
            var substring = s.substring(left, right)
            while(substring.toSet().size != substring.length) {
                left += 1
                substring = s.substring(left, right)
            }
            longest = maxOf(longest, substring.length)
            right += 1
        }

        return longest
    }
}
