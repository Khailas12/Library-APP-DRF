from django.urls import path
from . import views


urlpatterns = [
    path('basic_login/', views.SuperuserLoginAPIView.as_view()),
    path('logout/', views.LogoutAPIView.as_view())
]