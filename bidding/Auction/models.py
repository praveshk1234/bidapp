from django.db import models
from django.contrib.auth.models import User
import uuid
from django.utils import timezone
from django.db.models import Max
from django.db.models.signals import post_save
# Create your models here.

class Auction(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True,primary_key=True,editable=False)
    item_image = models.ImageField(blank=True,null=True,upload_to="item_image",default="item.png")
    item_name = models.CharField(max_length=200)
    item_detail = models.TextField()
    startdate=models.DateTimeField(auto_now_add=True)
    enddate=models.DateTimeField(blank=True,null=True)
    startprice=models.IntegerField(blank=True,null=True)
    highbid=models.IntegerField(blank=True,null=True)
    def __str__(self):
        return str(self.item_name)
    @property
    def imageURL(self):
        try:
            url = self.item_image.url
        except:
            url=''
        return url

    @property
    def maxBidAmount(self):
       alluser = self.profile_set.all().aggregate(Max('amount')) 
       self.highbid = alluser['amount__max']
       self.save()
       print("Max amount",alluser['amount__max'])
    @property
    def bidStatus(self):
        currenttime = timezone.now()
        if currenttime <= self.enddate:
            bidactive = True
        else:
            bidactive = False
        return bidactive
class Profile(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True,primary_key=True,editable=False)
    amount = models.IntegerField(blank=True,null=True)
    name=models.OneToOneField(User,on_delete=models.CASCADE,blank=True,null=True)
    auction = models.ForeignKey(Auction,on_delete=models.CASCADE,blank=True,null=True)
    def __str__(self):
        return str(self.name)

def createProfile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(name=instance)

post_save.connect(createProfile,sender=User)
    