from django.shortcuts import render
from datetime import datetime

class User:
    def __init__(self,name,age):
        self.name = name
        self.age = age

def home(request):
    
    Context ={
        "name" : "Navanath",
        "age" : 28,
        "skills" : ["python","Django","flask"],
        "user" : User("Nava",29),
        "blog" : {
            "title": "Django Template Intro",
            "content": "<b>This is Bold</b>",
            "created_at": datetime(2026,1,31,12,13)
        },
        "empty_value": None
        }
    return render(request,"home.html",Context)
    
