import unittest
from fileset import FileSet

class TestFileSet(unittest.TestCase):
    def test_insert(self):
        fset = FileSet("set.txt")
        assert fset.insert(1)
        assert fset.insert(2)
        assert fset.insert(3)

        items = fset.to_list()
        assert len(items) == 3
        assert 1 in items and 2 in items and 3 in items

    def test_insert_dup(self):
        fset = FileSet("set.txt")
        assert fset.insert(1)
        assert fset.insert(2)
        assert fset.insert(3)
        assert not fset.insert(3)

    def test_size(self):
        fset = FileSet("set.txt")
        assert fset.insert(1)
        assert fset.insert(2)
        assert fset.insert(3)

        assert fset.size() == 3

    def test_contains(self):
        fset = FileSet("set.txt")
        assert fset.insert(1)
        assert fset.insert(2)
        assert fset.insert(3)

        assert fset.contains(2)

    def test_delete_present(self):
        fset = FileSet("set.txt")
        assert fset.insert(1)
        assert fset.insert(2)
        assert fset.insert(3)

        assert fset.delete(2)

        items = fset.to_list()
        assert len(items) == 2
        assert 1 in items and 3 in items

    def test_delete_not_present(self):
        fset = FileSet("set.txt")
        assert fset.insert(1)
        assert fset.insert(2)
        assert fset.insert(3)

        assert not fset.delete(5)

        items = fset.to_list()
        assert len(items) == 3
        assert 1 in items and 2 in items and 3 in items
