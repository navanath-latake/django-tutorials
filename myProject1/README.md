# 📘 Django Project – Multiple Apps with Views & URLs

## 🚀 What I Learned

In this project, I learned how to create and manage multiple apps in a single Django project and connect them using views and URLs.

---

## 📌 Topics Covered

### 1. Create Project and Multiple Apps
- Created a Django project  
- Created two apps:
  - blog
  - shop  

Command used:
```bash
python manage.py startapp blog
python manage.py startapp shop
```

---

### 2. Add Apps in INSTALLED_APPS
- Registered both apps in settings.py  

Example:
```python
INSTALLED_APPS = [
    'blog',
    'shop',
]
```

---

### 3. Create Views in Each App
- Created separate views for each app  

Example:

blog/views.py
```python
from django.http import HttpResponse

def blog_home(request):
    return HttpResponse("Welcome to Blog App")
```

shop/views.py
```python
from django.http import HttpResponse

def shop_home(request):
    return HttpResponse("Welcome to Shop App")
```

---

### 4. Create URLs for Each App
- Created urls.py inside both apps  

blog/urls.py
```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_home),
]
```

shop/urls.py
```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.shop_home),
]
```

---

### 5. Connect Apps to Main Project URLs
- Linked both apps in main project urls.py using include()  

Example:
```python
from django.urls import path, include

urlpatterns = [
    path('blog/', include('blog.urls')),
    path('shop/', include('shop.urls')),
]
```

---

### 6. Run Server and Final Output
- Successfully ran the server  

URLs:
- http://127.0.0.1:8000/blog/
- http://127.0.0.1:8000/shop/

---

## 🛠️ Tech Used
- Python  
- Django  

---

## 🎯 Conclusion
This project helped me understand:
- How to work with multiple apps in Django  
- How to organize project structure  
- How URLs and views work across different apps  

This is important for building real-world Django applications.

---

## ▶️ How to Run Project

```bash
python manage.py runserver
```