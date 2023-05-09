frozen_set_1 = frozenset({"A","B","C","D"})
frozen_set_2 = frozenset({"A",2,"C",4})

frozenset_union = frozen_set_1.union(frozen_set_2)
frozenset_common = frozen_set_1.intersection(frozen_set_2)
frozenset_difference = frozen_set_1 - frozen_set_2
frozenset_distinct = frozenset_union - frozenset_common

print("frozen_set_1:", frozen_set_1)
print("frozen_set_2:", frozen_set_2)
print("frozenset_union:", frozenset_union)
print("frozenset_common:", frozenset_common)
print("frozenset_difference:", frozenset_difference)
print("frozenset_distinct:",frozenset_distinct)