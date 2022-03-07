#买卖股票的最佳时机 II
def maxProfit(prices):
        profit = 0
        for i in range(1,len(prices)):
            tmp = prices[i] -prices[i-1]
            if tmp>0:
                profit = profit + tmp
        return profit
