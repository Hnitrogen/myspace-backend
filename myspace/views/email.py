from django.core.mail import EmailMessage
from django.shortcuts import render
from django.http import JsonResponse
from myspace.models.uploadfile import Document
from django.views.decorators.csrf import csrf_exempt

# def send_email(request):
#     return JsonResponse({'result': 'success'}) 
    # email = EmailMessage(
    #     '猪吧你', # 邮件主题
    #     '我和她这辈子没有可能了吗？', # 邮件正文
    #     '1791422575@qq.com', # 发件人
    #     ['3500085264@qq.com'], # 收件人列表
    # )
    # email.send()

@csrf_exempt
# def upload_file(request):
#     if request.method == 'POST':
#         document = Document(request.POST,request.FILES)
#         # name = document.title 
#         # file = document.file 
            
#         # doc = Document(title=name,file=file) 
#         # doc.save() 
#         return JsonResponse({'result': 'success'}) 


def upload_file(request):
    if request.method == 'POST':
        file = request.FILES['file']
        doc = Document.objects.create(title='tst2',file=file)
        doc.save()
        return JsonResponse({'result': 'success'})