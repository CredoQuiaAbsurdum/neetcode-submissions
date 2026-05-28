import java.util.PriorityQueue

class Solution {
    fun topKFrequent(nums: IntArray, k: Int): IntArray {

        val freq = HashMap<Int, Int>()

        for(n in nums) {
            freq[n] = (freq[n] ?: 0) + 1
        }

        val pq = PriorityQueue<Int> { a, b ->
            freq[a]!! - freq[b]!!
        }

        for(n in freq.keys) {
            pq.add(n)
            if(pq.size > k) {
                pq.poll()
            }
        }

        return pq.toIntArray()
    }
}
