#1672. Richest Customer Wealth
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        MAX = 0
        IND = 0
        for i in range(len(accounts)):
            IND = sum(accounts[i])
            if IND > MAX:
                MAX = IND
        return MAX
