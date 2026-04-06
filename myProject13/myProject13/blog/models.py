

'''

"""
========================
Retrieving Data from Database
========================

• Django uses ORM (Object Relational Mapper) to interact with the database.
• ORM allows us to write Python code instead of SQL queries.
• Data is retrieved using QuerySet methods.
"""

# --------------------------------------------------
# Django ORM QuerySet
# --------------------------------------------------

"""
• A QuerySet is a collection of database objects.
• It represents rows from a database table.
• QuerySets are lazy (data is fetched only when needed).
"""

# Example
from myapp.models import Student


# --------------------------------------------------
# all() Method
# --------------------------------------------------

"""
• all() is used to fetch all records from a table.
• It returns a QuerySet.
"""

students = Student.objects.all()
print(students)


# --------------------------------------------------
# get() Method
# --------------------------------------------------

"""
• get() is used to fetch a single record.
• It returns one object.
• Raises error if:
    - No record found (DoesNotExist)
    - Multiple records found (MultipleObjectsReturned)
"""

student = Student.objects.get(id=1)
print(student)


# --------------------------------------------------
# filter() Method
# --------------------------------------------------

"""
• filter() is used to fetch records based on condition.
• It returns a QuerySet.
• Does NOT raise error if no records found.
"""

students = Student.objects.filter(age=20)
print(students)


# --------------------------------------------------
# Using Django Shell
# --------------------------------------------------

"""
• Django shell is used to test queries.
• Run the command:

    python manage.py shell
"""

# Inside shell:
# from myapp.models import Student
# Student.objects.all()


"""
========================
Important Interview Difference
========================

get()
• Returns single object
• Raises error if none/multiple

filter()
• Returns QuerySet
• No error if empty
"""


'''





from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField(unique=True)
    city = models.CharField(max_length=100,default='unkown')
    
    def __str__(self):
        return super().__str__()
    