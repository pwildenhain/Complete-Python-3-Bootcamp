# counter = dictionary subclass, used to count hashable objects
from collections import Counter

l = [1, 1, 1, 2, 3, 4, 4, 5, 6, 5, 5, 5]
# Values = distinct objects in 1
# Key = # of occurences
Counter(l)
# Works similarly with strings
s = 'jslidjfisjfnjsdnvlursnun'
Counter(s)
# What about the words in a sentence?
sentence = "This sentence repeats itself This sentence repeats itself again"
words = sentence.split(" ")
Counter(words)
# Methods of counter
c = Counter(words)
c.most_common(2)
