from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render, get_object_or_404
from datacenter.views_helpers import format_duration, is_strange


def passcard_info_view(request, passcode):
    passcard = get_object_or_404(Passcard, passcode=passcode)
    all_visits = Visit.objects.filter(passcard=passcard)

    this_passcard_visits = []
    for visit in all_visits:
        if visit.leaved_at is not None:
            time_spent = visit.leaved_at - visit.entered_at
        duration = format_duration(time_spent)
        time_spent_minutes = time_spent.total_seconds() // 60

        this_passcard_visits.append(
            {
                'entered_at': visit.entered_at,
                'duration': duration,
                'is_strange': is_strange(time_spent_minutes)
            }
        )
    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
