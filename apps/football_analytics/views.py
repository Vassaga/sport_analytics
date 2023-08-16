

""" FOOTBALL VIEWS """


from django.shortcuts import render
from .models import Match

def matches_list(request):
    matches = Match.actual.all()
    context = {'matches': matches}
    return render(
        template_name='MatchList.html', 
        request=request, 
        context = context
        )