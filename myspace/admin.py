from django.contrib import admin

# Register your models here.
from myspace.models.CatImage import CatImage 
from myspace.models.post import Post , PostComment
from myspace.models.Hack import HackerImage
from myspace.models.uploadfile import Document
from myspace.models.todo import TodoList
from myspace.models.tutorial.project import Project 
from myspace.models.paste import Paste
from myspace.models.Timer import Timer , Answer

admin.site.register(CatImage)
admin.site.register(HackerImage)
admin.site.register(Post)
admin.site.register(PostComment)
admin.site.register(Document)
admin.site.register(TodoList)
admin.site.register(Project)
admin.site.register(Paste)
admin.site.register(Timer)
admin.site.register(Answer)