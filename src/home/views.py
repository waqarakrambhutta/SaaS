from django.http import HttpResponse


def home_page_view(request, *args, **kwargs):
    return HttpResponse("<h2>Hello World!</h2>")