# Assignment 5

In this assignment, you will complete a series of exercises to solve the traveling salesman problem (TSP).

## Your Task

You are given an implementation of a `TSP` class in `tsp.py` that uses an adjacency matrix representation of a graph to solve the TSP. It contains some starter code for constructing a graph, as well as starter code for two different algorithms to solve the TSP.

Recall that the traveling salesman problem asks the following: given a list of cities and the distances between each pair of cities, what is the shortest possible route that visits each city exactly once and returns to the origin city?

For example, say we have the following graph with five vertices:

<center>
<img
  src="/images/tsp-1.svg"
  alt="A weighted, complete graph with five vertices."
  style="width:475px;"
/>
</center>

Then the solution to the TSP for this graph is the following:

<center>
<img
  src="/images/tsp-2.svg"
  alt="A weighted, complete graph with five vertices and the highlighted solution to the traveling salesman problem."
  style="width:475px;"
/>
</center>

The solution is to traverse the graph by visiting the vertices in the following order: `[0, 1, 2, 3, 4]`, and then back to vertex `0`, which requires a distance of `10 + 76 + 69 + 30 + 26 = 211`.

Recall from the lessons this week that the TSP is an NP-hard problem, so there is no known efficient algorithm for it. Algorithms that compute the *exact* solution to the TSP, such as the brute force algorithm, require `O(n!)` steps, whereas approximation algorithms are able to run faster but don't always compute the exact solution.

Note: for the purposes of this assignment, we are assuming that we are using only *complete* graphs, where every vertex is neighbors with every other vertex.

Task 1 will ask you to finish the implementation of the brute-force approach to solving the TSP.

Task 2 will ask you to finish an approximation algorithm for solving the TSP.

## Steps to Complete

Complete the following steps to the best of your ability, and with the following guidelines:

* The use of generative AI tools (e.g., ChatGPT) is not permitted.
* You must only use concepts and programming constructs covered in this class or previous Kibo classes.
* The algorithms you write should be as efficient as possible.

1. In `tsp.py`, the `brute_force()` method is the start of an algorithm for computing the TSP. Most of the algorithm is written for you; you will need to implement the subroutine `__total_distance_permutation()`.

    In general, the brute force algorithm works as follows:

    1. Consisder every possible way of visiting all vertices. For example, in a graph with three vertices (0, 1, and 2), you could visit all vertices in this order: `[0, 1, 2, 0]` (you need to go back to 0 to complete the traveling salesman cycle).

        However, you could also visit all of the vertices in this order: `[1, 2, 0, 1]`, or this order: `[0, 2, 1, 0]`. The `brute_force()` method uses a library called `itertools` to compute all possible such *permutations* of the order in which to visit the vertices.

    2. For each permutation, compute the total distance of the path that is represented by that permutation. For example, to compute the total distance for the path permutation `[0, 1, 2, 0]`, you would need to sum the weights of the following edges: `(0, 1)`, `(1, 2)`, and `(2, 0)`.

    3. The permutation with the minimum total path distance is the solution to the TSP. The solution consists of both the path itself (e.g., `[0, 1, 2, 0]`) and the cost of the path (e.g., 80).

    Implement the `__total_distance_permutation()` method, which represents step 2 of the algorithm described above. Each call to `__total_distance_permutation()` should accept a permutation as input (e.g., `[0, 1, 2, 0]`), and compute the total distance of the path represented by that permutation.

    Notes:

    * You should only modify the `__total_distance_permutation()` method; you should *not* alter the `brute_force()` method itself.
    * Remember that the total cost of the path must also include the cost of getting from the last city to the starting city.
    * All of the edge weights can be found in the `self.adjacency_matrix` field.
    * For the purposes of this assignment, you can assume the graph is a complete graph.

2. The `nearest_neighbor()` method implements the *nearest neighbor* approximation algorithm. Some of the code is written for you, but you will need to finish implementing the method.

    The nearest neighbors algorithm works as follows:

    1. Start the algorithm at vertex 0. Mark the vertex as visited using the `visited` list.

    2. Among all of the neighbors of the vertex, pick the unvisited neighbor with the lowest edge weight. From the starting vertex, there are `n - 1` possible vertices to pick from. Once you pick the next vertex to visit, mark it as visited using the `visited` list.

    3. Repeat the algorithm, choosing the lowest cost, unvisited neighbor at each step and marking the `visited` list as appropriate.

    4. Once all vertices have been visited, add the cost of getting from the final vertex back to the original vertex.

    The nearest neighbors algorithm is an example of a *greedy* algorithm -- it makes decisions based on what is *locally* the best choice (e.g., the nearest unvisited neighbor at each vertex), but those decisions may not be *globally* the best choice. For this reason, the nearest neighbors algorithm often does not compute the exact answer like the brute force algorithm does, but instead computes an approximation.

    Notes:

    * As the algorithm progresses, you will need to keep track of which vertices have been visited using the `visited` list. For example, to mark vertex 0 as visited, set `visited[0] = True`.
    * You should also be appending to the `tour` list to keep track of the order in which the vertices were visited, so that you can return it. Don't forget to add the starting element to the end of the list to represent the full cycle.
    * In theory, the algorithm could start at any vertex. However, for consistency in grading, you should start the algorithm at vertex 0.
    * Hint: the algorithm should use nested loops; an outer loop for iterating over every vertex, and an inner loop that iterates over that vertex's neighbors to find the closest unvisited neighbor.

## Testing

In `test_tsp.py`, there are unit tests for the above pieces of functionality. Run the tests to check your code.

When you upload your submission to Gradescope, you will see the results for some tests, but there may be other edge cases we test during grading that you are not able to see when you submit. So be sure to test thoroughly!
