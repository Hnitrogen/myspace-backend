import subprocess
import time 

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt    # 取消安全规则
def compile(request):
    if request.method == 'POST':
        # request.POST.get 这是从表单中获取数据 , 不是从请求中获取Json
        code = request.POST.get('code', '')
        input_data = request.POST.get('input_data','')
        print("compile is on")
        with open('input.txt', 'w') as f:
            f.write(input_data)
        with open('source.cpp', 'w') as f:
            f.write(code) 

        proc = subprocess.run(['g++', '-o', 'program', '-x', 'c++', '-'], input=code.encode(), capture_output=True)
        if proc.returncode != 0:
            return JsonResponse({'error': proc.stderr.decode()})

        # 运行编译后的程序并传递输入数据
        start_time = time.time 
        try: 
            proc = subprocess.run(['./program'], input=input_data.encode(), capture_output=True,timeout=3)
            print("start")
        except subprocess.TimeoutExpired:   # 超时退出
            print("TLE")
            return JsonResponse({'error': 'Timeout in 3s'})
        except subprocess.CalledProcessError:   # 执行出错
            print("ERR")
            return JsonResponse({'error': proc.stderr.decode()})
        else:   # 以上异常不出现
            print("FIN")
            return JsonResponse({'output': proc.stdout.decode()})
           
    else:
        return JsonResponse({'error': 'Invalid request method'})



        #     if proc.returncode == 1:
        #         return JsonResponse({'error': proc.stderr.decode()})
        #     # 返回程序的输出结果

        # except TimeoutExpired:
        #     proc.kill() 
        #     return JsonResponse({'error': 'TLE'})