import timeit
print (dir(timeit))
list_test = timeit.timeit(stmt= "[1,2,3,4,5]",
                          number=100000)

tuple_test = timeit.timeit(stmt= "(1,2,3,4,5)",
                           number=100000)
print("List time: ", list_test)
print("Tuple time: ", tuple_test)