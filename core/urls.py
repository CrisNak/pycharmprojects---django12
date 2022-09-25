from django.urls import path
from .views import index, contato, produto

urlpatterns = [
    path('', index, name='index'), #pode colocar name ou não
    path('contato', contato, name='contato'),
    path('produto/<int:pk>', produto, name='produto'),
]