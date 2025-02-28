# Assignment 1

In this assignment, you will use the data structures knowledge and Python skills that you have gained from previous courses to implement a series of functions.

## Your Task

You are given a partial implementation of a class that serves as a transcript system for a university. The system provides the ability to add courses to a student's transcript, check that the prerequisites (order of courses) are valid, and get the transcript as a string.

To begin, you're given transcript.py, which contains a partial implementation of the `Transcript` class. Each `Transcript` object is a linked list of `CourseNode` objects, where each node contains the course name, the year that the student took the course, and the prerequisite courses that must be taken prior to the courses.

You will write four functions to implement other aspects of the `Transcript` class. These four functions will make use of topics such as linked data structures, efficiency and running time, recursion, and stacks and queues.

## Steps to Complete

Complete the methods below with these general guidelines:

1. The methods should be written as efficiently as possible. For example, you should not iterate over linked lists farther than is necessary, or more times than is necessary.
2. Unless otherwise stated, your methods should be `O(1)` in additional space. This means you are allowed to use a constant number of variables, but can't use additional lists, maps, or other data structures.
3. You should not alter the method headers in any way, including adding keyword arguments.
4. Unless otherwise stated, you are free to use either recursion or iteration in your algorithms.

Here are the method descriptions:

1. Complete the `add()` method. This method is called to add a new course to the transcript, and is parameterized with the new course name, the year, and the list of prerequisite courses. The new course should be added to the linked list in *sorted* order by year, with earliest class at the start of the list and the latest class at the end of the list.

    Notes:

    * You will need to create a new `CourseNode` object.
    * If there are already courses in the transcript with the same year as the course to be added, the new course should go *after* the existing courses in the list.
    * Be careful to consider all edge cases, including (but not limited to): adding the first node of the list and adding a new node to the beginning of an existing list.
    * You can see the contents of the linked list by printing the string returned by the given `to_string()` method.

2. Complete the `num_courses_in_year()` method. This method should iterate over the transcript, and count the number of courses that occurred in the given year.

    Notes:

    * This method must be written recursively. We have given you the start of the recursive helper method for you to implement.
    * There are multiple base cases for this method.
    * This method should assume that the linked list is sorted by year.
    * If the transcript is empty, 0 should be returned.

3. Complete the `check_prereqs()` method. This method should consider each course in the transcript, and check whether all of that course's prerequisites are satisfied. A prerequisite for a course is satisfied if the prerequisite is taken in any year before the course itself.

    Notes:

    * This method should assume that the linked list is sorted by year.
    * One way that this method could be implemented is to store temporary results in a data structure (such as a map), and use that map to help formulate your answer. However, in keeping with the general guidelines above, you should *not* use this approach. Your answer here should be `O(1)` in additional space.
    * As a comment before the `check_prereqs()` method, state the big-O running time of your algorithm, and explain your answer.
    * If the transcript is empty, `True` should be returned.

4. Complete the `get_transcript()` method. This method should build the transcript as a string, *with the most recent year at the top and least recent year at the bottom* (i.e., in reverse chronological order), and return that string.

    The format of the transcript is:

    ```
    year
    course
    ...
    course

    year
    course
    ...
    course

    ...
    ```

    For example:

    ```
    2014
    CS 132
    CS 131
    
    2013
    CS 112
    
    2012
    CS 111
    
    2010
    CS 105
    ```

    Notes:

    * You can use either a stack or a queue to help implement this method, depending on what you think is more appropriate. If using a stack, you should use a Python list with the `append()` and `pop()` functionality. If using a queue, you should use a Python `deque`. You may not use a map.
    * If the transcript is empty, the empty string should be returned.

## Testing

In `test_transcript.py`, there are unit tests for each of the four methods described above. Some of the unit tests depend on the `add()` method being written correctly.

When you upload your submission to Gradescope, you will see the results for some tests, but there may be other edge cases we test during grading that you are not able to see when you submit. So be sure to test thoroughly!
