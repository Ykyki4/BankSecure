from datacenter.models import Visit
from django.shortcuts import render
from datacenter.views_helpers import get_duration, format_duration, is_strange


def storage_information_view(request):
    visits = Visit.objects.filter(leaved_at__isnull=True)
    non_closed_visits = []
    for visit in visits:
        enter_time = visit.entered_at
        visiter_name = visit.passcard.owner_name
        time_spent = get_duration(visit)
        non_closed_visits.append(
            {
                'who_entered': visiter_name,
                'entered_at': enter_time,
                'duration': format_duration(time_spent),
                'is_strange': is_strange(time_spent)
            }
        )
    context = {
        'non_closed_visits': non_closed_visits,
    }
    return render(request, 'storage_information.html', context)
