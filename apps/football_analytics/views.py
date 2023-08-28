

""" FOOTBALL VIEWS """


from django.shortcuts import render
from .models import Match, Banner

def matches_list(request):
    matches = Match.actual.all()
    active_banners = Banner.objects.filter(is_active=True)
    context = {'matches': matches,
               'active_banners': active_banners}
    return render(
        template_name='MatchList.html', 
        request=request, 
        context = context
        )

# def base(request):
#     active_banners = Banner.objects.filter(is_active=True)
#     context = {'active_banners': active_banners}
#     return render(
#         template_name='random/slot_mashine.html',
#         request=request,
#         context = context
#     )