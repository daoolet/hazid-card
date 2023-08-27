from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views import View
from django.http import HttpResponseRedirect


from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required, permission_required


from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


from .forms import SurveyForm, LoginUserForm, RegisterUserForm
from .models import Survey


# @api_view(["GET"])
# def index(request):
#     surveys = Survey.objects.all()
#     serializer = SurveySerializer(surveys, many=True)
#     return Response(serializer.data)

# @api_view(["POST"])
# def create_survey(request):
#     serializer = SurveySerializer(data=request.data)
#     if serializer.is_valid():
#         survey = serializer.save()
#         return Response({
#             "detail": "Successful",
#             "survey_id": survey.id,
#         })
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(["GET"])
# def read_survey(request, survey_id):
#     survey = get_object_or_404(Survey, pk=survey_id)
#     serializer = SurveySerializer(survey)
#     return Response(serializer.data)

# @api_view(["GET"])
# def read_all_surveys(request):
#     pass

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

