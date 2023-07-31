from django.shortcuts import render, redirect
# ⬆️ 안쓰면 지워도 상관 ❌
# Flask의 render_template와 비슷
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def hello_world(request):
    return HttpResponse("Hello, World!")

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)
        if user:
            # 로그인 성공시
            print('로그인 성공')
            # ✅ 사용자 정보 저장
            login(request, user)
            return redirect('home')
        else:
            # 로그인 실패시
            print('로그인 실패')

    return render(request, 'login.html')

@login_required
def home_view(request):
    # 로그인한 사용자 정보 불러오기
    user = request.user
    # ✨ context 딕셔너리로 전달 필요 ➡️ render가 기본적으로 받는 변수
    # ✨ html에서 jinja {{ username }} 사용 가능
    # ✨ 보낼 때 'context'만 써도 됨 : 이름 바꿔도 됨 보낼 때 순서만 세 번째!
    context = {
        'username': user.username,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'email': user.email
    }
    return render(request, 'home.html', context)

def logout_view(request):
    logout(request)
    return redirect('login')