import datetime
import random

# --I don't have Vinaigrette-- #
def get_date(from_date, to_date):
    """
    # Generates a new date that is between the two given dates from the user.
    :param from_date:start date
    :param to_date: finish date
    :return: a random date between the two given dates
    """
    # from string to datetime
    from_date = datetime.datetime.strptime(from_date, '%Y-%m-%d')
    to_date = datetime.datetime.strptime(to_date, '%Y-%m-%d')
    # random a date between the two given dates
    dis = to_date - from_date
    days_num = random.randint(0, dis.days)
    random_date = from_date + datetime.timedelta(days=days_num)

    print("The random is", random_date.strftime('%Y-%m-%d'))

    # if the random date is Monday
    if random_date.weekday() == 0:
        print("I don't have vinaigrette!")


if __name__ == '__main__':
    # --I don't have Vinaigrette-- #
    first_date = input("Enter from date (YYYY-MM-DD): ")
    second_date = input("Enter to date (YYYY-MM-DD): ")
    get_date(first_date, second_date)