from django.contrib import admin
from django.urls import path, include
from users import views as userViews
from django.contrib.auth import views as authViews


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', include('homepage.urls')),
    path('', include('homepage.urls'), name='home'),
    path('reg/', userViews.register, name='reg'),
    path('login/', authViews.LoginView.as_view(template_name="users/login.html"),name = 'login'),
    path('exit/', authViews.LogoutView.as_view(template_name="users/exit.html"), name='exit'),
    path('profile/', userViews.profile, name='profile')
]
