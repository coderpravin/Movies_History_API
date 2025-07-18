from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView, status
from .serializers import MovieSerializer
from movie.models import Movie
from rest_framework import mixins, generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters




# Create your views here.
class movieView(APIView):
    def get(self,request):
        movies = Movie.objects.all()
        serilalizer = MovieSerializer(movies, many=True)
        return Response(serilalizer.data,status=status.HTTP_200_OK)
        
    def post(self, request):
        serilalizer = MovieSerializer(data=request.data)
        if serilalizer.is_valid():
            serilalizer.save()
            return Response(serilalizer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serilalizer.errors, status=status.HTTP_400_BAD_REQUEST)


class movieCreateView(APIView):
    def get(self,request,pk):
        try:
            movie = Movie.objects.get(pk=pk)
        except Movie.DoesNotExist():
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serilalizer = MovieSerializer(movie)
        return Response(serilalizer.data)
        
    def put(self, request, pk):
        movie = Movie.objects.get(pk=pk)
        serilalizer = MovieSerializer(movie, data=request.data)
        if serilalizer.is_valid():
            serilalizer.save()
            return Response(serilalizer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serilalizer.data, status=status.HTTP_404_NOT_FOUND)
        

    def patch(Self,request,pk):
        movie = Movie.objects.get(pk=pk)
        serilalizer = MovieSerializer(movie, data=request.data, partial=True)
        if serilalizer.is_valid():
            serilalizer.save()
            return Response(serilalizer.data, status=status.HTTP_200_OK)
        
        else:
            return Response(serilalizer.errors, status=status.HTTP_404_NOT_FOUND)
        
    def delete(self,reques,pk):
        movie = Movie.objects.get(pk=pk)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


#using Mixins
class MovieListMixinsView(mixins.ListModelMixin,mixins.CreateModelMixin, generics.GenericAPIView):
    serializer_class = MovieSerializer
    queryset = Movie.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['movie_actor']

    def get(self,request):
        return self.list(request)
    
    def post(self,request):
        return self.create(request)
    
class MovieDetailMixinsView(mixins.RetrieveModelMixin, mixins.UpdateModelMixin,mixins.DestroyModelMixin,  generics.GenericAPIView):
    serializer_class = MovieSerializer
    queryset = Movie.objects.all()

    def get(self,request,pk):
        return self.retrieve(request, pk)
    
    def put(self, request, pk):
        return self.update(request, pk)
    
    def delete(self,request,pk):
        return self.delete(request, pk)
    






        