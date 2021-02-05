from django.shortcuts import render
from .models import Signup
from django.http import HttpResponseRedirect
# Create your views here.


def index(request):
    return render(request, 'signup/index.html')

def signup(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        user_id = request.POST.get('user_id')
        user_pw = request.Post.get('user_pw')
        return HttpResponseRedirect('/index/')
    return render(request, 'index.html')

