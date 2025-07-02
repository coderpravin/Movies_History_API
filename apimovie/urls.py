
from django.urls import path
from .views import movieView, movieCreateView

urlpatterns = [
    path('movieApi', movieView.as_view()),
    path('movieApi/<int:pk>', movieCreateView.as_view()),
]
