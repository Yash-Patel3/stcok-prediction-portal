from django.urls import path
from acoounts import views as UserViews

urlpatterns =[
    path('register/',UserViews.RegisterView.as_view()),
]