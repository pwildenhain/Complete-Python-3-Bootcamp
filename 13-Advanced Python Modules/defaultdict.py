# A defaultdict will _never_ return a KeyError -- it will just return the default value provided

from collections import defaultdict
# Regular dict behavior
d = {'Key 1': 1}
d['Key 1']

d = defaultdict(object)
# Now this returns object
d['Key 1']
# And add a "Key 1" as a key, with object as the default value
[item for item in d.items()]
# Can the default has to be callable (or None)
d = defaultdict(0)
# But we can use lamda's to do that
d = defaultdict(lambda : 0)
# Gives a zero by default
d['key']
[item for item in d.items()]
# Can also just assign keys the regular way
d['next key'] = 1
[item for item in d.items()]