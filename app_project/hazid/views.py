from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.db.models import Count


from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required, permission_required


from .forms import SurveyForm, LoginUserForm, RegisterUserForm
from .models import Survey

def index(request):
    surveys = Survey.objects.all()
    context = {
        "surveys": surveys[::-1],
    }
    return render(request, "hazid/index.html", context)

@login_required(login_url="/login")
def create_survey(request):
    if request.method == "POST":
        form = SurveyForm(request.POST)
        if form.is_valid():
            survey = form.save(commit=False)
            survey.author = request.user
            survey.save()
            return redirect(reverse("read_survey", args=(survey.id,)))
    else:
        form = SurveyForm()
    return render(request, "hazid/create_survey.html", {"form": form})


def read_survey(request, survey_id):
    survey = get_object_or_404(Survey, pk=survey_id)
    context = {
        "survey": survey,
    }
    return render(request, "hazid/detail.html", context)


def register(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = RegisterUserForm()
    return render(request, 'registration/register.html', {'form': form})


def custom_login(request):
    if request.method == 'POST':
        form = LoginUserForm(request, data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect("hazid:index")
    else:
        form = LoginUserForm()
    return render(request, "registration/login.html", {"form": form})

def stats(request):

    observed_counts = Survey.objects.values('i_observed').annotate(count=Count('i_observed'))

    context = {
        "observed_counts": observed_counts,
    }
    return render(request, "hazid/stats.html", context)


def winners(request):

    context = {

    }
    return render(request, "hazid/winners.html", context)

def qr(request):
        
    context = {

    }
    return render(request, "hazid/qr.html", context)