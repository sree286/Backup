# find a day to obtain maximum profit

def maxProfit(prices):

	max_profit, current_val = 0, 0

	for price in reversed(prices):
		current_val = max(price, current_val)
		profit = current_val - price
		max_profit = max(max_profit, profit)

	return max_profit



prices = list(map(int, input().split()))

print(maxProfit(prices))