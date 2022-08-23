from django.db import models

# Create your models here.

class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    student_number = models.IntegerField()
    #null true & blank true => user can leave empty
    description = models.TextField(null=True, blank=True)

    #auto_now_add method captures the date when data entered for the first time
    register_date = models.DateField(auto_now_add=True)

    #auto_now method captures time each on update 
    last_update_date = models.DateTimeField(auto_now=True)

    is_active = models.BooleanField(default=True)

    # __str__ method for seeing the summary on admin panel
    def __str__(self):
        return (f"{self.student_number} - {self.first_name}")

    def student_year_status(self):
        "Returns the student's year status."
        import datetime
        if self.register_date < datetime.date(2019, 1, 1):
            return "Senior"
        elif self.register_date < datetime.date(2020, 1, 1):
            return "Junior"
        else:
    
    # allows us to filter the data on the admin panel according to student_number, increasing
    class Meta:
        ordering = ["student_number"]
        verbose_name_plural = "student_list"

#! commands below to inform the database and django about my new class/model

# python manage.py makemigrations

# python manage.py migrate