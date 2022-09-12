from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.utils.timezone import localtime
from datacenter.views_helpers import get_duration, format_duration, is_strange






def storage_information_view(request):
    visits = Visit.objects.filter(leaved_at=None)
    non_closed_visits = []
    for visit in visits:
        enter_time = visit.entered_at
        visiter_name = visit.passcard.owner_name
        time_spent = get_duration(enter_time)
        time_spent_minutes = time_spent.total_seconds() // 60

        non_closed_visits.append(
            {
                'who_entered': visiter_name,
                'entered_at': enter_time,
                'duration': format_duration(time_spent),
                'is_strange': is_strange(time_spent_minutes)
            }
        )
    context = {
        'non_closed_visits': non_closed_visits,
    }
    return render(request, 'storage_information.html', context)
