from django.contrib import admin
from blog.models import Post # post에 대한 admin을 만드는거니까.

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'modify_date')
    list_filter = ('modify_date',)
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Post, PostAdmin)
