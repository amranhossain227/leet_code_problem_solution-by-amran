class Solution(object):
    def maxProfit(self, prices):
        most_profit=0
        
        for i in range (len(prices)):
            for j in range(i+1,len(prices)):
                if prices[j]-prices[i]>most_profit:
                    most_profit=prices[j]-prices[i]
        return most_profit