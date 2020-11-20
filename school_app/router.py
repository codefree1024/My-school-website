from .views import CourseViewset, StudentViewset #UserViewSet, GroupViewSet,
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'courses', CourseViewset)
router.register(r'students', StudentViewset)
# router.register(r'users', UserViewSet)
# router.register(r'groups', GroupViewSet)

# localhost:p/api-auth/courses/1
# GET, POST, PUT, DELETE
# list , retrieve