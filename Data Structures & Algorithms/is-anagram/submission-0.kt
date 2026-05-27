class Solution {
    fun isAnagram(s: String, t: String): Boolean {

        if(s.length != t.length) {
            return false
        }

        val myMap = HashMap<Char, Int>()

        for(c in s) {
            myMap[c] = (myMap[c] ?: 0) + 1
        }

        for(c in t) {
            myMap[c] = (myMap[c] ?: 0) - 1
            if(myMap[c] == 0) {
                myMap.remove(c)
            }
        }

        return if (myMap.isEmpty()) {
            true
        } else {
            false
        }
    }
}
