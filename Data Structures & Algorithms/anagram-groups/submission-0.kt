class Solution {
    fun groupAnagrams(strs: Array<String>): List<List<String>> {

        val map = HashMap<String, MutableList<String>>()

        for (s in strs) {

            val count = IntArray(26)

            for (c in s) {
                count[c - 'a']++
            }

            val key = count.joinToString("#")

            map.getOrPut(key) { mutableListOf() }.add(s)
        }

        return map.values.toList()
    }
}
