from django.urls import path
from . import views

app_name = 'proejectlist'

urlpatterns=[
    path('',views.project_list,name='project_list'),
    path('<int:project_id>/',views.project_detail,name='project_detail'),
]
