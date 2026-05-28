class Solution {
    fun isValidSudoku(board: Array<CharArray>): Boolean {

        val rows = Array(9) { BooleanArray(9) }
        val cols = Array(9) { BooleanArray(9) }
        val boxes = Array(9) { BooleanArray(9) }

        for(i in 0..8) {
            for(j in 0..8) {

                if(board[i][j] == '.') {
                    continue
                }

                val numIndex = board[i][j].digitToInt() - 1
                val boxIndex = (i/3) * 3 + j/3

                if(rows[i][numIndex] || cols[j][numIndex] || boxes[boxIndex][numIndex]) {
                    return false
                }

                rows[i][numIndex] = true
                cols[j][numIndex] = true
                boxes[boxIndex][numIndex] = true
            }
        }

        return true
    }
}
