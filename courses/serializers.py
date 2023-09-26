from rest_framework import serializers
from .models import CourseItem
from .models import InstanceItem




class CourseItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseItem
        fields = '__all__'


class InstanceItemSerializer(serializers.ModelSerializer):
    # course = CourseItemSerializer()
    class Meta:
        model = InstanceItem
        fields = '__all__'

class CourseInstanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = InstanceItem
        fields = '__all__'