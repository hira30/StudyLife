from django.contrib import admin
from django.urls import include, path
from django.views.generic import base

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('',base.RedirectView.as_view(url='/main/'), ),
    path('', include('main.urls')),
    path('studyapp/', include('studyapp.urls')),
    # 標準viewのデフォルトのurlはaccounts/login/なので，そのアドレスが指定されたらmain/loginにリダイレクトする
    path('accounts/login/', base.RedirectView.as_view(pattern_name="main:login")),
    # loginに成功すると標準ではaccounts/profile/にリダイレクトされるので，main/indexに再リダイレクトする
    path('accounts/profile/', base.RedirectView.as_view(pattern_name="main:index")),
]
