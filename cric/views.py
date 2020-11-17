from django.shortcuts import render
from .forms import TeamForm
from .models import Team

# Create your views here.


def home(request):
    return render(request, 'main.html')


def match(request):
    form1 = TeamForm()
    form2 = TeamForm()
    context = {'form1': form1, 'form2': form2}
    return render(request, 'match.html', context)


def manage(request):
    if request.method == 'POST':
        form1 = TeamForm(request.POST)
        # form2 = TeamForm(request.POST['form2'])
        if form1.is_valid():  # and form2.is_valid():
            form1.save()
            # form2.save()
            team1 = Team.objects.get(team_name=form1.cleaned_data['team_name'])
            # team2 = Team.objects.get(name=form2.cleaned_data['team_name'])
            context = {'team1': team1}  # , 'team2': team2}

            return render(request, 'matchmanage.html', context)
