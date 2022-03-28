print("shashank")
thisset = {"shashank","rupam","ragini"}
print("rupam" in thisset)
print("yes")
for x in thisset:
    print(x)
thisset2 = {"rich"}
thisset.update(thisset2)
thisset.add("nitu")
print(thisset)