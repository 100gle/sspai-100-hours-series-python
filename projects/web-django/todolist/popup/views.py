from django.http.response import HttpResponseNotAllowed
from django.shortcuts import redirect, render
from django.utils.html import format_html

from .models import Group, Task


def index(request):

    welcome = "欢迎来到 Todolist 练习项目 Popup 应用主页！"

    index_content = format_html(
        """
    这是<a href="https://sspai.com/series/271" style="text-decoration: none;">《100 小时后请叫我程序员》</a>课程用于进行 Django 实践练习的网站，主要包括了以下几部分：
    <ul>
        <li><b>少数派 Logo</b>：你可以点击跳转至少数派首页；</li>
        <li><b>Home</b>：即当前页面；</li>
        <li><b>Task</b>：用于实践的待办清单页面，你可以在里面创建、更新以及删除任务；</li>
        <li><b>About</b>：对个人或网站信息进行简要说明的介绍页。</li>
    </ul>
    """
    )

    ctx = dict(
        title="home",
        welcome=welcome,
        index_content=index_content,
    )

    return render(request, "index.html", context=ctx)


def about(request):
    title = "About"
    header = f"{title} Me"
    about_content = """
    这是一段简单的，About Me 页面。
    它可以用来展示关于个人的一些信息，或者是简单的介绍。

    例如：
    """.strip().splitlines()
    items = [
        ("昵称", "100gle"),
        ("职业", "少数派作者"),
        ("编程语言", "Python、Golang、JavaScript 等等"),
    ]

    ctx = dict(
        title=title,
        header=header,
        about_content=about_content,
        items=items,
    )
    return render(request, "about.html", context=ctx)


def query_all_tasks(request):
    tasks = Task.objects.all()
    fields = ["序号", "任务名称", "优先级", "任务描述", "是否完成", "分组"]

    if Group.objects.count() == 0:
        groups = [
            Group(name="收集箱"),
            Group(name="生活"),
            Group(name="工作"),
        ]

        Group.objects.bulk_create(groups)

    groups = Group.objects.all()

    ctx = dict(
        title="Task",
        tasks=tasks,
        fields=fields,
        groups=groups,
    )
    return render(request, "tasks.html", context=ctx)


def create_task(request):
    """create a task"""
    if request.method == "POST":
        name = request.POST.get("taskName")
        priority = request.POST.get("taskPriority")
        description = request.POST.get("taskDescription")
        group_id = request.POST.get("taskGroup")
        group = Group.objects.get(id=group_id)

        Task.objects.create(
            name=name, priority=priority, description=description, group=group
        )
        return redirect("/tasks/")
    else:
        return HttpResponseNotAllowed(["POST"])


def update_task(request, task_id):
    """update a task"""
    task = Task.objects.get(id=task_id)
    task.is_done = False if task.is_done else True

    task.save()
    return redirect("/tasks/")


def delete_task(request, task_id):
    """delete a task"""
    task = Task.objects.get(id=task_id)

    task.delete()
    return redirect("/tasks/")
