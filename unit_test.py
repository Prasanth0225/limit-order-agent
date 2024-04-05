import unittest
from unittest.mock import MagicMock
from limit_order_agent import LimitOrderAgent
class TestLimitOrderAgent(unittest.TestCase):
    def test_buy_order_execution(self):
        execution_client = MagicMock()
        agent = LimitOrderAgent(execution_client)
        agent.price_tick('IBM', 99)
        execution_client.buy.assert_called_once_with('IBM', 1000, 99)
    def test_sell_order_execution(self):
        execution_client = MagicMock()
        agent = LimitOrderAgent(execution_client)
        agent.price_tick('AAPL', 120)
        # Assuming AAPL price is not below $100
        execution_client.sell.assert_not_called()
    def test_add_order(self):
        execution_client = MagicMock()
        agent = LimitOrderAgent(execution_client)
        agent.add_order(True, 'GOOGL', 200, 200)
        self.assertEqual(len(agent.orders), 1)
        self.assertEqual(agent.orders[0], (True, 'GOOGL', 200, 200))
    def test_execute_held_orders(self):
        execution_client = MagicMock()
        agent = LimitOrderAgent(execution_client)
        agent.add_order(True, 'MSFT', 300, 250)
        agent.execute_held_orders(260)
        execution_client.buy.assert_called_once_with('MSFT', 300, 250)
if __name__ == '__main__':
    unittest.main()