# # 파이썬 2.x를 위한 것.
# from __future__ import unicode_literals
# from django.utils.encoding import python_2_unicode_compatible

from django.db import models

# from django.core.urlresolvers import reverse

# Create your models here.

class Post(models.Model):
    title = models.CharField('TITLE', max_length=50)
    slug = models.SlugField('SLUG', unique=True, allow_unicode=True, help_text= 'one word for title alias')
    description = models.CharField('DESCRIPTION', max_length=100, blank=True, help_text='simple description text.')
    content = models.TextField('CONTENT')
    create_date = models.DateTimeField('Create Date', auto_now_add= True)
    modify_date = models.DateTimeField('Modify Date', auto_now=True)

    class Meta: # 필드 속성 외에 필요한 파라미터는 내부 클래스 Meta로 정의.
        verbose_name = 'post' # verbose = 별칭.
        verbose_name_plural = 'posts'
        db_table = 'my_post' # 생략해도 됨. 생략하면 앱명_모델클래스명, 즉 blog_post가 됨.
        ordering = ('-modify_date',) # modify_date 기준으로 내림차순 정렬.

    def __str__(self):
        return self.title

    # 아래의 모델 클래스 메소드들은 이따가 다시 설명.
    def get_absolute_url(self):
        return reverse('blog:post_detail', args =(self.slug,))

    def get_previous_post(self):
        return self.get_previous_by_modify_date()

    def get_next_post(self):
        return self.get_next_by_modify_date()



