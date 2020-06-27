from django.conf.urls import url
from users import views


# Template URLS!

app_name = 'users'

urlpatterns = [
    url(r'^register/$', views.register, name='register'),
    url(r'^user_login/$', views.user_login, name='user_login')
]
