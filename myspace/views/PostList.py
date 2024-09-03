from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from myspace.models.post import Post , PostComment
from myspace.serializers import PostSerializer , PostCommentSerializer , PostSimpleSerializer
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator 
from rest_framework.decorators import permission_classes
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from rest_framework import generics
from taggit.models import Tag
from collections import Counter

class PostPagination(PageNumberPagination):
    page_size = 5 
    max_page_size = 5
    page_size_query_param = 'page_size'


class PostList(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSimpleSerializer
    pagination_class = PostPagination
    
class PostDetail(APIView):    
    def get(self,request,pk):
        p = Post.objects.get(id=pk) 
        serializer = PostSerializer(p)
        return Response(serializer.data)

# 这个鉴权应该是可以合并的
class PostCommentAPI(APIView):
    def get(self,request,id): 
        # 返回两个以上的数据要用filter , get只能返回一个
        p = PostComment.objects.filter(attach_id = id)  
        serializer = PostCommentSerializer(p,many=True)
        return Response(serializer.data)
    
    # @method_decorator(permission_classes([IsAuthenticated]))
    # def post(self,request): 
    #     author = request.POST.get('author') 
    #     attach_id = request.POST.get('attach_id')
    #     content = request.POST.get('content')
    #     content_location  = request.POST.get('content_location')
    #     PostComment.objects.create(author=author,attach_id=attach_id,content=content,content_location=content_location)
    #     return JsonResponse({'result':'post_success'})



class SendPostComment(APIView):
    permission_classes = ([IsAuthenticated])
    def post(self,request): 
        author = request.POST.get('author') 
        attach_id = request.POST.get('attach_id')
        content = request.POST.get('content')
        content_location  = request.POST.get('content_location')
        PostComment.objects.create(author=author,attach_id=attach_id,content=content,content_location=content_location)
        return JsonResponse({'result':'post_success'})

@api_view(['GET'])
def getPostCategory(request): 
    tags = [i.__str__() for i in Tag.objects.all()]
    hashed = Counter(tags)
    return Response(hashed)


@api_view(['GET'])
def search_by_tag(request): 
    tag = request.GET.get('tag','')
    filter_list = []
    
    for post in Post.objects.all(): 
        tags = post.tags.all()
        tag_list = [str(x) for x in tags]
        if tag in tag_list: 
            filter_list.append(post.id)
            continue 
    res = Post.objects.filter(id__in=filter_list)
    return Response(PostSerializer(res,many=True).data)