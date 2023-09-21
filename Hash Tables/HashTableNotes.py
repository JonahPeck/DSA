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
#ord is short for ordinal - grabs the ASCII numerical value for each letter
    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(i, ": ", val)

my_hash_table = HashTable()
my_hash_table.print_table()
