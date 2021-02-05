from django.shortcuts import render
from .models import Signup
from django.http import HttpResponse
# Create your views here.


def index(request):
    return render(request, 'index.html')


def signup(request):
    if request.method == "GET":
        return render(request, 'index.html')

    elif request.method == 'POST':
        email = request.POST('email')
        user_id = request.POST('user_id')
        user_pw = request.Post('user_pw')
        user_pw_re = request.Post('user_pw_re')

        if user_pw != user_pw_re:
            return HttpResponse("비밀번호가 다름")

        register = Signup(
            email=email,
            user_id=user_id,
            user_pw=user_pw,
        )
        register.save()

        return render(request, 'index.html')


