class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_profit = 0

        for price in prices[1:]:    # 두번째 날부터
            profit = price - min_price  # 지금 판매 시의 이익
            max_profit = max(max_profit, profit)    # 지금까지의 최대이익보다 크면 갱신
            min_price = min(min_price, price)   # 현재 가격이 더 싸다면 최저가 갱신

        return max_profit