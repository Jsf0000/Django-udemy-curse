from rest_framework import serializers
from .models import Movie, Ratings
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password')
        extra_kwargs = {'password': {'write_only': True, 'required': True}}

    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        # create token for user
        Token.objects.create(user=user)
        return user

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id', 'title', 'description', 'number_of_ratings', 'avg_rating')

class RatingSeriealizer(serializers.ModelSerializer):
    class Meta:
        model = Ratings
        fields = ('id', 'stars', 'user', 'movie')