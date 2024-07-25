from django.urls import path
from . import views

urlpatterns = [
    path('', views.resultAnalysis, name='Home'),
    path('Html/Result Analysis.html', views.resultAnalysis, name='Result Analysis'),
    path('process_regular_sgpa/', views.process_regular_sgpa, name='Regular SGPA'),
    path('process_reval_sgpa/', views.process_reval_sgpa, name="Reval SGPA"),
    path('process_cgpa/', views.cgpa, name='CGPA'),
    path('Display Data.html', views.display_data, name='Displaying data'),
    path('add_gradepoint/', views.add_gradepoint, name='add gradepoint'), 
    path('delete_gradepoint/',views.delete_gradepoint,name='Delete Gradepoint'),
    path('add_branchcode/',views.add_branchcode,name="add branchcode"),
    path('delete_branchcode/',views.delete_branchcode,name="delete branchcode")
    
]
