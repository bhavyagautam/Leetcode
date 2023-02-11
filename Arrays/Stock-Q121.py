class Solution(object):
    def maxProfit(self, prices):
        profit=0
        minimum=prices[0]
        sellprice=prices[0]
        for i in range(1,len(prices)):
            
            sellprice=prices[i]
            temp=sellprice-minimum
            if temp>profit:
                profit=temp
            if sellprice<minimum:
                minimum=sellprice
        return profit
            
sol=Solution()
prices = [7,1,5,3,6,4]
print(sol.maxProfit(prices))