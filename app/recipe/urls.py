from django.urls import path, include

from rest_framework.routers import DefaultRouter
# default router will automatically generate urls for the viewset
from recipe import views


router = DefaultRouter()
# new router object
router.register('tags', views.TagViewSet)
# registers viewset with the router  and give a name

app_name = 'recipe'
# so reverse function can lookup correct names

urlpatterns = [
    path('', include(router.urls))
]
