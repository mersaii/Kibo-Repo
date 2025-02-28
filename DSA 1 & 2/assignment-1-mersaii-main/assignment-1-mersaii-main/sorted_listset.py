class SortedListSet:
    def __init__(self):
        self.items = []

    def insert(self, item):
        # Task 3, Step 1: implement this method
        idx = len(self.items)

        
        for each_item in range(idx):
            if self.items[each_item] > item:
                idx = each_item
                break
        
        if idx == len(self.items):
            self.items = self.items[:idx] + [item]
        else:
            self.items = self.items[:idx] + [item] + self.items[idx:]
        return self.items

    def contains(self, item):
        # Task 3, Step 2: implement this method
        try: 
            self.items.index({item})
        except:
            return False

    def delete(self, item):
        if item not in self.items:
            return False

        self.items.remove(item)
        return True

    def size(self):
        return len(self.items)

    def to_list(self):
        return self.items.copy()
