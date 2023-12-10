from django.urls import path
from django.contrib.auth import views as auth_views
from . import views # common.views.py 사용

app_name = 'common'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='common/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.signup, name='signup'), # 회원가입 페이지 매핑
]