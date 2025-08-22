class Solution(object):
    def maxProfit(self, prices):
        most_profit=0
        min=prices[0]
       
        
        for i in range(1,len(prices)):
            if(prices[i]<min):
                min=prices[i]
            else:
                k=prices[i]-min
                if k>most_profit:
                    most_profit=k
        return most_profit







        