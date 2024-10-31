
from django.db import models

class StudentResult(models.Model):
    student_name = models.CharField(max_length=100)
    roll_number = models.CharField(max_length=6, unique=True )
    subject = models.CharField(max_length=100)
    marks = models.IntegerField()

    def __str__(self):
        return f"{self.student_name} - {self.subject}"



    


