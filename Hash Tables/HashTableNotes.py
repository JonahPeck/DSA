#Hash Tables - dictionaries are made up of a key value pair
#hash tables work through a hash function works by performing a hash on a key and run it through a function and it returns an address for the key value pair
#this is how a dictionary is stored
#Hashes are one way - you can only insert into a hash and recieve an address not vice versa
#Hashes are deterministic - every time a key is put in you will expect to get the same output

#collisions - happens when a key value pair is put in a place where another key value pair already exists
#separate chaining - putting 
#linear probing - form of open addressing - makes sure you don't have more than one key value pair at the same address
#linked list that points to each of the places with the same address

#hash tables should always have a prime number of sections because it increases randomness

class HashTable:
    def __init__(self, size = 7):
        self.data_map = [None] * size

#creating the hash method which creates the address for the key, value pair
    def __hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash
#this line of code above creates the random address hash method by which key value pairs will receive an address
#ord is short for ordinal - grabs the ASCII numerical value for each letter
    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(i, ": ", val)

    def set_item(self, key, value):
        index = self.__hash(key)
        if self.data_map[index] == None:
            self.data_map[index] = []
        self.data_map[index].append([key, value])

    def get_item(self,key):
        index = self.__hash(key)
        if self.data_map[index] is not None:
            for i in range(len(self.data_map[index])):
                if self.data_map[index][i][0] == key:
                    return self.data_map[index][i][1]
        return None
# Get item for a hash table
#learning what's next in hash tables

my_hash_table = HashTable()
my_hash_table.set_item('bolts', 300)
my_hash_table.set_item('washers', 1500)
my_hash_table.set_item('nuts', 700)

print(my_hash_table.get_item('nuts'))
print(my_hash_table.get_item('lumber'))

