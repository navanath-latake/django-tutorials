from django.shortcuts import render
from datetime import datetime

def blog_list (request):
    blogs =[
        {"title":"Django Basics","is_featured":True,"author":"Jhon Doe"},
        {"title":"Django Advance","is_featured":False,"author":""},
        {"title":"Django REST Framework","is_featured":False,"author":"Nava"},
    ]
    
    context ={
        "blogs":blogs,
        "today":datetime.now(),
        "html_code":"<h1>Welcome To My Blog<h1/>",
    }
    return render(request, 'blog_list.html',context)