from django.db import models

# Create your models here.
class CourseItem(models.Model):
    title = models.CharField(max_length=200)
    code = models.IntegerField(default=0)
    description = models.CharField(max_length=400,default='Description')

    def __str__(self):
        return self.title
    

class InstanceItem(models.Model):
    # course = models.ForeignKey(CourseItem,on_delete=models.CASCADE,default=1)
    title = models.CharField(max_length=200)
    year = models.PositiveIntegerField(default=0)
    semester = models.PositiveBigIntegerField(default=0)
    course_id = models.PositiveSmallIntegerField(default=1)

    
    
    def __str__(self):  
        return self.title
    




    
    