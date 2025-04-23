t = (10, 20, 30)
t = t[:1] + (99,) + t[2:]  # Change element at index 1
print("Modified tuple:", t)
