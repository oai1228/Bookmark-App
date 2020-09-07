from django.urls import path
from .views import *

urlpatterns = [

    path("",BookmarkListView.as_view(), name='list'), # 아무것도 없는 거에 매칭
    path("add/",BookmarkCreateView.as_view(),name='add'),
    path("detail/<int:pk>/",BookmarkDeatailView.as_view(),name='detail'), #슬러거도 사용가능
    path("update/<int:pk>/",BookmarkUpdateView.as_view(),name='update'),
    path("delete/<int:pk>/",BookmarkDeleteView.as_view(),name='delete'),    # as_view() 클래스형 뷰를 함수형 뷰로 바꿔줌.
    # name = url패턴의 이름.
]