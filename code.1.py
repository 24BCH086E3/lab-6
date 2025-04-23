data = ["Alice", ("John",), "Maya", ("Alex",), "Sophia", ("Mark",)]
boys = girls = 0
for ele in data:
    if isinstance(ele, tuple):
        boys += 1
    else:
        girls += 1
print("Number of boys:", boys)
print("Number of girls:", girls)
