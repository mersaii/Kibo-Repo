import ast
import os

class FileSet:
    def __init__(self, fname):
        self.fname = fname
        # remove any already existing set
        try:
            os.remove(fname)
        except FileNotFoundError:
            pass

    def __file_to_list(self):
        try:
            with open(self.fname, 'r', encoding = 'utf-8') as f:
                lines = f.readlines()

                if len(lines) == 0:
                    print("file " + self.fname + " is empty")
                    return []

                if len(lines) > 1:
                    print("file " + self.fname + " has more than one line; invalid")
                    return []

                return ast.literal_eval(lines[0].strip('\n'))
        except FileNotFoundError:
            return []

    def __list_to_file(self, lst):
        with open(self.fname, 'w', encoding = 'utf-8') as f:
            f.write(str(lst).strip('\n'))

    def insert(self, item):
        # Task 2, Step 1: implement this method
        lst = self.__file_to_list()
        
        lst.append(item)
        self.__list_to_file(lst)
        return True

    def contains(self, item):
        # Task 2, Step 2: implement this method
        lst = self.__file_to_list()
        
        counter = lst.count(item)
        if counter > 0:
            return True
        else:
            return False

    def delete(self, item):
        lst = self.__file_to_list()
        
        if item not in lst:
            return False

        lst.remove(item)
        self.__list_to_file(lst)
        return True

    def size(self):
        lst = self.__file_to_list()
        return len(lst)

    def to_list(self):
        return self.__file_to_list()
