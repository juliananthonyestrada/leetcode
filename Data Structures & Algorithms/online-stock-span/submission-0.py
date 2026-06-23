class StockSpanner:

    # span = max num of CONSECUTIVE days (starting from td) for which prc <= to the price of td

    def __init__(self):
        # store prcs in a stack where the bottom of the stack is the first day collected
        # the top of the stack, is yesterday
        self.prices = []

    def next(self, price: int) -> int:
        span = 0
        i = 1

        self.prices.append(price)

        # calculate span of today
        while i <= len(self.prices) and self.prices[-i] <= price:
            span += 1
            i += 1

        # add curr price
        return span


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)