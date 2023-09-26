from django.urls import path
from .views import CourseListCreateView, CourseDetailView ,InstanceListCreateView , InstanceDetailView , CourseListByYearSem, CourseListById,InstanceListByYearSemId
# ,InstanceCourseListView,InstanceCourseDetailView


urlpatterns = [
    # 1 & 2 Create a new course and list of all courses available

    path('api/courses/',CourseListCreateView.as_view(),name='course-list-create'),
    path('api/courses/<int:pk>/',CourseDetailView.as_view(),name='course-list-detail'),

    # 3 & 4 View detailed information about a course with ID and delete a course with ID

    path('api/courses/<int:id>/',CourseListById.as_view(),name='course-detail-by-id'),

    #5 & 6 - Create a new instance of a course delivery

    path('api/instances/',InstanceListCreateView.as_view(),name='instance-list-create'),
    path('api/instances/<int:pk>/',InstanceDetailView.as_view(),name='instance-detail'),

    #6 - list of courses delivered in yearand semestet

    path('api/instances/<int:year>/<int:semester>/', CourseListByYearSem.as_view(), name='course-list-by-year-sem'),

    #7 & 8 - View detailed information about an instance of a course ID, delivered in YYYY, and semester
    
    path('api/instances/<int:year>/<int:semester>/<int:course_id>/', InstanceListByYearSemId.as_view(),name='instance-list-by-year-sem'),

    
    
    
]