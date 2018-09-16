my_dict = {'key1':'value1', 'key2':'value2'}
my_dict
# Index through keys, instead of positions
my_dict['key1']
# Can contain any value type
prices_lookup = {'apples':2.99, 'oranges':1.99, 'milk':5.80}
prices_lookup
# Easily return value
prices_lookup['apples']
# dictionaries are very flexible
d = {'k1':123, 'k2':[0, 1, 2], 'k3':{'insideKey':100}}
d['k2']
# Access multiple levels
d['k2'][2]
d['k3']['insideKey']
# Perform methods on objects inside the dict
d = {'k1':['a', 'b', 'c']}
d['k1'][0].upper()
# But that method doesn't change the list in the dict
d
# Adding items to dict
d = {'k1':100, 'k2':200}
d['k3'] = 300
d
# Similar method to overwrite existing value
d['k1'] = 10
d
# Useful methods
# Return all keys
d.keys()
# Return all values
d.values()
# Return items
d.items()
