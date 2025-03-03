"""
A login management system that uses an open addressing hash table.
"""
class LoginManager:
    # A space is empty if it has never had a value.
    EMPTY = -1
    # A space is removed if it previously had a value,
    # but it has since been deleted.
    REMOVED = -2

    """
    Constructor for the LoginManager class.
    """
    def __init__(self, length, max_load_factor=0.7):
        self.table = length * [self.EMPTY]
        self.num_users = 0
        self.max_load_factor = max_load_factor

    """
    Hash function that uses the length of the key.
    """
    def hash_func(self, key):
        return len(key) % len(self.table)

    """
    Resizes the table to be twice the size that it previously was.
    """
    def resize_table(self):
        # Save a reference to the old table.
        old_table = self.table
        # Create a new table that is twice the size of the old table.
        self.table = [self.EMPTY] * (2 * len(old_table))
        # Reset the number of users to 0.
        self.num_users = 0
        # Re-insert all of the old users into the new table.
        for user in old_table:
            if user != self.EMPTY and user != self.REMOVED:
                self.register_user(user[0], user[1])

    """
    Register a new username and password combination by adding them to the table.
        Returns True if the user was able to be registered and added to the table.
        Returns Falsae if the table is full or if the user already exists.
    """

    def register_user(self, username, password):
        # if table is full, resize the table 
        if self.num_users / len(self.table) >= self.max_load_factor:
            self.resize_table()

        i = self.hash_func(username)

        ht = self.table
        num_checked = 0
        removed_spaces = []

        while num_checked < len(ht) and ht[i] != self.EMPTY and (ht[i] == self.REMOVED or ht[i][0] != username):
            if ht[i] == self.REMOVED:
                removed_spaces.append(i)
            i = (i + 1) % len(ht)
            num_checked += 1

        # If the table is full or the user already exists, return False.
        if num_checked >= len(ht) or ht[i] != self.EMPTY:
            # User already exists in the table.
            return False
 
        # Add the user to the table.
        if removed_spaces != []:
            i = removed_spaces[0]

        ht[i] = (username, password)
        self.num_users += 1
        return True

    """
    Deletes a user from the system by removing them from the table.
        Returns True if the user was removed from the table.
        Returns false if the user was not found in the table.
    """
    def delete_user(self, username):
        i = self.hash_func(username)
        num_checked = 0
        while num_checked < len(self.table) and self.table[i] != self.EMPTY and \
                (self.table[i] == self.REMOVED or self.table[i][0] != username):
            i = (i + 1) % len(self.table)
            num_checked += 1

        if num_checked >= len(self.table) or self.table[i] == self.EMPTY:
            # User was not found in the table.
            return False

        # Remove this user from the table.
        self.table[i] = self.REMOVED
        self.num_users -= 1
        return True

    """
    Checks whether a user can log into the system using the given username and password.
        Returns True if the given (username, password) combination exists.
        Returns False if the given user cannot be found or if the password is incorrect.
    """
    def login(self, username, password):
        # Find the user in the table.
        i = self.hash_func(username)
        ht = self.table
        num_checked = 0
        while num_checked < len(ht) and ht[i] != self.EMPTY or ht[i] == self.REMOVED:
            if ht[i][0] == username and ht[i][1] == password:
                    return True
            i = (i + 1) % len(ht)
            num_checked += 1
        return False

    

    """
    Merges two old accounts into a new account.
        Returns True if the two accounts were successfully replaced by the new account.
        Returns False if the two accounts could not be replaced by the new account.
        old_account1 is a (username, password) tuple.
        old_account2 is a (username, password) tuple.
        new_account is a (username, password) tuple.
    """
    def merge_accounts(self, old_account1, old_account2, new_account):
            # Find the two old accounts in the table.

        ht = self.table
        i = self.hash_func(old_account1[0])
        num_checked = 0
        while num_checked < len(ht) and ht[i] != self.EMPTY and ht[i] != self.REMOVED and ht[i] != old_account1:
            i = (i + 1) % len(ht)
            num_checked += 1

        if num_checked >= len(ht) or ht[i] == self.EMPTY:
            # old_account1 was not found in the table.
            return False
        
        j = self.hash_func(old_account2[0])

        num_checked = 0
        while num_checked < len(ht) and ht[j] != self.EMPTY and ht[j] != self.REMOVED and ht[j] != old_account2:
            j = (j + 1) % len(ht)
            num_checked += 1

        if num_checked >= len(ht) or ht[j] == self.EMPTY:
            # old_account2 was not found in the table.
            return False
        
        # Delete the two old accounts from the table.

        self.delete_user(old_account1[0])
        self.delete_user(old_account2[0])

        # Register the new account in the table.
        self.register_user(new_account[0], new_account[1])
        return True


    def skip3_probe():
        return [
            # initial iteration:
            [ -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
            # dog
            [ -1, -1, -1, 'dog', -1, -1, -1, -1, -1, -1, -1],
            # zebra
            [ -1, -1, -1, 'dog', -1, -1, -1, -1, -1, 'zebra', -1],
            # cat
            [ -1, -1, 'cat', 'dog', -1, -1, -1, -1, -1, 'zebra', -1],
            # giraffe
            [ -1, -1, 'cat', 'dog', -1, 'giraffe', -1, -1, -1, 'zebra', -1],
            # bird
            [ -1, 'bird', 'cat', 'dog', -1, 'giraffe', -1, -1, -1, 'zebra', -1],
            # alpaca
            [ 'alpaca', 'bird', 'cat', 'dog', -1, 'giraffe', -1, -1, -1, 'zebra', -1],
            # alligator
            [ 'alpaca', 'bird', 'cat', 'dog', 'alligator', 'giraffe', -1, -1, -1, 'zebra', -1],
            # elephant
            [ 'alpaca', 'bird', 'cat', 'dog', 'alligator', 'giraffe', -1, 'elephant', -1, 'zebra', -1],
            # baboon
            [ 'alpaca', 'bird', 'cat', 'dog', 'alligator', 'giraffe', -1, 'elephant', -1, 'zebra', 'baboon'],
        ]
