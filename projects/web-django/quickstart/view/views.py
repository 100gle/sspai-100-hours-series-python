from django.http import HttpResponse, HttpResponseNotAllowed
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def index(request):
    """index page"""

    method = request.method

    if method == "GET":
        return HttpResponseNotAllowed(["POST"])
    elif method == "POST":
        return HttpResponse(f"You has got this page by POST method.")


@method_decorator(csrf_exempt, name="dispatch")
class IndexView(View):

    template = """\
    <p>You has got this page by {method} method, the following steps are: <br />
    {content}
    </p>
    """

    def get(self, request):
        """index page"""

        steps = [
            "1. handle GET request",
            "2. log request and other info",
            "3. query something from database",
        ]
        response = self.template.format(
            method="GET",
            content=r"<br />".join(steps),
        )

        return HttpResponse(response)

    def post(self, request):

        steps = [
            "1. handle POST request",
            "2. log request and other info",
            "3. get form or parameters from request",
            "4. parse form or parameters",
            "5. query something from database",
            "6. return response",
        ]

        response = self.template.format(
            method="POST",
            content=r"<br />".join(steps),
        )

        return HttpResponse(response)
