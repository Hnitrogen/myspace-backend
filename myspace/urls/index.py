from django.urls import path, re_path
from django.conf.urls import url
from django.views.static import serve 
from mysite.settings import MEDIA_ROOT
from rest_framework.urlpatterns import format_suffix_patterns

from myspace.views.CatImageList import CatImageList , CatImageRandom
from myspace.views.PostList import (PostList , 
PostDetail , PostCommentAPI , SendPostComment , getPostCategory , search_by_tag)

from myspace.views.HackList import HackerDetail , HackerAll 
from myspace.views.index import index 
from myspace.views.compile import compile 
from myspace.views.email import upload_file 
from myspace.views.todoCmd import todoDelete , todoPost
from myspace.views.Getproject import ProjectList 
from myspace.views.pastebin import PasteList , PasteDetail 
from myspace.views.getAnswer import getAnswer , setTimer , getTimeStamp
from myspace.views.UserViewSet import UserList
from myspace.views.remote_desktop import turn_on

# oj 
from myspace.views.oj import submit_problem 

urlpatterns = [
    path('remote/',turn_on),
    path('submitcode/',submit_problem),
    
    path('getUser/<int:user_id>/',UserList.as_view()),
    path('getpictures/',CatImageList.as_view()),
    path('random/<int:pk>/',CatImageRandom.as_view()),
    path('post/',PostList.as_view()),
    path('post/<int:pk>/',PostDetail.as_view()),
    path('postComment/<int:id>/',PostCommentAPI.as_view()),
    path('postComment/',PostCommentAPI.as_view()),
    path('sendpostComment/',SendPostComment.as_view()),
    path('getBlogCategory/',getPostCategory),
    path('search_by_tag/',search_by_tag),
    path('hacker/<int:pk>/',HackerDetail.as_view()),
    path('hacker/list/',HackerAll.as_view()),
    path('compile/',compile,name='compile'),
    path('send/',upload_file),

    # path('todo/',TodoViewSet.as_view()),
    # path('addtodo/',todoPost),
    # path('hhh/',todoDelete),
    # path('todo/simple/',TodoViewSet.get_simple_todo,name='TodoViewSet.get_simple_todo'),


    path('tutorial/',ProjectList.as_view()),
    path('pastebin/',PasteList.as_view()), 
    path('pastebin/<int:pk>/', PasteDetail.as_view()),
    path('getAnswer/',getAnswer.as_view()),
    path('getTimeStamp/',getTimeStamp.as_view()),
    path('setTimer/',setTimer),

    url(r'^upload/(?P<path>.*)$',serve,{"document_root": MEDIA_ROOT}),
    # re_path(r".*", index, name="myspace_index"),  # 这玩意覆盖drf 的路由了
    
]

# 使用routers
from rest_framework import routers
from myspace.views.todoList import TodoViewSet 

router = routers.SimpleRouter()
router.register(r'todos',TodoViewSet)


# urlpatterns = format_suffix_patterns(urlpatterns)
urlpatterns += router.urls

# from pprint import pprint 
# pprint(urlpatterns)