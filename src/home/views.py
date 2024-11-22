import pathlib
from django.http import HttpResponse

html_dir = pathlib.Path(__file__).resolve().parent

def home_page_view(request, *args, **kwargs):
    print(html_dir)
    html_ = ""
    html_file_path = html_dir / 'home.html'
    html_= html_file_path.read_text() 
    return HttpResponse(html_)