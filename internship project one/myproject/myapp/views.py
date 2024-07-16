# myapp/views.py
from django.http import HttpResponse

def home(request):
    html = """
    <h1>Home Page</h1>
    <p>Welcome to the Home Page.</p>
    <a href="/page1/">Go to Page 1</a><br>
    <a href="/page2/">Go to Page 2</a>
    """
    return HttpResponse(html)

def page1(request):
    html = """
    <h1>Page 1</h1>
    <p>Welcome to Page 1.</p>
    <a href="/">Go back to Home</a><br>
    <a href="/page2/">Go to Page 2</a>
    """
    return HttpResponse(html)

def page2(request):
    html = """
    <h1>Page 2</h1>
    <p>Welcome to Page 2.</p>
    <a href="/">Go back to Home</a><br>
    <a href="/page1/">Go to Page 1</a>
    """
    return HttpResponse(html)
