import random
import datetime


def random_date(start_date, end_date):
    """
    Returns a random date between two dates (inclusive).
    :param start_date: The start date
    :param end_date: The end date.
    :return:  datetime: A random date between start_date and end_date (inclusive).
    """
    # Calculate the time difference between start_date and end_date
    delta = end_date - start_date

    # Generate a random number of seconds between 0 and the total number of seconds in delta
    random_seconds = random.randint(0, delta.total_seconds())

    # Add the random number of seconds to start_date to get a random datetime object
    rand_date = start_date + datetime.timedelta(seconds=random_seconds)
    return rand_date


def is_valid(date):
    """
    check if the input is valid date as DD/MM/YYYY
    :param date: string of input
    :return: true if the string has the struct DD/MM/YYYY
    """
    parts = date.split('/')
    if not all(map(lambda x: x.isdigit(), parts)):
        return False
    day = int(parts[0])
    month = int(parts[1])
    year = int(parts[2])
    if day < 1 or day > 31 or len(parts[0]) != 2:
        return False
    if month < 1 or month > 12 or len(parts[1]) != 2:
        return False
    if year < 0 or month > 2100:
        return False
    return True


def get_date(number):
    """
    get the date from the user
    :param number: string of the sequence number of the input
    :return: the date
    """
    date = input("enter the " + number + " date: (in DD/MM/YYYY) ")
    while not is_valid(date):
        date = input("wrong input try again")
    return datetime.datetime.strptime(date, "%d/%m/%Y").date()


def vinigrate():
    """
    Receives as input from the user two dates in the configuration: YYYY-MM-DD.
    and generates a new date that is between the two dates the user entered as input.
    If the date falls on a Monday, print: "I have no vinaigrette!"
    :return:
    """
    start_date = get_date("start")
    end_date = get_date("end")
    randomly_date = random_date(start_date, end_date)
    print(randomly_date)
    if randomly_date.strftime('%A') == "Monday":
        print("אין לי ויניגרט!")


def main():
    vinigrate()


if __name__ == '__main__':
    main()
