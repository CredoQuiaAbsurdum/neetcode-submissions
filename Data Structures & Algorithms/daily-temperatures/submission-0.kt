class Solution {
    fun dailyTemperatures(temperatures: IntArray): IntArray {

        val result = IntArray(temperatures.size) { 0 }

        val stack = ArrayDeque<Int>()

        for(i in 0 until temperatures.size) {
            while(stack.isNotEmpty() && temperatures[stack.last()] < temperatures[i]) {
                val prev = stack.removeLast()
                result[prev] = i - prev
            }
            stack.addLast(i)
        }
        return result
    }
}
