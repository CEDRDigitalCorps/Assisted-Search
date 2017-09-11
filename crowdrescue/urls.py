from django.conf.urls import url
from django.contrib import admin
from crowdrescue.search.views import HomeView, SearchView


urlpatterns = [
    url(r'^$', HomeView.as_view(), name="home"),
    url(r'^search/$', SearchView.as_view(), name="search"),
    url(r'^admin/', admin.site.urls),
]
