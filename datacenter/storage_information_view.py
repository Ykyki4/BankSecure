from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.utils.timezone import localtime


def get_duration(enter_time):
    time_current = localtime()
    time_spent = time_current - enter_time
    return(time_spent)

def format_duration(time_spent):
    seconds = time_spent.total_seconds()
    hours = seconds // 3600
    minutes = (seconds % 3600) //60
    return f"{int(hours)}:{round(int(minutes))}"


def storage_information_view(request):
    visits = Visit.objects.filter(leaved_at=None)
    non_closed_visits = [
        {
            'who_entered': "",
            'entered_at': "",
            'duration': "",
            'is_strange': ""
        }
    ]
    for visit in visits:
        enter_time = visit.entered_at
        visiter_name = visit.passcard.owner_name
        time_spent = get_duration(enter_time)
        time_spent_minutes = time_spent.total_seconds() // 60
        if time_spent_minutes > 60:
            is_strange = True
        else:
            is_strange = False
        non_closed_visits.append(
            {
                'who_entered': visiter_name,
                'entered_at': enter_time,
                'duration': format_duration(time_spent),
                'is_strange': is_strange
            }
        )
    context = {
        'non_closed_visits': non_closed_visits,  # не закрытые посещения
    }
    return render(request, 'storage_information.html', context)
