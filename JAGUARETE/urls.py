from django.urls import path
from . import views

app_name = "JAGUARETE"

urlpatterns = [
    path('', views.index, name="index"),
    path('acerca-de/', views.acerca_de, name="acerca-de"),
    path('contacto/', views.contacto, name="contacto"),
    path('nuevo_producto', views.nuevo_producto, name="nuevo_producto"),
    path('editar_producto/<int:id_producto>', views.editar_producto, name="editar_producto"),
    path('producto/<int:id_producto>', views.producto, name="producto")
]