from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    mobile = models.CharField(max_length=10, unique=True, null=True, verbose_name='mobile')

    class Meta:
        db_table = 'tb_user'
        verbose_name = 'USERS'
        verbose_name_plural = verbose_name  # 复述形式
