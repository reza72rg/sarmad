from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView
from rest_framework.viewsets import ModelViewSet
from ...models import Student
from .serializers import UserSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .filters import PostFilters
# Create your views here.

@api_view(["GET"])
def get_users(request):
    if request.method == "GET":
        result = Student.objects.all()
        serializer = UserSerializer(result, many=True)
        return Response(serializer.data)
    return HttpResponse("ok")

@api_view(["GET"])
def get_age(request, pass_age):
    if request.method == "GET":
        result = Student.objects.filter(age=pass_age)
        serializer = UserSerializer(result, many=True)
        return Response(serializer.data)

@api_view(["GET"])
def get_age_username(request, pass_age, username):
    if request.method == "GET":
        result = Student.objects.filter(age=pass_age, username=username)
        serializer = UserSerializer(result, many=True)
        return Response(serializer.data)



class GetUsers(ListAPIView):
    serializer_class = UserSerializer
    queryset = Student.objects.all()


class GetUsersFilter(ListAPIView):
    serializer_class = UserSerializer
    queryset = Student.objects.filter()
    filter_backends = [DjangoFilterBackend]  # Enable filtering
    filterset_fields = ["age", "username"]
    #filter_backends = [SearchFilter]
    search_fields = ["username", "age"]




class PostModelViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = Student.objects.all()
    #filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    #search_fields = ["username", "age"]
    #ordering_fields = ["age"]
    #filterset_class = PostFilters
