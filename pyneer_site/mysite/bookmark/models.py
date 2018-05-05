from __future__ import unicode_literals # python 2.x 지원용.

from django.db import models
from django.utils.encoding import python_2_unicode_compatible # 마찬가지.

# Create your models here.

# Django에선 테이블을 하나의 클래스로 정의하고, 테이블의 컬럼은 클래스의 변수(속성)으로 매핑한다.
# 테이블 클래스는 django.db.models.Model 클래스를 상속받아 정의하고,
# 각 클래스 변수의 타입도 장고에서 미리 정의해 둔 필드 클래스를 사용한다.

@python_2_unicode_compatible
class Bookmark(models.Model):
    title = models.CharField(max_length = 100, blank = True, null = True) # 얇은 글씨로 표현됨.
    url = models.URLField('url', unique = True) # url컬럼에 대한 label문구. Field.verbose_name 즉, 필드의 별칭.
    # null=False, blank=False 이기 때문에 굵은 글씨로 표현됐다.

    def __str__(self): # 객체를 문자열로 표현하는 함수. 테이블 명 보여줄 때 이거 없으면 제대로 표현되지 않는다.
        return self.title

# 참고로, 애플리케이션 명을 bookamrk로 해도 Bookmark로 보여주고 테이블명은 Bookmarks로 해주는데
# 이는 장고가 자동으로 해주는 것.
# startapp appname --> appname 대문자화 시켜줌.
# 테이블명 복수화 시켜주고 대문자화 시킴.
# 객체명은 반대로 클래스 이름을 소문자와 공백으로 만듦.

