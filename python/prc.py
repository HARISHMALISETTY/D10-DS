# # import sys

# # my_list = [1, 2, 3, 4, 5]
# # my_tuple = (1, 2, 3, 4, 5)

# # print("List Memory:", sys.getsizeof(my_list), "bytes")
# # print("Tuple Memory:", sys.getsizeof(my_tuple), "bytes")


# import timeit

# list_test = timeit.timeit(
#     stmt="[1,2,3,4,5][2]",
#     number=10000000
# )

# tuple_test = timeit.timeit(
#     stmt="(1,2,3,4,5)[2]",
#     number=10000000
# )

# print("List Time:", list_test)
# print("Tuple Time:", tuple_test)

