class Solution {
    fun lengthOfLongestSubstring(s: String): Int {

        var current = mutableSetOf<Char>()

        var longest = 0

        var left = 0 

        for(right in s.indices) {

            while(s[right] in current) {
                current.remove(s[left])
                left ++
            }
            current.add(s[right])

            longest = maxOf(longest, right - left + 1)
        }

        return longest
    }
}
