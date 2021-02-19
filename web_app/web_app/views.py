from django.shortcuts import render

from .captcha_generator import create_new_captcha

def home_page(request):
    data = create_new_captcha()
    print(data)
    return render(request, "index.html")
