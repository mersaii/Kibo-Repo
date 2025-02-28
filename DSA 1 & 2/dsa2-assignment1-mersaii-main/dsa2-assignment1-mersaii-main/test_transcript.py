import unittest
import io
import sys
from transcript import Transcript

class TestTranscript(unittest.TestCase):
    def setUp(self):
        self.t = Transcript()

    def test_add_two_nodes(self):
        self.t.add('CS 111', 2012, [])
        self.t.add('CS 112', 2013, ['CS 111'])
        lst_str = self.t.to_string()
        self.assertEqual(lst_str, '(CS 111)-->(CS 112)', msg='add() does not correctly build the linked list')

    def test_add(self):
        self.t.add('CS 111', 2012, [])
        self.t.add('CS 112', 2013, ['CS 111'])
        self.t.add('CS 131', 2014, ['CS 111'])
        self.t.add('CS 132', 2014, ['CS 112', 'CS 131'])
        self.t.add('CS 105', 2010, [])
        lst_str = self.t.to_string()
        self.assertEqual(lst_str, '(CS 105)-->(CS 111)-->(CS 112)-->(CS 131)-->(CS 132)', msg='add() does not correctly build the linked list')

    def test_num_courses_in_year(self):
        courses = [
            ('CS 132', 2014, ['CS 112', 'CS 131']),
            ('CS 131', 2014, ['CS 111']),
            ('CS 112', 2013, ['CS 111']),
            ('CS 111', 2012, []),
            ('CS 105', 2010, [])
        ]
        for c in courses:
            self.t.head = Transcript.CourseNode(c[0], c[1], c[2], self.t.head)
        num_courses = self.t.num_courses_in_year(2014)
        self.assertEqual(num_courses, 2, msg='num_courses_in_year() does not correctly count the courses in a year with multiple courses')

    def test_num_courses_in_year_none(self):
        courses = [
            ('CS 132', 2014, ['CS 112', 'CS 131']),
            ('CS 131', 2014, ['CS 111']),
            ('CS 112', 2013, ['CS 111']),
            ('CS 111', 2012, []),
            ('CS 105', 2010, [])
        ]
        for c in courses:
            self.t.head = Transcript.CourseNode(c[0], c[1], c[2], self.t.head)

        num_courses = self.t.num_courses_in_year(2020) # no courses in 2020
        self.assertEqual(num_courses, 0, msg='num_courses_in_year() does not correctly count the courses in a year with zero courses')

    def test_check_prereqs(self):
        courses = [
            ('CS 132', 2014, ['CS 112', 'CS 131']),
            ('CS 131', 2014, ['CS 111']),
            ('CS 112', 2013, ['CS 111']),
            ('CS 111', 2012, []),
            ('CS 105', 2010, [])
        ]
        for c in courses:
            self.t.head = Transcript.CourseNode(c[0], c[1], c[2], self.t.head)
        self.assertEqual(self.t.check_prereqs(), True, msg='check_prereqs() does not correctly check the prereqs for a transcript that has valid prereqs')

    def test_check_prereqs_invalid(self):
        courses = [
            ('CS 131', 2015, ['CS 111']),
            ('CS 132', 2014, ['CS 112', 'CS 131']),
            ('CS 112', 2013, ['CS 111']),
            ('CS 111', 2012, []),
            ('CS 105', 2010, [])
        ]
        for c in courses:
            self.t.head = Transcript.CourseNode(c[0], c[1], c[2], self.t.head)
        self.assertEqual(self.t.check_prereqs(), False, msg='check_prereqs() does not correctly check the prereqs for a transcript that has invalid prereqs')

    def test_check_get_transcript(self):
        expected_output = '2014\nCS 132\nCS 131\n\n2013\nCS 112\n\n2012\nCS 111\n\n2010\nCS 105\n'
        courses = [
            ('CS 132', 2014, ['CS 112', 'CS 131']),
            ('CS 131', 2014, ['CS 111']),
            ('CS 112', 2013, ['CS 111']),
            ('CS 111', 2012, []),
            ('CS 105', 2010, [])
        ]
        for c in courses:
            self.t.head = Transcript.CourseNode(c[0], c[1], c[2], self.t.head)
        val = self.t.get_transcript()
        self.assertEqual(val, expected_output, msg='get_transcript() does not correctly output the transcript; there may be missing courses or just formatting issues')
