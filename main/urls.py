from django.urls import path, reverse_lazy
from django.contrib.auth import views as auth_views
from .views import IndexView, MypageView, ProfileChangeView
from . import views

app_name = 'main'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name="main/login.html"), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page="main:index"), name='logout'),
    path('mypage/<int:pk>/', MypageView.as_view(), name='mypage'),
    path('profile_change/<int:pk>/', ProfileChangeView.as_view(), name='profile_change'),
    path(
        'password_change/',
        auth_views.PasswordChangeView.as_view(
            success_url=reverse_lazy('main:password_change_done'),
            template_name="main/password_change.html"
            ),
        name='password_change'
    ),
    path(
        'password_chnage/done/',
        auth_views.PasswordChangeDoneView.as_view(template_name="main/password_change_done.html"),
        name='password_change_done'
    ),
    path('contact/', views.contact, name='contact'),
    path('contact/complete/', views.contact_complete, name='complete'),
]
