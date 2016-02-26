from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework import routers
from testrest import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'adds', views.AddViewSet)
router.register(r'groups', views.GroupViewSet)
#router.register(r'creates', views.Createone)
#router.register(r'deleteone', views.deleteone)


urlpatterns = patterns('',
    url(r'^', include(router.urls)),
    url(r'^index/$', views.MyRESTView.as_view()),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
)

