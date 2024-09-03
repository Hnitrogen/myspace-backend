from rest_framework import serializers
from django.utils import timezone

from .models.CatImage import CatImage
from .models.post import Post , PostComment
from .models.Hack import HackerImage
from .models.todo import TodoList
from .models.tutorial.project import Project
from .models.paste import Paste
from .models.Timer import Timer , Answer
from django.contrib.auth.models import User
from taggit.models import Tag
from taggit.serializers import (TagListSerializerField,
                                TaggitSerializer)
# 将model序列化为Json传输
class TodoListSerializer(serializers.ModelSerializer):
    createtime = serializers.SerializerMethodField()

    class Meta:
        model = TodoList 
        fields = '__all__'


    def get_createtime(self, obj):
        # 获取原始的创建时间
        original_time = obj.createtime
        # 添加时区偏移量，这里假设是 UTC+8
        offset_8 = original_time + timezone.timedelta(hours=8)
        # 返回格式化后的时间
        return offset_8.strftime('%Y-%m-%d %H:%M:%S')

class CatImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CatImage
        fields = '__all__'

class PostSimpleSerializer(TaggitSerializer,serializers.ModelSerializer):
    tags = TagListSerializerField()
    class Meta:
        model = Post
        fields = ['id','title','tags','createtime','pic_url']

class PostSerializer(TaggitSerializer,serializers.ModelSerializer):
    tags = TagListSerializerField()
    class Meta:
        model = Post
        fields = '__all__'

class HackSerializer(serializers.ModelSerializer):
    class Meta:
        model = HackerImage 
        fields = '__all__'

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project 
        fields = '__all__'

class PasteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paste
        fields = '__all__'

class TimerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Timer 
        fields = '__all__' 

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__' 
 
class UserSerializer(serializers.ModelSerializer):
    class Meta: 
        model = User
        fields = ['id','username']


class PostCommentSerializer(serializers.ModelSerializer):
    class Meta: 
        model = PostComment
        fields = '__all__'