# -- Cup of join -- #
def join(*lists, sep='-'):
    """
    :param lists: If the parameter 'sep' is provided then it is threaded between any two lists.
    :param sep: Default value is "-".
    :return: All lists obtained as parameters as one list.
    """
    res = []
    for index, l in enumerate(lists):
        if index > 0:
            res.append(sep)
        res.extend(l)

    if res:
        return res
    else:
        print("ERROR!!")


if __name__ == '__main__':
    # -- Cup of join -- #
    join()
    print(join([1, 2, 3], [4, 5, 6], sep='@'))
