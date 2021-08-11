from rest_framework import serializers
from .models import Article
# from .models import User


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'
        # fiels = ['id', 'title', 'author', 'email', 'date']


# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = '__all__'
