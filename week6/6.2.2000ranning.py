import time


def timer(f, *args1, **args2):
    """
    This function calculate the run time of the argument function.
    :param f: The function.
    :param args1: this is the parameters of the function if they are given by position
    :param args2: this is the parameters of the function if they are given by name
    :return: the execution time of the function
    """

    if f(**args2):
        start_run = time.time()
        f(**args2)
        end_run = time.time()
    elif f(*args1):
        start_run = time.time()
        f(*args1)
        end_run = time.time()
    else:
        start_run = time.time()
        f(*args1)
        end_run = time.time()
    return end_run - start_run


if __name__ == '__main__':

    print(timer(print, "Hello"))
    print(timer(zip, [1, 2, 3], [4, 5, 6]))
    print(timer("Hi {name}".format, name="Bug"))

