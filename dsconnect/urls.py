"""dsconnect URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from network.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index, name = 'index'),
    url(r'^login/', login_view , name = "login"),
    url(r'^profile/(?P<user_id>[0-9]+)/$', profile, name = "profile"),
    url(r'^edit_profile/', edit_profile , name = "edit_profile"),
    url(r'^home/', home , name = "home"),
    url(r'^signup/', signup , name = "signup"),
    url(r'^logout/', logout_view, name = "logout"),
    url(r'^delete/postid=(?P<post_id>[0-9]+)/$', delete_post, name = 'delete_post'),
    url(r'^docs/$', upload_file , name='upload_file'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


