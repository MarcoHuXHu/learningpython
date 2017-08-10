def test_args(first, second, third):
    print ('First argument: ', first)
    print ('Second argument: ', second)
    print ('Third argument: ', third)

# Use *args
args = [1, 2, 3]
test_args(*args)
# results:  # First argument:  1    # Second argument:  2   # Third argument:  3
# test_args(args)
# results:  TypeError: test_args() missing 2 required positional arguments: 'second' and 'third'

# Use **kwargs
kwargs = {
    'first': 1,
    'second': 2,
    'third': 3
}

test_args(**kwargs)
# results:  # First argument:  1    # Second argument:  2   # Third argument:  3
test_args(*kwargs)
# results:  # First argument:  second   # Second argument:  first   # Third argument:  third
