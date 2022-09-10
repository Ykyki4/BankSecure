from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render, get_object_or_404
from datacenter.storage_information_view import format_duration


def passcard_info_view(request, passcode):
    passcard = get_object_or_404(Passcard, passcode=passcode)
    all_visits = Visit.objects.filter(passcard=passcard)

    this_passcard_visits = [
        {
            'entered_at': "",
            'duration': "",
            'is_strange': False
        },
    ]
    for visit in all_visits:
        if visit.leaved_at is not None:
            time_spent = visit.leaved_at - visit.entered_at
        duration = format_duration(time_spent)
        time_spent_minutes = time_spent.total_seconds() // 60
        if time_spent_minutes > 60:
            is_strange = True
        else:
            is_strange = False

        this_passcard_visits.append(
            {
                'entered_at': visit.entered_at,
                'duration': duration,
                'is_strange': is_strange
            }
        )
    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
