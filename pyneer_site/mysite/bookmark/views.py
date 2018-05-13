from django.shortcuts import render

from django.views.generic import ListView, DetailView # 제네릭 뷰를 위해 임포트
from bookmark.models import Bookmark # 테이블 조회를 위해 모델 클레스 임포트

# Create your views here.

class BookmarkLV(ListView):
    model = Bookmark

class BookmarkDV(DetailView):
    model = Bookmark


