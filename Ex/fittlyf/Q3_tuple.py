t_1 = (1,4,9,16,25,36)

t_modified = tuple(i**2 for i in t_1)

element = t_modified[4]

t_sliced = t_modified[1:4]

print("t_1 :", t_1)
print("t_modified :",t_modified)
print("Element at index position 4 of t_modified :",element)
print("t_sliced :",t_sliced)