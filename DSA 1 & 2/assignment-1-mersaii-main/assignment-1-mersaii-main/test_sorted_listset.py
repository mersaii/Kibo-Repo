import random
import unittest
from sorted_listset import SortedListSet

class TestSortedListSet(unittest.TestCase):
    def test_insert(self):
        lset = SortedListSet()
        assert lset.insert(1)
        assert lset.insert(2)
        assert lset.insert(3)

        items = lset.to_list()
        assert len(items) == 3
        assert 1 in items and 2 in items and 3 in items

    def test_insert_dup(self):
        lset = SortedListSet()
        assert lset.insert(1)
        assert lset.insert(2)
        assert lset.insert(3)
        assert not lset.insert(3)

    def test_size(self):
        lset = SortedListSet()
        assert lset.insert(1)
        assert lset.insert(2)
        assert lset.insert(3)

        assert lset.size() == 3

    def test_contains(self):
        lset = SortedListSet()
        assert lset.insert(1)
        assert lset.insert(2)
        assert lset.insert(3)

        lst = lset.to_list()
        for i in [1, 2, 3]:
            assert i in lst
        assert lset.contains(2)

    def test_delete_present(self):
        lset = SortedListSet()
        assert lset.insert(1)
        assert lset.insert(2)
        assert lset.insert(3)

        assert lset.delete(2)

        items = lset.to_list()
        assert len(items) == 2
        assert 1 in items and 3 in items

    def test_delete_not_present(self):
        lset = SortedListSet()
        assert lset.insert(1)
        assert lset.insert(2)
        assert lset.insert(3)

        assert not lset.delete(5)

        items = lset.to_list()
        assert len(items) == 3
        assert 1 in items and 2 in items and 3 in items

    def test_sortedness(self):
        lset = SortedListSet()
        for i in range(100):
            lset.insert(random.randint(1, 100))

        items = lset.to_list()
        for i in range(len(items) - 1):
            assert items[i] <= items[i + 1]
