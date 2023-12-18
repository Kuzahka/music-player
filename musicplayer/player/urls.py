from django.urls import path, include
from . import views
from .views import SongList, SongDetail
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


app_name = 'player'
urlpatterns = [
    path('', views.index, name='index'),
    path('upload/', views.upload, name='upload'),
    path('signup/', views.SignUp.as_view(), name='signup'),
    path(
        'login/',
        LoginView.as_view(template_name='player/login.html'),
        name='login'
    ),
    path(
        'logout/',
        # Прямо в описании обработчика укажем шаблон,
        # который должен применяться для отображения возвращаемой страницы.
        # Да, во view-классах так можно! Как их не полюбить.
        LogoutView.as_view(template_name='player/logged_out.html'),
        name='logout'
    ),
    path('songs/', SongList.as_view()),
    path('songs/<int:pk>/', SongDetail.as_view()),
    path('auth/', include('djoser.urls')),
    # JWT-эндпоинты, для управления JWT-токенами:
    path('auth/', include('djoser.urls.jwt')),
]
