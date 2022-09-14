from django.utils.timezone import localtime


def get_duration(visit):
    time_spent = localtime(visit.leaved_at) - visit.entered_at
    return time_spent


def format_duration(time_spent):
    seconds = time_spent.total_seconds()
    hours = seconds // 3600
    minutes = (seconds % 3600) //60
    return f"{int(hours)}:{round(int(minutes))}"


def is_strange(time_spent):
    time_spent_minutes = time_spent.total_seconds() // 60
    return time_spent_minutes > 60
