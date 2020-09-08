from django.urls import path
import blogs.views

urlpatterns = [
    path('', blogs.views.allblogs, name='allblogs'),
    path('<int:blog_id>', blogs.views.singlepost, name="singlepost")
]
