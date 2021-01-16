from rest_framework import routers
from . import views

app_name = "courses"
router = routers.SimpleRouter()
router.register("courses", views.CourseViewSet)
router.register("reviews", views.ReviewViewSet)
