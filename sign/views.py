from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import auth
from django.shortcuts import redirect

# Create your views here.


def login(request):
    return render(request, 'sign/login.html', {
        'page_title': 'User Login'
    })


def login_process(request):
    user_id = request.POST['user_id']
    user_password = request.POST['user_pw']
    user = auth.authenticate(request, username=user_id, password=user_password)
    if user is not None:
        auth.login(request, user)
        user_dict = {
            'u_id': user.id,
            'u_name': user.username
        }
        request.session['loginObj'] = user_dict
        return redirect('home')
    else:
        return render(request, 'sign/login.html', {
            'err_msg': '로그인 실패입니다. 다시 시도해보세요!'
        })


def signup(request):
    return render(request, 'sign/signup.html', {
        'page_title': 'User Signup'
    })


def signup_process(request):
    u_id = request.POST['user_id']
    u_email = request.POST['email']
    u_password1 = request.POST['user_pw']
    u_password2 = request.POST['user_pw_re']

    # 이미 존재하는 id(이메일)인지를 확인
    user_list = User.objects.all()
    if user_list.filter(username=u_email).exists():
        return redirect('users:signup', {
            'err_msg': '존재하는 email입니다.'
        })
    elif user_list.filter(username=u_id).exists():
        return redirect('users:signup', {
            'err_msg': '존재하는 ID입니다.'
        })

    elif u_password1 == u_password2:
        user = User.objects.create_user(username=u_id, password=u_password1)
        auth.login(request, user)
        user_dict = {
            'user_id': user.id,
            'user_name': user.username
        }
        request.session['loginObj'] = user_dict
        return redirect('home')
    else:
        return render(request, 'sign/signup.html', {
            'err_msg': '비밀번호가 일치하지 않습니다.'
        })


def logout(request):
    auth.logout(request)
    return redirect('home')
