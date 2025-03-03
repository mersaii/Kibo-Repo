import unittest
import io
import sys
from tsp import TSP

class TestTSP(unittest.TestCase):
    def setUp(self):
        adjacency_matrix = [
            [0, 10, 74, 60, 26],
            [10, 0, 76, 22, 81],
            [74, 76, 0, 69, 84],
            [60, 22, 69, 0, 30],
            [26, 81, 84, 30, 0]
        ]
        self.tsp = TSP(adjacency_matrix)

    def test_brute_force_order_4(self):
        adjacency_matrix = [
            [0, 10, 15, 20],
            [10, 0, 100, 25],
            [15, 100, 0, 30],
            [20, 25, 30, 0]
        ]
        self.tsp = TSP(adjacency_matrix)
        order, _ = self.tsp.brute_force()
        self.assertEqual(order, [0, 1, 3, 2, 0])

    def test_brute_force_cost_4(self):
        adjacency_matrix = [
            [0, 10, 15, 20],
            [10, 0, 100, 25],
            [15, 100, 0, 30],
            [20, 25, 30, 0]
        ]
        self.tsp = TSP(adjacency_matrix)
        _, cost = self.tsp.brute_force()
        self.assertEqual(cost, 80)

    def test_nn_order_4(self):
        adjacency_matrix = [
            [0, 10, 15, 20],
            [10, 0, 100, 25],
            [15, 100, 0, 30],
            [20, 25, 30, 0]
        ]
        self.tsp = TSP(adjacency_matrix)
        order, _ = self.tsp.nearest_neighbor()
        self.assertEqual(order, [0, 1, 3, 2, 0])

    def test_nn_cost_4(self):
        adjacency_matrix = [
            [0, 10, 15, 20],
            [10, 0, 100, 25],
            [15, 100, 0, 30],
            [20, 25, 30, 0]
        ]
        self.tsp = TSP(adjacency_matrix)
        _, cost = self.tsp.nearest_neighbor()
        self.assertEqual(cost, 80)

    def test_brute_force_order_5(self):
        order, _ = self.tsp.brute_force()
        self.assertEqual(order, [0, 1, 2, 3, 4, 0])

    def test_brute_force_cost_5(self):
        _, cost = self.tsp.brute_force()
        self.assertEqual(cost, 211)

    def test_nn_order_5(self):
        order, _ = self.tsp.nearest_neighbor()
        self.assertEqual(order, [0, 1, 3, 4, 2, 0])

    def test_nn_cost_5(self):
        _, cost = self.tsp.nearest_neighbor()
        self.assertEqual(cost, 220)
