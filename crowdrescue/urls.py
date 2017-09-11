from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from crowdrescue.core.views import logout_view, HomeView
from crowdrescue.search.views import SearchView


urlpatterns = [
    url(r'^$', HomeView.as_view(), name="home"),
    url(r'^search/$', SearchView.as_view(), name="search"),
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/login', auth_views.login, name="login"),
    url(r'^logout/$', logout_view, name="logout"),
]
