from rest_framework import routers

from backend.apps.blog.api.views import ProjectViewSet

router = routers.DefaultRouter()

router.register('project', ProjectViewSet)
