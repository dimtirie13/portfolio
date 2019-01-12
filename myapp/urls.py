from django.urls import path, re_path
from . import views


# template url notation in base.html
app_name = 'myapp'


urlpatterns = [
    path('',views.HomePage.as_view(),name='homepage'),
]