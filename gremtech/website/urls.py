from django.conf.urls import url

from . import views

app_name = 'website'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^project/(?P<id>[0-9]+)$', views.project, name='project'),
    url(r'^investment$', views.investment, name='investment'),
    url(r'^investment_send$', views.investment_send, name='investment_send'),
    url(r'^feedback$', views.feedback, name='feedback'),
    url(r'^feedback_send$', views.feedback_send, name='feedback_send'),
    url(r'^old_browser$', views.old_browser, name='old_browser'),
]
