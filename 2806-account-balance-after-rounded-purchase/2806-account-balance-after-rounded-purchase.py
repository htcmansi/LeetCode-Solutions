class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        rem=purchaseAmount%10
        if rem>=5:
            roundedAmount=purchaseAmount+(10-rem)
        else:
            roundedAmount=purchaseAmount-rem
        return 100-roundedAmount