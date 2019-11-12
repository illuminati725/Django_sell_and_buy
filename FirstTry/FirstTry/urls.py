"""first_try URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.conf.urls import url
from django.urls import path, include
from account import views as account_views
from item import views as item_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^account/', include('account.urls')),
    url(r'^$',account_views.home,name='home'),
    url(r'^home/(?P<category>.+)/$',item_views.category_page,name='category_page'),
    url(r'^home/profile/(?P<name>.+)/$',account_views.user_profile,name='user_profile'),
    url(r'^home/post/(?P<name>.+)/$',account_views.post,name='post'),
    url(r'^profile/$',account_views.profile,name='profile'),
    url(r'^login/$',auth_views.LoginView.as_view(template_name='account/login.html'),name='login'),
    url(r'^logout/$',auth_views.LogoutView.as_view(template_name='account/logout.html'),name='logout'),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
