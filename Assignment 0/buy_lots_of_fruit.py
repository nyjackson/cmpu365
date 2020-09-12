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

"""
To run this script, type

  python3 buy_lots_of_fruit.py

Once you have correctly implemented the buy_lots_of_fruit function,
the script should produce the output:

Cost of [('apples', 2.0), ('pears', 3.0), ('limes', 4.0)] is 12.25
"""

fruit_prices = {
    "apples": 2.00,
    "oranges": 1.50,
    "pears": 1.75,
    "limes": 0.75,
    "strawberries": 1.00,
}


def buy_lots_of_fruit(order_list):
    """
    order_list: List of (fruit, num_pounds) tuples

    Returns cost of order
    """
    total_cost = 0.0
    for tuples in order_list:
            total_cost+= fruit_prices[tuples[0]] * tuples[1]
            
    # ** YOUR CODE HERE ***

    return total_cost


if __name__ == "__main__":
    # This code runs when you invoke the script from the command line.
    order_list = [("apples", 2.0), ("pears", 3.0), ("limes", 4.0)]
    print("Cost of", order_list, "is", buy_lots_of_fruit(order_list))
