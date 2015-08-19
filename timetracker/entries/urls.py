from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.RootRedirectView.as_view(), name='root'),
    url(r'^clients/$', views.ClientListView.as_view(), name='client-list'),
    url(r'^clients/create$', views.ClientCreateView.as_view(), name='client-create'),
    url(r'^clients/(?P<pk>\d+)/$', views.ClientDetailView.as_view(), name='client-detail'),
    url(r'^entries/$', views.EntryListView.as_view(), name='entry-list'),
    url(r'^projects/$', views.ProjectListView.as_view(), name='project-list'),
    url(r'^projects/create$', views.ProjectCreateView.as_view(), name='project-create'),
    url(r'^projects/(?P<pk>\d+)/$', views.ProjectDetailView.as_view(), name='project-detail'),
]
