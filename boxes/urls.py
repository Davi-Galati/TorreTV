from django.urls import path
from . import views

urlpatterns = [path('',views.boxes, name='boxes'),
path('<int:box_id>',views.box, name='box')

]
