from django.contrib import admin
from bookmark.models import Bookmark # Bookmark를 import해온다.

# Register your models here.

class BookmarkAdmin(admin.ModelAdmin): # Bookmark 클래스가 Admin사이터에서 어떤 모습으로 보여줄 지 정의하는 클래스.
    list_display = ('title', 'url')

admin.site.register(Bookmark, BookmarkAdmin)