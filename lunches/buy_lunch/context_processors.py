from django.db.models import Sum
from django.contrib.auth.models import AnonymousUser


def points(request):
    from .models import Points
    if not AnonymousUser:
        count_points = Points.objects.filter(user=request.user).aggregate(Sum('amount'))
        all_points = count_points['amount__sum']
    else:
        all_points = 0

    return {
        'points': all_points,
    }