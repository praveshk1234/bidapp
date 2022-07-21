from django.shortcuts import render,redirect
from .models import Auction
from django.views.generic import ListView,DetailView
from .forms import BidForm,AuctionForm,NewUserForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.
def login_view(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("index")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="login.html", context={"login_form":form})

def logout_view(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("index")

def register_view(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("index")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="register.html", context={"register_form":form})
def auctionlist(request):
    itemlist =Auction.objects.all()
    return render(request,'auction_list.html',{'itemlist':itemlist})
@login_required(login_url='login')
def auctiondetail(request,pk):
    item = Auction.objects.get(id=pk)
    profile= request.user.profile
    if request.method == 'POST':
        itemupdate =Auction.objects.filter(id=pk)
        bidvalue=request.POST.get('bidvalue')
        form = BidForm(request.POST,instance=profile)
        if form.is_valid():
            bidform=form.save(commit=False)
            bidform.auction=item
            bidform.name = request.user
            bidform.amount= bidvalue
            bidform.save()
            item.maxBidAmount
            
            return redirect('index')
         
    bidstatus=item.bidStatus
    context ={'object':item,'bidstatus':bidstatus}
    return render(request,'auction_detail.html',context)

def index(request):

    return render(request,'index.html')