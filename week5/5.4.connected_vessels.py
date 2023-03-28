
# -- connected vessels -- #
def interleave(*iterables):
    """
    Accepts one or more iterable parameters, and returns the list of nested members.
    :param iterables: one or more iterable parameters.
    """
    length = range(max(len(lst) for lst in iterables))
    for index in length:
        for var in iterables:
            if index < len(var):
                yield var[index]


if __name__ == '__main__':
    my_list = []
    for item in interleave('abc', [1, 2, 3], ('!', '@', '#')):
        my_list.append(item)
    print('The output is: ' + str(my_list))
