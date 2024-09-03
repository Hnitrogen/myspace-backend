import requests
from django.http import JsonResponse , HttpResponse

def submit_problem(request):
    # 构造JSON数据
    data = {
        "cmd": [{
            "args": ["/usr/bin/g++", "a.cc", "-o", "a"],
            "env": ["PATH=/usr/bin:/bin"],
            "files": [{
                "content": ""
            }, {
                "name": "stdout",
                "max": 10240
            }, {
                "name": "stderr",
                "max": 10240
            }],
            "cpuLimit": 10000000000,
            "memoryLimit": 104857600,
            "procLimit": 50,
            "copyIn": {
                "a.cc": {
                    "content": "#include <iostream>\nusing namespace std;\nint main() {\nint a, b;\ncin >> a >> b;\ncout << a + b << endl;\n}"
                }
            },
            "copyOut": ["stdout", "stderr"],
            "copyOutCached": ["a.cc", "a"],
            "copyOutDir": "1"
        }]
    }

    # 发送HTTP POST请求
    response = requests.post('http://jiwaicat.top:5050/run', json=data)

    # 获取判题结果
    result = response.json()

    # 返回JSON响应
    print("Active in SubmitCode!!!!")
    # return JsonResponse(result)
    # return JsonResponse({'result':'success'})
    return HttpResponse(result)