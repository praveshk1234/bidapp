
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework.response import Response
from django.http import JsonResponse
from .serializers import AuctionSerializer
from Auction.models import Auction,Profile
@api_view(['GET'])
def getRoutes(request):
    routes = [
        {'GET': 'helll'},
        {'GET': 'hellfsdfsdl'},
    ]
    return JsonResponse(routes)
@api_view(['GET'])
def getAuctions(request):
    print("USER",request.user)
    biditems = Auction.objects.all()
    serializer = AuctionSerializer(biditems,many=True)
    return Response(serializer.data)
@api_view(['GET'])
def getAuction(request,pk):
    biditem = Auction.objects.get(id=pk)
    serializer = AuctionSerializer(biditem,many=False)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated,IsAdminUser])
def auctionBid(request,pk):
    biditem = Auction.objects.get(id=pk)
    user = request.user
    bid,created = Profile.objects.get_or_create(
        name=user,
        auction=biditem,
        
    )
    bid.auction = biditem
    bid.amount = request.data['amount']
    bid.save()
    biditem.maxBidAmount
    serializer=AuctionSerializer(biditem,many=False)
    return Response(serializer.data)