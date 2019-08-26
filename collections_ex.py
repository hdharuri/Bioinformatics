import collections
import itertools
string1 = 'harish'

#c = collections.Counter(string1)
iterable = [40, 30, 50, 46,39, 44]

it = iter(iterable)
d = collections.deque(itertools.islice(it, 2))
d.appendleft(0)
s = sum(d)
for elem in it:
    print(elem)
print(d)
print(s)
