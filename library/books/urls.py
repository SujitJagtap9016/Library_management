from django.urls import path
from books import views
#from .views import UpdatePostView
urlpatterns = [
    path("",views.home,name='home'),
    path("loginuser",views.loginuser,name='loginuser'),
    path("registeruser",views.registeruser,name='registeruser'),
    path("adminprofile",views.adminprofile,name='adminprofile'),
    path("studentprofile",views.studentprofile,name='studentprofile'),
    path("logoutuser",views.logoutuser,name='logoutuser'),
    path("addbook",views.addbook,name='addbook'),
    path("updatebook<int:id>",views.updatebook,name='updatebook'),
    path("deletebook<int:id>",views.deletebook,name='deletebook'),
    path("viewbook",views.viewbook,name='viewbook'),
   


    #path("updatebook1/<int:pk>",UpdatePostView.as_view(),name='updatebook1'),
]