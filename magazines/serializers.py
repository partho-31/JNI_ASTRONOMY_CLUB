from rest_framework import serializers
from users.models import CustomUser
from django.db.models import Avg
from magazines.models import *



class ShortInfoUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'image', 'role']


class ReviewSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField('get_user')
    class Meta:
        model = Review
        fields = ['id','comment','rating','user']
        read_only_fields = ['id','user']

    def get_user(self,obj):
        if obj.user :
            return ShortInfoUserSerializer(obj.user).data
        return {
            'first_name': "AnonymousUser", 
            'last_name': " ", 
            'image': "image/upload/default_for_users_hpwnzn"
            }


class ArticleSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField('get_author')
    avg_rating = serializers.SerializerMethodField()
    magazine_title = serializers.SerializerMethodField()
    # reviews = ReviewSerializer(many=True, read_only=True)
    class Meta:
        model = Article
        fields = ['id','title','sub_title','cover_img','discription','summary','created_at','updated_at','author','avg_rating','heading_01','paragraph_01','heading_02','paragraph_02','heading_03','paragraph_03','quotes','quoter',"read_time",'magazine','magazine_title','status']
        read_only_fields = ['id','created_at','updated_at','author','reviews','avg_rating','magazine_title']

    def get_magazine_title(self,obj):
        return obj.magazine.title

    def get_author(self,obj):
        return ShortInfoUserSerializer(obj.author).data
    
    def get_avg_rating(self,obj):
        average = obj.reviews.aggregate(avg_rating = Avg('rating'))
        return average.get('avg_rating') if average is not None else 0
    

class MagazineSerializer(serializers.ModelSerializer):
    # articles = ArticleSerializer(many= True, read_only =True)
    class Meta:
        model = Magazine
        fields = ['id','title','sub_title','cover_img','discription','outcomes','summary','created_at','updated_at','user','read_time','status']
        read_only_fields = ['id','created_at','updated_at','articles','user']


 