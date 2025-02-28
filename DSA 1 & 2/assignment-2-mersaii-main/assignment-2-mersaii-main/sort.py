class Sort:
    def __init__(self):
        self.reset_stats()

    def reset_stats(self):
        self.comps = 0
        self.moves = 0

    def get_comps(self):
        return self.comps

    def get_moves(self):
        return self.moves

    def compare(self, comparison):
        self.comps += 1
        return comparison

    def swap(self, lst, i, j):
        temp = lst[i]
        lst[i] = lst[j]
        lst[j] = temp
        self.moves += 3

    #
    # Task 1
    #

    def mystery_sort(self, lst):
        for i in range(len(lst) - 1, 0, -1):
            for j in range(len(lst) - 1, len(lst) - 1 - i, -1):
                if self.compare(lst[j] < lst[j - 1]):
                    self.swap(lst, j, j - 1)

    #
    # Task 2
    #

    # returns the nth digit of num,
    # where digit 0 is the least significant digit
    # e.g.: digit(1234, 0) -> 4
    def digit(num, n):
        return int(num // 10 ** n % 10)

    # returns a list of buckets of order radix
    # e.g.: get_new_buckets(10) will return a
    # 2D list of 10 empty lists: [ [], [], [], ... ]
    def get_new_buckets(radix):
        buckets = []
        for i in range(radix):
            buckets.append([])
        return buckets

    # first number on list is max_num compare it to all numbers in the list 
    # if number greater than max_num number becomes new max number
    # convert max_num to string and iterate through it and increase counter.
    def get_max_num_digits(lst):
        # Task 2, Step 1
        counter = 0
        max_num = lst[0]

        for number in lst:
            if number > max_num:
                max_num = number
        for i in str(max_num):
            counter += 1           
        return counter
    
    
    # converts a list of numbers to a list
    # of buckets, with entries sorted by
    # their least significant digit
    def list_to_buckets(self,lst):
        # Task 2, Step 2
        buckets = Sort.get_new_buckets(10)
        
        for lst_idx in range(len(lst)):
            for buck_idx in range(len(buckets)):
                least_sign_digit = Sort.digit(lst[lst_idx], 0)
                if least_sign_digit == buck_idx:
                    buckets[buck_idx].append(lst[lst_idx])
                    self.moves += 1   
        return buckets

    # converts a list of buckets 
    # into a one-dimensional list
    def buckets_to_list(self, buckets):
        # Task 2, Step 3
        bucket = []
        for idx in buckets:
            for idx, enum in enumerate(idx):
                bucket.append(enum)
        return bucket
    
    # sort a list of numbers by distributing
    # them to buckets according to their digits
    def radix_sort(self, lst):
        # Task 2, Step 4
        iter = 1
        max_digit = Sort.get_max_num_digits(lst)
        new_bucket = self.list_to_buckets(lst)
        new_lst = self.buckets_to_list(new_bucket)

        while iter <= (max_digit-1):
            buckets = Sort.get_new_buckets(10)
            for bucket_idx in range(len(buckets)):
                for lst_idx in range(len(new_lst)):
                    sign_digit = Sort.digit(new_lst[lst_idx], iter)
                    if sign_digit == bucket_idx:
                        buckets[bucket_idx].append(new_lst[lst_idx])
                        self.moves += 1
            iter += 1  
            new_lst = self.buckets_to_list(buckets)       
        return new_lst