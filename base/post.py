# -*- coding: utf-8 -*-
from django.http import HttpResponse

def list(request):
    return HttpResponse('你好,劳资测试一下就知道了')