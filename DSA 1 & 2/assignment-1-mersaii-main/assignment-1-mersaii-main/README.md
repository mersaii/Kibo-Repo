# Set ADT

In this assignment, you will implement a set ADT using three different approaches, and benchmark their performance using Python's `timeit` library.

## Your Task

A set has the following properties:

- Each element in the set is unique; there can't be any duplicates
- A set is unordered; there is no notion of "position i" in a set

Sets also have the following operations:

- `insert(item)`: insert an item into the set; returns `True` on successful insertion, `False` otherwise (for example, if the item is already in the set
- `contains(item)`: returns whether the set contains the item
- `delete(item)`: delete an item from the set; returns `True` on successful deletion, `False` otherwise (for example, if the item was not in the set)
- `size()`: returns the number of elements in the set
- `to_list()`: returns the set as a Python list

You are given three partial implementations of the set ADT:

- A `ListSet` in `listset.py`, which implements the set using a Python list
- A `SortedListSet` in `sorted_listset.py`, which implements the set using a Python list object, but maintains all of the elements of the set in sorted order. The idea is that making `insert()` carefully insert each item while maintaining sorted order will make `contains()` and `delete()` faster, since you can use binary search to find the position of an item (or the absence of an item) more quickly than a linear search
- A `FileSet` in `fileset.py`, which implements the set by storing it in a file

You have four high-level tasks:

1. Task 1: Implement the unfinished methods in `ListSet` so that it fully implements the set ADT.
2. Task 2: Implement the unfinished methods in `FileSet` to implement the set ADT.
3. Task 3: Implement the unfinished methods in `SortedListSet` to implement the set ADT.
2. Task 4: Benchmark the performance of each of the three set implementations to compare their relative speeds when running the `contains()` operation.

## Starter Code

You are given several files to start with. It is recommended that you read through the given files to gain an understanding of what is already provided, and what you must implement. The files are:

- Classes that implement the set ADT in `listset.py`, `sorted_listset.py`, and `fileset.py`. Each class is missing some functionality that you will implement, as described below.
- Unit tests of each implementation, in `test_listset.py`, `test_sorted_listset.py`, and `test_fileset.py`. Each of these files contain the same unit tests, checking the correctness of `insert()`, `contains()`, `delete()`, etc. Additionally, `test_sorted_listset.py` contains an extra test to check whether the list is being maintained in sorted order.
- A main script, `main.py`, where you will implement benchmarking code.

## Testing

We have provided all of the unit tests you should need to test for basic functional correctness of the set implementations, but you are welcome to add more unit tests in any of the testing files.

## Steps to Complete

Your first task is to finish the implementations of the three types of sets. Whenever you are implementing a method, remember to remove the `pass` statement that is currently a placeholder in the method body.

You may find it useful to review the properties and expected behavior of the set ADT above.

### Task 1: Finish `ListSet` 

1. Implement the `insert()` method in `listset.py`. Remember that the method should return `True` only if the insertion was successful.

2. Implement the `contains()` method in `listset.py`. For the purposes of this assignment, you should *not* use the `in` operator.
<br><br>
At this point, you should be able to run the unit tests for `ListSet` in `test_listset.py`. If there are any failures, revisit your implementations of `insert()` and `contains()`.

### Task 2: Finish `FileSet` 

1. Implement the `insert()` method in `fileset.py`. The point of the `FileSet` implementation is to store the set in a file (on disk) when not actively in use by a method call. During a method call, the set is read from the file into a Python list.
<br><br>
We have given you the following methods, which take care of reading the set from the file and writing it back to the file:
    - `__file_to_list()`: reads the set from the file it's stored in, and returns it as a Python list
    - `__list_to_file()`: writes the set (stored in a Python list) to the file

See the implementation of the `delete()` method to see how these file methods are used. Your `insert()` method should make use of both of these functions to read the set in from the file to a Python list, modify the list (if needed), and then write the list back to the file.
<br><br>
The items in the `FileSet` do not need to be kept in sorted order.

2. Implement the `contains()` method in `fileset.py`. This method will also require you to read in the set from the file, but will not require you to write the set back to the file.
<br><br>
At this point, you should be able to run the unit tests for `FileSet` in `test_fileset.py`. If there are any failures, revisit your implementations of `insert()` and `contains()`.

### Task 3: Finish `SortedListSet` 

1. Implement the `insert()` method in `sorted_listset.py`. Remember that the point of this implementation of the set is to keep the set in sorted order to try to make the `contains()` method run a little bit faster. Therefore, `insert()` should make sure that the new item is inserted in sorted order. To do so, you should make use of the following algorithm:

    When `insert()` is invoked, the expectation is that the list is in sorted order. In this case, we want to insert `8` into the already sorted list:

    <center>
    <img
      src="/images/assignment-1-list-1.svg"
      alt="Inserting an 8 into an already sorted list."
      style="width:400px;"
    />
    </center>

    To do so, you can iterate over the contents of the list until you've found the position where the `8` belongs. If there is not already an `8` present, you can use list slicing to split the current list apart and add the `8` between them:

    <center>
    <img
      src="/images/assignment-1-list-2.svg"
      alt="The sorted list with 8 now an element of it."
      style="width:400px;"
    />
    </center>

2. Implement the `contains()` method in `sorted_listset.py`. This method should try to take advantage of the fact that the list is sorted by stopping the search once you can be sure that the item is not in the list.
<br><br>
Because we want to take advantage of the sortedness of the list, you should *not* use the `in` operator, which will be unaware of the fact that the list is sorted, and will search the entire list.
<br><br>
At this point, you should be able to run the unit tests for `SortedListSet` in `test_sorted_listset.py`. If there are any failures, revisit your implementations of `insert()` and `contains()`.

## Task 4: Benchmark the `contains()` method

You will now write the code in `main.py` to benchmark the different set implementations. Read through the code already given in `main.py` to get a feel for how it is organized. To summarize, it prompts the user for a set implementation and creates an instance of that set. The remaining steps are up to you to complete below.

Note: in this task, you should *not* change the constants `NUM_SET_ITEMS`, `ITEM_VALUE_DOMAIN`, or `NUM_TESTS`.

1. Find the line of code in `main.py` marked "Task 4, Step 1." This is where you will populate the set object `s` with randomly generated integers. For each of the iteration of the loop, you should generate a random number in the range `[0, ITEM_VALUE_DOMAIN]` and add it to the set. To do so, you may find it helpful to consult the documentation for Python's [random](https://docs.python.org/3/library/random.html) module and find an appropriate method for generating an integer within a range.

2. Find the line of code in `main.py` marked "Task 4, Step 2." This is where you will populate the list of test cases -- values we will use to test the `contains()` method. Using the same approach as in (1), populate the `test_samples` list with `NUM_TESTS` random numbers drawn from the range `[0, ITEM_VALUE_DOMAIN]`.

3. Find the line of code in `main.py` marked "Task 4, Step 3." This is where we will benchmark the call to the `contains()` the set. Currently, there is a placeholder line of code that includes this expression:
    ```python
    timeit.timeit(stmt='pass', number=1, globals=globals())
    ```
    This is using Python's [timeit](https://docs.python.org/3/library/timeit.html) module to record how long the given code fragment takes to execute. Currently, the given statement is just `pass`, meaning it is not doing anything of value. `number=1` tells `timeit` that we want to run this operation once, and `globals=globals()` makes it so that the variable names that are currently in the scope of the Python program can be used in the `stmt`.
    <br><br>
    Replace `'pass'` with `'s.contains(sample)'`, since that is the code we wish to execute and benchmark.
    <br><br>
    The `timeit()` function will return the time it takes (measured in seconds) to execute the statement.

4. The benchmarking test is almost ready to be run! Before we do so, let's add some code to show how long the evaluation takes. Under "Task 4, Step 4," add code to show the results of the test, both in terms of the overall time it took to run all of the samples, as well as the average time per call to the `contains()` method. It should look like this:
    ```txt
    Benchmarking contains()...
      total time (1000 calls): 0.12535749400740315 seconds
      average time per call: 0.00012535749400740314 seconds
    ```

5. Try running `main.py` for each of the set implementations. Note that the `FileSet` will take a longer time than the others -- including the time it takes to populate the set with `insert()`!
<br><br>
Think about the results that you see. Do they make sense? Refer back to our discussion of how fast accesses of main memory are compared to disk accesses. We said disk accesses are approximately 80x slower. Do the results you see agree with that statement? You don't need to submit answers to these questions.

## Extra Challenge

Looking for an extra challenge? Consider the following extension to this assignment. This is optional -- only complete it if you want to!

Think back to our implementation of `SortedListSet`. Since the list is sorted, you can implement `contains()` using [binary search](https://en.wikipedia.org/wiki/Binary_search_algorithm), which was described in P1 as a technique for reducing the number of guesses needed in the number guessing game.

The basic idea is to repeatedly divide the list in half and check if the item you are looking for is in that half. The process is repeated until you either find the item, or can determine that the item is not in the list.

Once implemented, this should speed up the `contains()` method even further!
