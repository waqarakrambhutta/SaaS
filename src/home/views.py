import pathlib
from django.http import HttpResponse

html_dir = pathlib.Path(__file__).resolve().parent

def home_page_view(request, *args, **kwargs):
    print(html_dir)
    html_ = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>Document</title>
    </head>
    <body>
        <h1>This is any<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Document</title>
  </head>
  <body>
    <h1>This is Anything!</h1>
  </body>
</html>
thing!</h1>
    </body>
    </html>

    """
    # html_file_path = html_dir / 'home.html'
    # html_= html_file_path.read_text() 
    return HttpResponse(html_)