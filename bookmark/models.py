from django.db import models
from django.urls import reverse
# Create your models here.

# 모델형식의 클래스를 생성해서 만듬.
# 모델 : 데이터베이스를 SQL없이 다루기 위해 사용
# 데이터를 객체화해서 다룸.
# 모델 = 테이블
# 모델 필드 = 테이블의 컬럼
# 인스턴스 = 테이블의 레코드

# 필드의 값(인스턴스) = 레코드의 컬럼 데이터값

class Bookmark(models.Model):
    # 필드 데이터 명시
    site_name = models.CharField(max_length=100)
    url = models.URLField('Site URL') # URL 필드 사용시 admin에서 자동으로 링크를 걸어줌

    def __str__(self):
        return f"이름 : {self.site_name} ,주소 ; {self.url}"
    # 필드의 종류가 결정하는 것
    # 1. 데이터베이스의 컬럼 종류
    # 2. 제약 사항(글자 수)
    # 3. Form의 종류
    # 4. Form에서 제약사항


    def get_absolute_url(self):
        return reverse('detail', args=[str(self.id)])

# 모델을 만들었다 -> 데이터베이스에 어떤 데이터를 어떤 형태로 넣을지 결정
# migrate -> 데이터베이스에 모델의 내용을 반영(테이블 생성)
# makemigrations -> 모델의 변경사항을 추적해서 기록




