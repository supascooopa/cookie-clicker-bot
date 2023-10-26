import datetime


def starting_time():
    """
    :return: time now
    """
    now = datetime.datetime.now()
    return now.time()


def back_up_time(current_time: datetime, seconds: int = 5):
    backup_time = current_time + datetime.timedelta(seconds=seconds)
    return backup_time.time()
