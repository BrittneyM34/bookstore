from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm

# Define a function view that takes a request from user
def login_view(request):
    # initialize:
    error_message = None
    # form object with username and password fields
    form = AuthenticationForm()

    # when user hits "login" button, then POST request is generated
    if request.method == "POST":
        # read the data sent by the form via POST request
        form = AuthenticationForm(data=request.POST)

        # Check if form is valid
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            # use Django authenticate function to validate the user
            user=authenticate(username=username, password=password)
            # If user is authenticated:
            if user is not None: 
                # then use pre=defined Django function to login
                login(request, user)
                return redirect('sales:records')
        else:
            error_message = 'oops.. something went wrong'
    
    # prepare data to send from view to template
    context = {
        'form': form,
        'error_message': error_message
    }

    return render(request, 'auth/login.html', context)

def logout_view(request):
    logout(request)
    return redirect('login')