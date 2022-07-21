from django.urls import path
from .views import getRoutes,getAuctions,getAuction,auctionBid
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
   
    path('bids/',getAuctions),
    path('bids/<pk>/',getAuction),
    path('auction/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auction/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('bids/<str:pk>/raisebid/',auctionBid),
]