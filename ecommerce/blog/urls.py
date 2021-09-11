from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name="index"),
    path('commet/<int:id>', views.post_detail,name="post_detail"),

    path('delete/<int:id>', views.delete,name="delete"),
]