from django.conf.urls import include, url
from django.contrib import admin
from lib.views import Hello,current_datetime
urlpatterns = [
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^hello/$',Hello),
    url(r'^time/$',current_datetime)
]
