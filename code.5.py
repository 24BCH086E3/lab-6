tuples = [(), (1, 2), (), (3, 4), ()]
cleaned = [t for t in tuples if t]
print("After removing empty tuples:", cleaned)
