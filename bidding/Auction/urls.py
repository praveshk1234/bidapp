from django.urls import path,include
from .views import auctionlist,auctiondetail,register_view,login_view,logout_view
urlpatterns = [
    path('',auctionlist,name='index'),
   
    path('registeruser/', register_view, name="registeruser"),
    path('login/',login_view,name="login"),
    path('logout/',logout_view,name="logout"),
    path('<str:pk>/',auctiondetail,name='auction-detail'),
]