def group_by(f, iterable):
    """
    This function performs operations on a dictionary.
    :param f: A function.
    :param iterable: A list of values.
    :return: A dictionary where the keys are the values returned from the function passed as the first parameter,
     the value corresponding to a particular key is a list of all the members for which the value appearing in the key
     was returned.
    """
    res_dict = {}
    for item in iterable:
        key = f(item)
        if key not in res_dict:
            res_dict[key] = []
        res_dict[key].append(item)
    return res_dict


if __name__ == '__main__':
    print("The output is:")
    dictionary = group_by(len, ["hi", "bye", "yo", "try"])
    for key, value in dictionary.items():
        print(str(key) + ': ' + str(value))

