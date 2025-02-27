import pathlib
from django.http import HttpResponse
from django.shortcuts import render
from visits.models import PageVisit
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.conf import settings


html_dir = pathlib.Path(__file__).resolve().parent

LOGIN_URL = settings.LOGIN_URL

def home_view(request, *args, **kwargs):
    print(request.user.is_authenticated, request.user)
    return about_view(request, *args, **kwargs)

def about_view(request, *args, **kwargs):
    qs = PageVisit.objects.all()
    queryset = PageVisit.objects.filter(path = request.path)

    try:
        percent = (queryset.count() /qs.count()) * 100.00
    except: 
        percent = 0
        
    page_title = 'My page'
    my_content = {
        "title": page_title,
        "page_visit_count": qs.count(),
        "percent": percent,
        "total_visit_count": queryset.count(),
    }
    html_template = 'home.html'
    PageVisit.objects.create(path=request.path)
    return render(request, html_template, my_content )


def old_home_page_view(request, *args, **kwargs):

    page_title = 'My page'
    my_content = {
        "title": page_title,
    }
    html_ = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>Document</title>
    </head>
    <body>
        <h1>{title} anything</h1>
    </body>
    </html>
    """.format(**my_content)
    # html_file_path = html_dir / 'home.html'
    # html_= html_file_path.read_text() 
    return HttpResponse(html_)

VALID_CODE = 'abc123'

def pw_protected_view(request, *args, **kwargs):
    is_allowed = request.session.get('protected_page_allowed') or 0
    if request.method == 'POST':
        user_pw_code = request.POST.get('code') or None
        if user_pw_code == VALID_CODE:
            request.session['protected_page_allowed'] = 1
    if is_allowed:
        return render(request, 'protected/view.html', {})
    return render(request, 'protected/entry.html', {})

@login_required(login_url=LOGIN_URL)
def user_only_view(request, *args, **kwargs):
    return render(request, 'protected/user-only.html', {})


@staff_member_required(login_url=LOGIN_URL)
def staff_only_view(request, *args, **kwargs):
    return render(request, 'protected/user-only.html', {})
