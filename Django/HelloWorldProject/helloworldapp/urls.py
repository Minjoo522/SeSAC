from django.urls import path
from . import views

# Flask에서 @app.route('/')와 동일한 역할
urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('home/', views.home_view, name='home'),
    path('', views.hello_world, name='hello_world'),
]