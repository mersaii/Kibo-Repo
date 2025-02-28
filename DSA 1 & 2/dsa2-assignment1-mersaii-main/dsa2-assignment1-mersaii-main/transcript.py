class Transcript:
    class CourseNode:
        def __init__(self, course_name, year, prereqs, next):
            self.course_name = course_name
            self.year = year
            self.prereqs = prereqs
            self.next = next

    def __init__(self):
        self.head = None

    def add(self, course_name, year, prereqs):
        # Implement this
        if year < 0:
            raise ValueError("Year must be a positive integer")
        new_course = Transcript.CourseNode(course_name, year, prereqs,next=None)
        if self.head is None or self.head.year > year: # insertion in an empty list or at the begining
            new_course.next = self.head
            self.head = new_course
            return
        trav = self.head
        while trav.next is not None and trav.next.year <= year:
            trav = trav.next
        if trav.next is None: # insertion at the end
            trav.next = new_course
        else:   # insertion in the middle
            new_course.next = trav.next
            trav.next = new_course
        return

    def __num_courses_in_year(self, node, year):
        # Implement this
        if year < 0: # invalid year
            raise ValueError("Year must be a positive integer")
        if node is None or node.year > year: # empty list or year not found
            return 0
        if node.year == year: # year found
            return 1 + self.__num_courses_in_year(node.next, year)
        return self.__num_courses_in_year(node.next, year) # year not found

    def num_courses_in_year(self, year):
        return self.__num_courses_in_year(self.head, year)

    # The big o notation of check_prereqs() is O(n^3) where n is the number of courses in the transcript. This outermost while loop has a time complexity of O(n) and to check the prereqs of each course, the inner while for has a time complexity of O(n) in the worst case scenario, this loop also has an inner while loop which can have a time complexity of O(n) in the worst case scenario. Therefore, the time complexity of the check_prereqs function is O(n^3).
    def check_prereqs(self):
        # Implement this
        if self.head is None: #empty transcript
            return True
        trav = self.head 
        while trav is not None: # traverse the transcript
            for prereq in trav.prereqs: # traverse the prereqs of the current course
                prereq_found = False # flag to check if the prereq is found
                travprereq = self.head
                while travprereq is not None and travprereq.year <= trav.year: # traverse the transcript to find the prereq with the same year or before
                    if travprereq.course_name == prereq:
                        prereq_found = True
                        break
                    travprereq = travprereq.next
                if travprereq is None or travprereq.year > trav.year or not prereq_found: # has reached the end of the transcript, has reached after the current course year or prereq not found
                    return False
            trav = trav.next
        return True

    def get_transcript(self):
        # Implement this
        trav = self.head
        if trav is None:
            return ''
        s = ''
        last_year = None  # to keep track of the last year printed
        stack = []
        while trav is not None:  # traverse the transcript and store the courses in a stack
            stack.append(trav)
            trav = trav.next
        for i in range(len(stack)):  # print the courses in the stack
            curr = stack.pop()
            if last_year is None:
                s += str(curr.year) + '\n'
                last_year = curr.year
            if curr.year != last_year:
                s += '\n' + str(curr.year) + '\n'  # Concatenate the year to the string
                last_year = curr.year
            s += curr.course_name + '\n'  # Concatenate the course name to the string if the year is the last year
        return s


    def to_string(self):
        trav = self.head
        s = ''

        if trav is not None:
            s += '(' + trav.course_name + ')'
            trav = trav.next

        while trav is not None:
            s += '-->(' + trav.course_name + ')'
            trav = trav.next

        return s

