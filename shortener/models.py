from django.db import models

# 기존에 만들어진 테이블을 커스텀 하기 위해 사용 ( 컬럼추가 )
from django.contrib.auth.models import AbstractUser 
from django.contrib.auth.models import User as U
from django.conf import settings

# Create your models here.
class PayPlan(models.Model):
    name = models.CharField(max_length=20)
    price = models.IntegerField()
    update_at = models.DateTimeField(auto_now=True)
    create_at = models.DateTimeField(auto_now_add=True)

#AbstractUser : 변경됬는지 2개 같이 못씀 users, UserDetail --> 강의에선 같이 써도 된다했지만 충돌나는듯
# 해결방법 :https://stackoverflow.com/questions/67747391/field-defines-a-relation-with-the-model-auth-user-which-has-been-swapped-out 참고
# UserDetaild의 OneToOneField에 to 옵션에다가 settings.AUTH_USER_MODEL 경로를 정의해서 알려주니 오류 발생안함
class users(AbstractUser):
    pay_plan = models.ForeignKey(PayPlan, on_delete=models.DO_NOTHING) # AUTH_USER_MODEL = "shortener.Users" : settings.py 정의 필요


# class UserDetail(models.Model):
#     user = models.OneToOneField(to=settings.AUTH_USER_MODEL , on_delete=models.CASCADE)
#     pay_plan = models.ForeignKey(PayPlan, on_delete=models.DO_NOTHING)
 