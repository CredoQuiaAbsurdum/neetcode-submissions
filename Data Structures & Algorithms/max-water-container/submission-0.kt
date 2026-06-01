class Solution {
    fun maxArea(heights: IntArray): Int {

        var left = 0
        var right = heights.lastIndex
        var result = 0

        while(left < right) {
            val current = minOf(heights[left]!!, heights[right]!!) * (right - left)
            result = maxOf(result, current)
            if (heights[left] < heights[right]) {
                left++
            } else {
                right--
            }
        }

        return result

    }
}
