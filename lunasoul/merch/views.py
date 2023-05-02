from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def shop(request):
    """
    Renders the 'shop.html' template if the user is logged in.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: A rendered HTTP response.

    """
    return render(request, 'shop.html')
