class Solution:
	def accountBalanceAfterPurchase(self, purchaseAmount):

		purchaseAmount = ((purchaseAmount - 5) // 10 ) * 10 + 10

		result = 100 - purchaseAmount

		return result

