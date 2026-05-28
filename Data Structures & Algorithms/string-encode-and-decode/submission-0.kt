class Solution {

    fun encode(strs: List<String>): String {

        if(strs.size == 0) {
            return ""
        }

        var map = mutableListOf<Int>()
        var strings = ""

        for(s in strs) {
            map.add(s.length)
            strings += s
        }
        val mapString = map.joinToString("#")
        println(mapString + "|" + strings)
        return mapString + "|" + strings

        
    }

    fun decode(str: String): List<String> {

        if(str == "") {
            return emptyList()
        }

        val parts = str.split('|', limit = 2)
        val map = parts[0].split("#")
        var strings = parts[1]
        val result = mutableListOf<String>()

        for(n in map) {
            var str = ""
            var len = n.toInt()
            while(len != 0) {
                str += strings[0]
                strings = strings.substring(1)
                len -= 1
            }
            result.add(str)
        }

        return result
    }
}
