from django.urls import path
from .views import LoginView, RegisterView, LogoutView, ProfilView, ProfilUpdateView


urlpatterns = [
    path('login/', LoginView.as_view(), name='login-view'),
    path('register/', RegisterView.as_view(), name='register-view'),
    path('logout/', LogoutView.as_view(), name='logout-view'),
    path('profile/', ProfilView.as_view(),name="profile-view"),
    path('profil-update/', ProfilUpdateView.as_view(),name="profil-update-view"),

]
