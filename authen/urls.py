
from django.urls import path
from . import views

urlpatterns = [
    
    path('signup/',views.operatesignup,name="operatesignup"),
    path('login/',views.operatelogin,name="operatelogin"),
    path('logout/',views.operatelogout,name="operatelogout"),
    # path('activate/<uidb64>/<token>',views.ActivateAccount.as_view(),name="activate")
     
]
