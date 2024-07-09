from django.urls import path, include
from .import views
urlpatterns = [
    path('',views.job_list),   #al jops
    path('<int:id>/',views.job_detail), #one jop

]