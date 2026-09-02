class Solution {
    /**
     * @param {number[]} prices
     * @return {number}
     */
    maxProfit(prices) {
        let maxProfit = 0
        let left = 0
        for (let right = 0; right < prices.length; right++){
            let total = prices[right] - prices[left]
            if (prices[left] > prices[right]){
                left = right
            }
            maxProfit = Math.max(total, maxProfit)

        }
        return maxProfit
    }
}
