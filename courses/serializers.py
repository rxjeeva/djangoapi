from rest_framework import serializers
from .models import Course

class CourseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Course
        # field = ('id', 'name', 'language', 'price')
        fields = '__all__'
    
