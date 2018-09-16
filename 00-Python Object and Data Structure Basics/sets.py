# A set is an unordered collection of UNIQUE objects. No repeats!
my_set = set()
my_set
type(my_set)
# Add objects
my_set.add(1)
# Notice it's contained within curly braces like a dict, but with no key value pair
my_set
my_set.add(2)
# I bet it throws an error if I try to add an existing item
my_set.add(2)
# huh, no error, it just doesn't add the duplicate object
my_set.add(1)
# Yea, it just does nothing, if the item already exists in the set
my_set
# Sets are useful for this reason! 
# Example, cast a list as a set to get rid of duplicate values
my_list = [1, 1, 1, 1, 2, 2, 2, 3, 3, 3]
my_set = set(my_list)
# Voila! Instant de-duplication
my_set
# Though keep in mind, sets techincally don't have an order to them
my_set[0] # <- Throws an error