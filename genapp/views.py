from django.shortcuts import render
import random
import string

def home(request):
    return render(request, 'index.html', {})

def about(request):
    return render(request, 'about.html', {})

def generate(request):
    return render(request, 'generate.html', {})

def password(request):
    if request < 8 and request > 16:
        try:
            lower_case = string.ascii_lowercase
            upper_case = string.ascii_uppercase
            number = string.digits
            symbol = string.punctuation

            length = int(request.GET.get('length'))

            create = lower_case + upper_case + number + symbol
            password = "".join(random.sample(create,length))
        except:
            print("Your password must contain 8-16 characters.")
    return render(request, 'password.html', {'password':password})
