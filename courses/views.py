from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.decorators import action

from rest_framework.response import Response


from . import models
from . import serializers


class Course(generics.ListCreateAPIView):
    queryset = models.Course.objects.all()
    serializer_class = serializers.CourseSerializer


class CourseDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Course.objects.all()
    serializer_class = serializers.CourseSerializer

class Review(generics.ListCreateAPIView):
    queryset = models.Review.objects.all()
    serializer_class = serializers.ReviewSerializer

    def get_queryset(self):        
        return self.queryset.filter(course__id=self.kwargs.get("course_pk"))
    
    def perform_create(self, serializer):
        course = get_object_or_404(models.Course, pk=self.kwargs.get("course_pk"))
        serializer.save(course=course)
    


class ReviewDetail(generics.ListCreateAPIView):
    queryset = models.Review.objects.all()
    serializer_class = serializers.ReviewSerializer

    def get_object(self):
        return get_object_or_404(
            self.get_queryset(), 
            course__id=self.kwargs.get("course_pk"),
            pk=self.kwargs.get("review_pk")
        )

class CourseViewSet(viewsets.ModelViewSet):
    queryset = models.Course.objects.all()
    serializer_class = serializers.CourseSerializer

    @action(methods=["GET"], detail=True)
    def reviews(self, req, pk=None):
        course = self.get_object()
        serializer = serializers.ReviewSerializer(
            course.reviews.all(), many=True
        )
        return Response(serializer.data)



class ReviewViewSet(viewsets.ModelViewSet):
    queryset = models.Review.objects.all()
    serializer_class = serializers.ReviewSerializer
