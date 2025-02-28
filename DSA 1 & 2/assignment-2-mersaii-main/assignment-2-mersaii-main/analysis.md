# Assignment 2 Analysis

## Task 1: Mystery Sort

### Random List Results

Below is the table of results from running the mystery sort on random lists of various sizes:

| List Size | Number of Comps | Number of Moves |
|-----------|-----------------|-----------------|
| 1000      |    499500       |     716376      |
| 2000      |    1999000      |     3008142     |
| 4000      |    7998000      |     12051537    |
| 8000      |    31996000     |     48238227    |

*Insert your analysis of the experimental results here.*
Above, doubling the input size increases the number of comparisons by a factor of approximately 4. There is a 4x increase in the number of comparison when the list size increases by 2x this implies a time complexity of O(n^2). 

Also, there is a 4x increase in the number of moves when the list size increases in size by 2x and so the time complexity is O(n^2). 

The time complexity of the mystery sort algorithm on a random list is O(n^2) + O(n^2) = O(n^2)

### Almost-Sorted List Results

Below is the table of results from running the mystery sort on almost-sorted lists of various sizes:

| List Size | Number of Comps | Number of Moves |
|-----------|-----------------|-----------------|
| 1000      |   499500        |  1344           |
| 2000      |   1999000       |  2832           |
| 4000      |   7998000       |  6006           |
| 8000      |   31996000      |  11475          |

*Insert your analysis of the experimental results here.*
There is a 4x increase in the number of comparison when the list size increases by 2x this implies a time complexity of O(n^2).

There is a 2x increase in the number of moves when the list size increases in size by 2x. Here, The number of moves made by the algorithm is much lower for an almost sorted input. This suggests that the mystery sort algorithm has a better time complexity for almost sorted inputs. Since the number of moves increases linearly with the input size, this suggests the time complexity is O(n)

The time complexity of the mystery sort algorithm on a random list is O(n^2) + O(n) = O(n^2)

## Task 2: Radix Sort

### Random List Results

Below is the table of results from running radix sort on random lists of various sizes:

| List Size | Number of Moves |
|-----------|-----------------|
|  1000     |     5000        |
|  2000     |     10000       |
|  4000     |     20000       |

*Insert your analysis of the experimental results here.*
There is a 2x increase in the number of moves when the list size increases by 2x this implies a time complexity of O(n).
This means as the list size increases the number of moves required to sort the list will increase accordingly.

The time complexity of the radix sort algorithm on a random list is O(n)
### Almost-Sorted List Results

Below is the table of results from running radix sort on almost-sorted lists of various sizes:

| List Size | Number of Moves |
|-----------|-----------------|
|  1000     |    5000         |
|  2000     |    10000        |
|  4000     |    20000        |

*Insert your analysis of the experimental results here.*
There is a 2x increase in the number of moves when the list size increases by 2x this implies a time complexity of O(n).
This means as the list size increases the number of moves required to sort the list will increase accordingly.

The time complexity of the radix sort algorithm on an almost-sorted lists is O(n)