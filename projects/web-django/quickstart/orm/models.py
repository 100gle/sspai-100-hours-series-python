from django.db import models


class User(models.Model):

    gender_choices = [
        (0, "女"),
        (1, "男"),
    ]

    id = models.AutoField(
        primary_key=True,
        verbose_name="用户ID",
    )
    name = models.CharField(
        max_length=10,
        verbose_name="用户名",
    )
    age = models.IntegerField(verbose_name="年龄")
    gender = models.BooleanField(
        choices=gender_choices,
        blank=True,
        default="",
        verbose_name="性别",
    )
    email = models.EmailField(max_length=50, verbose_name="邮箱")
    telephone = models.CharField(
        max_length=11,
        blank=True,
        verbose_name="联系电话",
    )
    register_at = models.DateTimeField(auto_now_add=True, verbose_name="注册时间")

    def __repr__(self):
        return f"User<id:{self.id}, name:{self.name}>"
