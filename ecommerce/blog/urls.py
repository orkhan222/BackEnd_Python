from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name="index"),
    path('commet/<int:id>', views.commet,name="commet"),
    path('commet_detail/<int:id>', views.commet_detail,name="commet_detail"),
    path('delete/<int:id>', views.delete,name="delete"),
    path('create/', views.create,name="create"),
    path('update/<int:id>', views.update,name="update"),

    
]