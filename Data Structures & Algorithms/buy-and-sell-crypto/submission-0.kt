class Solution {
    fun maxProfit(prices: IntArray): Int {

        var buyDay = 0
        var sellDay = 1

        var minPrice = prices[0]
        var maxProfit = 0

        while(sellDay < prices.size) {
            if (prices[buyDay] < prices[sellDay]) {
                val profit = prices[sellDay] - prices[buyDay]
                maxProfit = maxOf(maxProfit, profit)
            } else {
                minPrice = prices[sellDay]
                buyDay = sellDay
            }
            sellDay = sellDay + 1
        }

        return maxProfit
    }
}
