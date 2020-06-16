from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name='index'),
    path('login/',views.authlogin,name='login'),
    path('signup/', views.signup,name='signup'),
    #path('home/',views.home,name='home'),
    path('logout/',views.logout,name='logout'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('categoryform/<str:name>/',views.categoryform,name='categoryform'),
    path('myforms/<int:id>/',views.myforms,name='myforms'),
    path('form/<int:id>/<str:cat>/',views.form,name='form'),
    path('removeform/<int:id>/<str:cat>/',views.removeform,name='removeform')
]