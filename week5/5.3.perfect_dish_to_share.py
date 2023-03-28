def perfect_number(my_num):
    """
     Gets all number's divisors.
    :param my_num: the number that is given from the user.
    :return: the number is a perfect num - return it's divisors, else - return an error.
    """
    int_my_num = int(my_num)
    div_list = [x for x in range(1, int_my_num) if int_my_num % x == 0 and x != int_my_num]
    if sum(div_list) == int_my_num:
        return div_list
    else:
        return 'ERROR'


if __name__ == '__main__':
    user_num = input("Please enter a maximum number to check:")
    list_div_user_num = perfect_number(user_num)
    if isinstance(list_div_user_num[0], int):
        print("The divisors are: " + str(list_div_user_num))
    else:
        print("ERROR! the number that you choose isn't a perfect num.")

