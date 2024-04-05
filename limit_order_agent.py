class LimitOrderAgent:
    def __init__(self, execution_client):
        self.execution_client = execution_client
        self.orders = []

    def price_tick(self, product_id, price):
        if product_id == 'IBM' and price < 100:
            self.execute_order(True, 'IBM', 1000, price)

    def execute_order(self, buy_flag, product_id, amount, limit):
        if buy_flag:
            self.execution_client.buy(product_id, amount, limit)
        else:
            self.execution_client.sell(product_id, amount, limit)

    def add_order(self, buy_flag, product_id, amount, limit):
        self.orders.append((buy_flag, product_id, amount, limit))

    def execute_held_orders(self, market_price):
        for order in self.orders:
            buy_flag, product_id, amount, limit = order
            if (buy_flag and market_price <= limit) or (not buy_flag and market_price >= limit):
                self.execute_order(buy_flag, product_id, amount, limit)
                self.orders.remove(order)