from django.shortcuts import render

# Create your views here.
# CRUD : Create Read Update Delete


# 클래스형 뷰 / 함수형 뷰
# 웹 페이지에 접속한다. -> 페이지를 본다.
# URL 입력 -> 웹 서버가 뷰를 찾아서 동작시킨다. -> 응답

from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from .models import Bookmark


class BookmarkListView(ListView): # Generic View를 사용할 때 model을 설정해야함.

    model = Bookmark # list view의 html 찾는 파일 이름이 appname_list.html 인듯?


class BookmarkCreateView(CreateView):

    model = Bookmark
    fields = ['site_name','url']
    success_url = reverse_lazy('list')
    template_name_suffix = '_create' #template name을 설정을 안해주면 기본적으로 bookmark_form.html을 찾음


class BookmarkDeatailView(DetailView):

    model = Bookmark


class BookmarkUpdateView(UpdateView):

    model = Bookmark
    fields = ['site_name', 'url']
    template_name_suffix = '_update' #template name을 설정을 안해주면 기본적으로 bookmark_form.html을 찾음


class BookmarkDeleteView(DeleteView):
    model = Bookmark
    success_url = reverse_lazy('list')

    #fields = ['site_name', 'url']
    #template_name_suffix = '_delete'  # template name을 설정을 안해주면 기본적으로 bookmark_form.html을 찾음
