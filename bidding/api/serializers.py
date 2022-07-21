from rest_framework import serializers
from Auction.models import Auction,Profile

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model= Profile
        fields = '__all__'

class AuctionSerializer(serializers.ModelSerializer):
    auction = serializers.SerializerMethodField()
    class  Meta:
        model = Auction
        fields = '__all__'
    def get_auction(self,obj):
        auction = obj.profile_set.all()
        serializer = ProfileSerializer(auction,many=True)
        return serializer.data