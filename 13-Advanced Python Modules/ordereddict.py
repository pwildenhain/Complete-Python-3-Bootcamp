# Dictionary subclass that remembers the order in which contents were added.
# Regular dicts are just mappings, they don't retain any order
# OrderedDicts remember the order that contents were added

d = {}
d["a"] = 0
d["b"] = 1
d["c"] = 2
d["d"] = 3
d["e"] = 4
d["f"] = 5
d["g"] = 6

d
# Let's see if the order gets mixed
[key for key in d]
# Ran that ~10 times and it seemed to retain order just fine...
# Let's try getting both at the same time
for k, v in d.items():
    print(k, v)
### UPDATE: dicts are now insertion ordered as of 3.6+
# https://stackoverflow.com/questions/39980323/are-dictionaries-ordered-in-python-3-6
# But ordereddict is still good to know about...
from collections import OrderedDict

d = OrderedDict()
d["a"] = 0
d["b"] = 1
d["c"] = 2
d["d"] = 3
d["e"] = 4
d["f"] = 5
d["g"] = 6

for k, v in d.items():
    print(k, v)
# something ordered dicts are good for can be comparing equality
# These will be equal even though they aren't in the same order
d1 = {'a': 1, 'b': 2}
d2 = {'b': 2, 'a': 1}
d1 == d2
# This won't be the case for OrderedDict
d1 = OrderedDict({'a': 1, 'b': 2})
d2 = OrderedDict({'b': 2, 'a': 1})
d1 == d2
