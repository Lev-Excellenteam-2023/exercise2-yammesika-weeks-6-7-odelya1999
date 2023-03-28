import os


# --This is the way -- #
def files_startswith_deep(user_path):
    """
     Gets the folder path from the user, when a file starts with the word "deep" returns it.
    :param user_path: the folder path that is given from the user
    :return: all files that start with the word "deep" into a list
    """
    files = os.listdir(user_path)
    list_files = []
    for f in files:
        if f.startswith("deep"):
            list_files.append(f)
    return list_files


if __name__ == '__main__':
    # --This is the way -- #
    path = input("Please enter a path file: ")
    print(files_startswith_deep(path))

    