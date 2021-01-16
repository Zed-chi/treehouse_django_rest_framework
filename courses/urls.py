from django.urls import path
from .import views

app_name = 'courses'


urlpatterns = [
    path("", views.Course.as_view(), name="course_list"),
    path("<int:course_pk>/reviews/", views.Review.as_view(), name="review_list"),
    path("<int:course_pk>/reviews/<int:review_pk>", views.ReviewDetail.as_view(), name="review"),
    path("<int:pk>", views.CourseDetail.as_view(), name="course"),
]