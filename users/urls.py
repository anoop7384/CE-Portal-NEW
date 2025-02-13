from django.urls import path

from . import views

urlpatterns = [
    path('register-single/', views.register_single, name='register_single'),
    # path('<int:pk>/', views.person_update_view, name='person_change'),
    path('register-team/', views.teamForm, name='register_team'),
    path('success/', views.success, name='success'),
    
    
    path('load-competitions-single/', views.load_competitions_single, name='load_competitions_single'),
    path('load-competitions-team/', views.load_competitions_team, name='load_competitions_team'),
    path('load-cities/', views.load_city, name='load_city'), # AJAX
    path('load_minmax/',views.load_minmax,name="load_minmax"),
    path('my_redirect',views.my_redirect,name="my_redirect"),
]