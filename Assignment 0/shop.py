# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
#
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


class FruitShop:
    def __init__(self, name, fruit_prices):
        """
            name: Name of the fruit shop

            fruit_prices: Dictionary with keys as fruit
            strings and prices for values e.g.
            {"apples": 2.00, "oranges": 1.50, "pears": 1.75}
        """
        self.fruit_prices = fruit_prices
        self.name = name
        print("Welcome to %s fruit shop" % (name))

    def get_cost_per_pound(self, fruit):
        """
            fruit: Fruit string
        Returns cost of 'fruit', assuming 'fruit'
        is in our inventory or None otherwise
        """
        if fruit not in self.fruit_prices:
            return None
        return self.fruit_prices[fruit]

    def get_price_of_order(self, order_list):
        """
            order_list: List of (fruit, num_pounds) tuples

        Returns cost of order_list, only including the values of
        fruits that this fruit shop has.
        """
        total_cost = 0.0
        for fruit, num_pounds in order_list:
            cost_per_pound = self.get_cost_per_pound(fruit)
            if cost_per_pound is not None:
                total_cost += num_pounds * cost_per_pound
        return total_cost

    def get_name(self):
        return self.name

    def __str__(self):
        return "<FruitShop: %s>" % self.get_name()

    def __repr__(self):
        return str(self)
