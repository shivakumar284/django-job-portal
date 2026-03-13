from django.urls import path
from . import views

urlpatterns=[
  path("",views.job_list,name='job_list'),
  path('job/<int:job_id>/',views.job_detail,name='job_detail'),
  path('apply/<int:job_id>/',views.apply_job,name='apply_job'),
  path('register/',views.register,name='register'),
  path('my_applications/',views.my_applications,name='my_applications'),
  path('logout/',views.logout_view,name='logout'),
]