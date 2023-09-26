from django.shortcuts import render


# Create your views here.

from rest_framework import generics
from .models import CourseItem
from .serializers import CourseItemSerializer

from .models import InstanceItem 
from .serializers import InstanceItemSerializer


from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework import status
from rest_framework.response import Response



class CourseListCreateView(generics.ListCreateAPIView):
    queryset = CourseItem.objects.all()
    serializer_class = CourseItemSerializer

class CourseDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CourseItem.objects.all()
    serializer_class = CourseItemSerializer

class InstanceListCreateView(generics.ListCreateAPIView):
    queryset = InstanceItem.objects.all()
    serializer_class = InstanceItemSerializer

class InstanceDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = InstanceItem.objects.all()
    serializer_class = InstanceItemSerializer

class InstanceCourseListView(APIView):
    def get(self, request, year, semester):
        instances = CourseItem.objects.filter(year=year, semester=semester)
        serializer = CourseItemSerializer(instances, many=True)
        return Response(serializer.data)

# to access course from instance

# class InstanceCourseDetailView(APIView):
#     def get(self, request, year, semester, id):
#         try:
#             instance = CourseItem.objects.get(year=year, semester=semester, id=id)
#         except CourseItem.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)
#         serializer = CourseItemSerializer(instance)
#         return Response(serializer.data)

#     def delete(self, request, year, semester, id):
#         try:
#             instance = CourseItem.objects.get(year=year, semester=semester, id=id)
#         except CourseItem.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)
#         instance.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
    

class CourseListByYearSem(generics.ListAPIView):
    serializer_class = InstanceItemSerializer

    def get_queryset(self):
        year = self.kwargs['year']
        semester = self.kwargs['semester']
        return InstanceItem.objects.filter(year=year, semester=semester)
    
class InstanceListByYearSemId(generics.ListAPIView):
    serializer_class = InstanceItemSerializer

    def get_queryset(self):
        course_id = self.kwargs['course_id']
        year = self.kwargs['year']
        semester = self.kwargs['semester']
        return InstanceItem.objects.filter(course_id=course_id,year=year,semester=semester)
    
    def delete(self):
        course_id = self.kwargs['course_id']
        year = self.kwargs['year']
        semester = self.kwargs['semester']
        try:
            deleteInstanceList  = InstanceItem.objects.filter(course_id=course_id)
            if deleteInstanceList.exists():
                deleteInstanceList.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
            else:
                return Response({"message": "No instances found for the specified year and semester"}, status=status.HTTP_404_NOT_FOUND)
            
        except Exception as e:
            return Response({"message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


        

    
class CourseListById(generics.ListAPIView):
    serializer_class = CourseItemSerializer

    def get_queryset(self):
        id = self.kwargs['id']
        # year = self.kwargs['year']
        # semester = self.kwargs['semester']
        return CourseItem.objects.filter(id=id)
    
    def delete(self,id):
        try:
            instances_queryset = CourseItem.objects.filter(id)
            if instances_queryset.exists():
                instances_queryset.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
            else:
                return Response({"message": "No instances found for the specified year and semester"}, status=status.HTTP_404_NOT_FOUND)
            
        except Exception as e:
            return Response({"message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

