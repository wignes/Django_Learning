from django.urls import path
from basicapp import views


#Template URL
app_name = "basicapp"

urlpatterns = [
  path('register/', views.register, name="register"),
  path('login/',views.user_login, name="user_login"),
]