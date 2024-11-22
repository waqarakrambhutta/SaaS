import pathlib
from django.http import HttpResponse
from django.shortcuts import render

html_dir = pathlib.Path(__file__).resolve().parent

def home_page_view(request, *args, **kwargs):

    page_title = 'My page'
    my_content = {
        "title": page_title,
    }
    html_template = 'home.html'
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
