'''

"""
========================
Django Example: Retrieve & Display Student Data
========================

• This example shows complete flow:
    Model → View → Template
• Data is fetched from database and displayed in HTML.
"""

# --------------------------------------------------
# models.py (Database Table)
# --------------------------------------------------

from django.db import models

class Student(models.Model):
    
    """
    • Define fields (columns of table)
    """
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    city = models.CharField(max_length=100)
    
    """
    • String representation of object
    """
    def __str__(self):
        return self.name


# --------------------------------------------------
# views.py (Business Logic)
# --------------------------------------------------

from django.shortcuts import render
from .models import Student

def student_list(request):
    
    """
    • Fetch all student records from database
    • Student.objects.all() returns QuerySet
    """
    students = Student.objects.all()
    
    """
    • Context Definition:
        Context is a dictionary used to send data
        from views.py to HTML template.
    
    • Why we use context:
        HTML cannot directly access database data.
        So we pass data using context.
    """
    context = {
        'students': students   # key → template variable, value → actual data
    }
    
    """
    • render() sends context data to template
    """
    return render(request, 'portfolio/student_list.html', context)


# --------------------------------------------------
# Template: student_list.html (Frontend)
# --------------------------------------------------

"""
<!DOCTYPE html>
<html>
<head>
    <title>My Portfolio</title>
</head>
<body>

    <h1>Student Data</h1>

    {% if students %}
    
    <table border="1">
        <thead>
            <tr>
                <th>Name</th>
                <th>Age</th>
                <th>City</th>
            </tr>
        </thead>

        <tbody>
            {% for student in students %}
            <tr>
                <td>{{ student.name }}</td>
                <td>{{ student.age }}</td>
                <td>{{ student.city }}</td>
            </tr>
            {% endfor %}
        </tbody>
    </table>

    {% else %}
        <p>No student data available</p>
    {% endif %}

</body>
</html>
"""

# --------------------------------------------------
# Explanation (Step-by-Step Flow)
# --------------------------------------------------

"""
1. Model (Student)
   → Defines database table structure

2. View (student_list)
   → Fetches data using ORM
   → Creates context dictionary
   → Sends data to template

3. Template (HTML)
   → Receives context data
   → Displays using {{ }} and loops

Flow:
Database → Model → View → Context → Template → Browser
"""

# --------------------------------------------------
# Key Concepts Used
# --------------------------------------------------

"""
• objects.all() → fetch all records
• QuerySet → collection of students

• Context → dictionary to pass data
• Why context → connect backend to frontend

• render() → send data + load template
• {{ }} → display variable
• {% for %} → loop through data
• {% if %} → condition check
"""

# --------------------------------------------------
# Output
# --------------------------------------------------

"""
• Displays student data in table format
• If no data → shows:
  "No student data available"
"""

'''