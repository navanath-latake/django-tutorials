from django.shortcuts import render
from datetime import datetime


def blog_details(request):
    
    post ={
        "title": "My Second Templates Post",  
        "descriptions": "Django is a high level Python Web Framework that encourage rapid development and clean pragmatic design.",
        "author": None,
        "created_at":datetime(2026,2,2,14,24),
         "comments_count":5,
        "tags":["Django","Python","Web Development"],   
        "price": 100,
        "number": 7, 
    }
    return render(request,'blog_details.html',{"post":post})