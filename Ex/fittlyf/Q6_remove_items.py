list_a = ["car", "place", "tree", "under", "grass", "price"]

remove_items_containing_a_or_A = lambda list1: [item for item in list1 if "a" not in item.lower()]

print(remove_items_containing_a_or_A(list_a))