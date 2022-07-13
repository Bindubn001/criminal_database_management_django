
from django.urls import path
from . import views

urlpatterns = [    
    path('', views.registerpage, name='register'),
    path('about_us', views.about_us, name='about_us'), 
    path('home',views.home, name='home'),

    path('login/', views.loginpage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    
    path('crime-list', views.crimeList, name='crime-list'),   
    path('crime-create', views.crimeCreate, name='crime-create'),
    path('crime-update/<int:crime_id>', views.crimeUpdate, name='crime-update'),
    path('crime-delete/<int:crime_id>', views.crimeDelete, name='crime-delete'),

    path('prison-list', views.prisonList, name='prison-list'),   
    path('prison-create', views.prisonCreate, name='prison-create'),
    path('prison-update/<int:prison_id>', views.prisonUpdate, name='prison-update'),
    path('prison-delete/<int:prison_id>', views.prisonDelete, name='prison-delete'),

    path('criminal-list', views.criminalList, name='criminal-list'),   
    path('criminal-create', views.criminalCreate, name='criminal-create'),
    path('criminal-update/<int:criminal_id>', views.criminalUpdate, name='criminal-update'),
    path('criminal-delete/<int:criminal_id>', views.criminalDelete, name='criminal-delete'),

    path('trial-list', views.trialList, name='trial-list'),   
    path('trial-create', views.trialCreate, name='trial-create'),
    path('trial-update/<int:case_id>', views.trialUpdate, name='trial-update'),
    path('trial-delete/<int:case_id>', views.trialDelete, name='trial-delete'), 

    path('victim-list', views.victimList, name='victim-list'),   
    path('victim-create', views.victimCreate, name='victim-create'),
    path('victim-update/<int:victim_id>', views.victimUpdate, name='victim-update'),
    path('victim-delete/<int:victim_id>', views.victimDelete, name='victim-delete')  
]

    

