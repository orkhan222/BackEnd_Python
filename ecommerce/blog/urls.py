from django.urls import path
from .views import *

urlpatterns = [
    path('', index,name="index"),
    path('commet_detail/<int:id>', commet_detail,name="commet_detail"),
    path('delete/<int:id>', delete,name="delete"),
    path('create/', create,name="create"),
    path('update/<int:id>', update,name="update"),

    
]