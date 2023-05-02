from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User


def register(request):
    """
    Registers a new user account and logs them in.

    If the request method is POST, the function retrieves the username, password,
    and first name from the request data and uses them to create a new User object.
    The user is then authenticated and logged in before being redirected to the 'shop'
    page. If the request method is GET, the function renders the 'register.html' template.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: A rendered HTTP response if the request method is GET, or a
        redirect response to the 'shop' page if the request method is POST and the
        registration was successful.

    """
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        first_name = request.POST['first_name']

        # Create a new user object
        user = User.objects.create_user(username=username, password=password)
        user.first_name = first_name
        user.save()

        # Authenticate and login the user
        user = authenticate(username=username, password=password)
        login(request, user)

        return redirect('merch:shop')

    return render(request, 'registration/register.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # Authenticate the user
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('merch:shop')
        else:
            # Handle invalid login credentials
            return render(request, 'registration/login.html', {'error': 'Invalid username or password.'})

    return render(request, 'registration/login.html')

