import datetime as dt


def is_future_date(date: str) -> bool:
    """Checks if the date is greater or equal than todays date

    :param date: Date as string in format YYYY-mm-dd
    :return: True if date is valid
    """
    try:
        date = dt.datetime.strptime(date, '%Y-%m-%d')
        if date.date() >= dt.date.today():
            return True
        return False
    except ValueError:
        return False


