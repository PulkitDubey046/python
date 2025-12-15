# filter(function, iterable) function returns an iterator that yields those items of iterable for which function(item) is true.
# map(function, iterable) function returns an iterator that applies function to every item of iterable,

seq = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd = lambda x: True if x % 2 != 0 else False
filtered_odd = filter(odd, seq)
print(filtered_odd) # yielding the results.
print(list(filtered_odd)) # converting the iterator to list to see the results.

mapped_even = map(lambda x: x * 2, seq)
print(mapped_even) # yielding the results.
print(list(mapped_even)) # converting the iterator to list to see the results.