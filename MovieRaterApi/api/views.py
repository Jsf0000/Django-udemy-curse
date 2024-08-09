from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Movie, Ratings
from .serializers import MovieSerializer, RatingSeriealizer, UserSerializer
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    # Add Token Authentication
    authentication_classes = (TokenAuthentication,)
    # permissions
    permission_classes = (IsAuthenticated,)

    # detail movie = True, all movies detail = False
    # optional that pk parameters will be optional with pk=None
    @action(detail=True, methods=['POST'])
    def rate_movie(self, request, pk=None):
        if 'stars' in request.data:

            movie = Movie.objects.get(id=pk)
            stars = request.data['stars']
            user = request.user
            print('movie title', movie.title, stars, 'Username', user.username)

            try:
                rating = Ratings.objects.get(user=user.id, movie=movie.id)
                rating.stars = stars
                rating.save()
                serializer = RatingSeriealizer(rating, many=False)
                response = {'message': 'Rating Updated', 'result': serializer.data}
            except:
                rating = Ratings.objects.create(user=user, movie=movie, stars=stars)
                serializer = RatingSeriealizer(rating, many=False)
                response = {'message': 'Rating Created', 'result': serializer.data}
            return Response(response, status=status.HTTP_200_OK)

        else:
            response = {'message': 'You need to provide starts'}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)


class RatingsViewSet(viewsets.ModelViewSet):
    queryset = Ratings.objects.all()
    serializer_class = RatingSeriealizer
    # Add token authentication
    authentication_classes = (TokenAuthentication,)
    # permissions
    permission_classes = (IsAuthenticated,)

    # restrict updated and created method #interview
    def update(self, request, *args, **kwargs):
        response = {'message': "You can't updated rating like that."}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)

    def create(self, request, *args, **kwargs):
        response = {'message': "You can't create rating like that."}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)
