from django.urls import path, include
from .views import get_users, get_age, get_age_username, GetUsers, GetUsersFilter, PostModelViewSet
from rest_framework.routers import DefaultRouter

app_name = "api-v1"

router = DefaultRouter()
router.register("post", PostModelViewSet, basename="post")



urlpatterns = [
    #path("", get_users, name= "get_user"),
    #path("getuser/filter/", GetUsersFilter.as_view(), name= "get_user"),
    #path("<int:pass_age>/<str:username>", get_users, name= "get_user"),
]+router.urls