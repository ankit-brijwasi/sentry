from django.http import HttpResponse, Http404
from sentry_sdk import capture_message
from .models import Post

def posts(request):
    post = Post.objects.get(id=1)
    return HttpResponse(posts.title)


def custom_404_error(request, exception):
    print(exception)
    capture_message("Page not found!", level="error")
    raise Http404("Oops! The resource was not found")