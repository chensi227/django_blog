# -*- coding: utf-8 -*-
from django.shortcuts import render
from .models import Category, Tag, Article
from django.db.models import Q
from django.forms.models import model_to_dict
from django.http import HttpResponse,HttpResponsePermanentRedirect
import json
import time
from datetime import datetime
import re
# Create your views here.

def index(request):
    return render(request, 'index.html')

def info(request):
    return render(request, 'info.html')

def login(request):
    return render(request, 'login.html')

'''
分类相相关
'''
# 文章分类列表
def category_list(request):
    list = Category.objects.all()
    return render(request,'category_list.html',{'list':list})

# 添加分类
def category_add(request):
    if request.method == 'POST':
        # 验证数据写入数据库
        categorys = Category()
        categorys.name = request.POST['name']
        categorys.title = request.POST['title']
        categorys.details = request.POST['details']
        categorys.order = request.POST['order']
        categorys.pid = request.POST['pid']
        # categorys.addtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        categorys.addtime = datetime.now()
        categorys.save()
        if(categorys.id > 0):
            return HttpResponsePermanentRedirect('/base/category_list/')
        else:
            return render(request, 'category_add.html', {'error':'添加文章分类失败'})
    else:
        list = Category.objects.filter(pid = 0)
        return render(request, 'category_add.html',{'list':list})

# 删除分类
def category_delete(request,id):
    result = Category.objects.filter(id = id).delete()
    '''
    categroy = Categroy.objects.get(pk = id)
    category.delete()
    '''
    if result[1]:
        #删除成功
        return HttpResponse(json.dumps({'status':0, 'msg':'删除成功'}),content_type='application/json')
    else:
        #失败
        return HttpResponse(json.dumps({'status':1, 'msg':'删除失败'}),content_type='application/json')

# 修改分类
def category_edit(request,id):
    if request.method == 'POST':
        # 更改数据库
        id = request.POST['id']
        categorys = Category.objects.get(pk = id)
        categorys.name = request.POST['name']
        categorys.title = request.POST['title']
        categorys.details = request.POST['details']
        categorys.order = request.POST['order']
        categorys.pid = request.POST['pid']
        categorys.addtime = datetime.now()
        categorys.save()
        if (categorys.id > 0):
            return HttpResponsePermanentRedirect('/base/category_list/')
        else:
            return render(request, 'category_add.html', {'error': '修改文章分类失败'})
    else:
        list = Category.objects.get(pk = id)
        data = Category.objects.filter(pid=0).filter(~Q(id = id))
        return render(request,'category_edit.html',{'list':list,'info':data})


'''
******************************************************************************************************************
'''

'''
tag标签相关
'''
# 标签列表
def tag_list(request):
    list = Tag.objects.all()
    return render(request,'tag_list.html',{'list':list})
# 修改标签
def tag_edit(request,id):
    if request.method == 'POST':
        id = request.POST['id']
        tag = Tag.objects.get(pk = id)
        tag.name = request.POST['name']
        tag.save()
        return HttpResponsePermanentRedirect('/base/tag_list/')
    else:
        list = Tag.objects.get(pk = id)
        return render(request,'tag_edit.html',{'list':list})
# 添加标签
def tag_add(request):
    if request.method == 'POST':
        tag = Tag()
        tag.name = request.POST['name']
        tag.addtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        tag.save()
        id = tag.id
        if id > 0 :
            return HttpResponsePermanentRedirect('/base/tag_list/')
        else:
            return render(request, 'tag_add.html', {'error': '添加标签失败'})
    else:
        return render(request, 'tag_add.html')
# 删除标签
def tag_delete(request,id):
    tag = Tag.objects.get(pk = id)
    result = tag.delete()
    if result[1]:
        #删除成功
        return HttpResponse(json.dumps({'status':0, 'msg':'删除成功'}),content_type='application/json')
    else:
        #失败
        return HttpResponse(json.dumps({'status':1, 'msg':'删除失败'}),content_type='application/json')

'''
**************************************************************************************************************
'''

'''
文章模块
'''
# 文章列表
def article_list(request):
    list = Article.objects.all()
    # info = dict(data)
    # list = model_to_dict(data)
    for v in list:
        # category = Category.objects.raw('SELECT name AS category FROM base_category WHERE id = %d LIMIT 1',[v.categoryid])

        # category = Category.objects.values('name').filter(id = v.categoryid).first()
        # v.category = category['name']

        category = Category.objects.only('name').get(id = v.categoryid)
        # category = Category.objects.only('name').filter(id = v.categoryid).first()
        # category = Category.objects.only('name').filter(id=v.categoryid)[0]
        v.category = category

        tag = v.tag
        tag = tag.split(',')
        name = ''
        for m in tag:
            name += '  '+str(Tag.objects.only('name').get(id= int(m)))

        v.tagname = name
        # list({d['city'] for d in ds})
        # tagname = Tag.objects.raw('SELECT id,group_concat(name) AS tagname FROM base_tag WHERE id in (%s) LIMIT 1', [v.tag])[0]
        # tagname = Tag.objects.only('group_concat(name) AS tagname').extra(where=["id IN ('v.tag')"])
        # v.tagname = tagname.tagname
    return render(request,'article_list.html',{'list':list})


# 添加文章
def article_add(request):
    if request.method == 'POST':
        # tag = request.POST.getlist('tag')
        # return HttpResponse(json.dumps(tag))
        # data = request.POST
        # return HttpResponse(json.dumps(data))
        # 获取数据
        article = Article()
        article.title = request.POST['title']
        article.author = request.POST['author']
        article.addtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        article.description = request.POST['description']
        article.content = request.POST['content']
        article.categoryid = request.POST['categoryid']
        tagid = request.POST.getlist('tag')
        article.tag = ','.join(tagid)
        article.save()
        if article.id > 0 :
            return HttpResponsePermanentRedirect('/base/article_list/')
        else:
            return render(request, 'article_add.html', {'error': '添加文章失败'})
    else:
        # 取出所有的标签
        tags = Tag.objects.all()
        # 取出所有的分类
        categorys = Category.objects.all()
        return render(request,'      .html',{'tags':tags,'categorys':categorys})

# 修改文章
def article_edit(request,id):
    if request.method == 'POST':
        id = request.POST['id']
        article = Article.objects.get(pk = id)
        article.title = request.POST['title']
        article.author = request.POST['author']
        article.addtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        article.description = request.POST['description']
        article.content = request.POST['content']
        article.categoryid = request.POST['categoryid']
        tagid = request.POST.getlist('tag')
        article.tag = ','.join(tagid)
        article.save()
        id = article.id
        if id > 0 :
            return HttpResponsePermanentRedirect('/base/article_list/')
        else:
            return render(request, 'article_edit.html', {'error': '添加文章失败'})
    else:
        list = Article.objects.get(pk=id)

        list.tag = list.tag.split(',')
        list.tag = [ int(i) for i in list.tag ]
        # 取出所有的标签
        tags = Tag.objects.all()
        # 取出所有的分类
        categorys = Category.objects.all()
        return render(request, 'article_edit.html', {'list':list,'tags':tags,'categorys':categorys})

#  删除文章
def article_delete(request,id):
    article = Article.objects.get(pk=id)
    result = article.delete()
    if result[1]:
        # 删除成功
        return HttpResponse(json.dumps({'status': 0, 'msg': '删除成功'}), content_type='application/json')
    else:
        # 失败
        return HttpResponse(json.dumps({'status': 1, 'msg': '删除失败'}), content_type='application/json')
