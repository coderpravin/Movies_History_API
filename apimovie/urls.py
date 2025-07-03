
from django.urls import path
from .views import movieView, movieCreateView, MovieListMixinsView, MovieDetailMixinsView

urlpatterns = [
    path('movieApi', movieView.as_view()),
    path('movieApi/<int:pk>', movieCreateView.as_view()),

    #class - mixins

    path('movieMixins', MovieListMixinsView.as_view()),
    path('movieMixins/<int:pk>', MovieDetailMixinsView.as_view()),

]
