from django.shortcuts import render

# Create your views here.
def index(request):
    """
    Renders the 'index.html' template.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: A rendered HTTP response.

    """
    return render(request, 'index.html')
