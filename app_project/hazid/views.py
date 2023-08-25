from django.shortcuts import get_object_or_404


from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


from .models import Survey
from .serializers import SurveySerializer


# Create your views here.

@api_view(["GET"])
def index(request):
    surveys = Survey.objects.all()
    serializer = SurveySerializer(surveys, many=True)
    return Response(serializer.data)

@api_view(["POST"])
def create_hazid(request):
    serializer = SurveySerializer(data=request.data)
    if serializer.is_valid():
        survey = serializer.save()
        return Response({
            "detail": "Successful",
            "survey_id": survey.id,
        })
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET"])
def read_hazid(request, survey_id):
    survey = get_object_or_404(Survey, pk=survey_id)
    serializer = SurveySerializer(survey)
    return Response(serializer.data)