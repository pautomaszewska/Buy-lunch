from django.db.models import Sum
from .models import Points


def points(request):
    if request.user.is_authenticated:
        count_points = Points.objects.filter(user=request.user).aggregate(Sum('amount'))
        all_points = count_points['amount__sum']
    else:
        all_points = 0

    return {
        'points': all_points,
    }