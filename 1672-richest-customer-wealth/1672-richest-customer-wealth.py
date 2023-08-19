class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        rich_customer=0
        for cust_account in accounts:
            total_wealth =sum(cust_account)
            rich_customer=max(rich_customer,total_wealth)
        return rich_customer