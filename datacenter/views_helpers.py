from django.utils.timezone import localtime

def get_duration(enter_time, leaved_at=None):
    time_current = localtime()
    if leaved_at is not None:
        time_spent = leaved_at - enter_time
    else:
        time_spent = time_current - enter_time
    return(time_spent)

def format_duration(time_spent):
    seconds = time_spent.total_seconds()
    hours = seconds // 3600
    minutes = (seconds % 3600) //60
    return f"{int(hours)}:{round(int(minutes))}"

def is_strange(minutes):
    return minutes > 60
