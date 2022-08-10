from django.db import models


class Task(models.Model):
    """the task record in todolist"""

    priority_choices = (
        (0, "一般"),
        (1, "优先"),
        (3, "紧急"),
    )

    is_done_choices = (
        (False, "未完成"),
        (True, "已完成"),
    )

    name = models.CharField(max_length=100, verbose_name="任务名称")
    priority = models.IntegerField(
        choices=priority_choices, default=0, verbose_name="任务优先级"
    )
    description = models.TextField(
        max_length=500, verbose_name="任务描述", blank=True, null=True
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="更新时间")
    is_done = models.BooleanField(
        default=False, verbose_name="是否完成", choices=is_done_choices
    )
    group = models.ForeignKey(
        "Group", on_delete=models.DO_NOTHING, default=0, verbose_name="所属分类"
    )

    def __repr__(self):
        return f"<Task {self.name}>"


class Group(models.Model):
    name = models.CharField(
        max_length=100,
        default="收集箱",
        unique=True,
        verbose_name="分类名称",
    )

    def __repr__(self):
        return f"<Group '{self.name}'>"
