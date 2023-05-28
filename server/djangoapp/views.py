from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render, redirect
# from .models import related models
from .models import CarMake, CarModel, DealerReview, CarDealer
# from .restapis import related methods
from .restapis import get_request, get_dealer_reviews_from_cf, get_dealers_from_cf, post_request, analyze_review_sentiments
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from datetime import datetime
import logging
import json

# Get an instance of a logger
logger = logging.getLogger(__name__)


# Create your views here.

# Create an `about` view to render a static about page
def about(request):
    return render(request, 'about.html/')


# Create a `contact` view to return a static contact page
def contact(request):
    return render(request, 'contact.html/')

# Create a `login_request` view to handle sign in request
def login_request(request):
    context={}
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['psw']
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('djangoapp:dealerdetails')
        else:
            return render('djangoapp/index.html',context)
    else:
        return render('djangpapp/index.html',context)


# Create a `logout_request` view to handle sign out request
def logout_request(request):
    print("Log out the user `{}`".format(request.user.username))
    logout(request)
    return redirect('djangoappp:dealerdetails')


# Create a `registration_request` view to handle sign up request
def registration_request(request):
    context={}
    if request.method=="GET":
        return render(request,'djangoapp/registration.html',context)
    elif request.method=="POST":
        username=request.POST['username']
        password=request.POST['pwd']
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        user_exist=False
        try:
            User.objects.get(username=username)
            user_exist=True
        except:
            logger.debug('{} is new user'.format(username))
        if not user_exist:
            user=User.objects.create_user(username=username,firstname=firstname,lastname=lastname,password=password)
            login(request,user)
            return redirect("djangoapp:dealerdetails")
        else:
            return render(request,"djangoapp/registration.html",context)



# Update the `get_dealerships` view to render the index page with a list of dealerships
def get_dealerships(request):
    if request.method == "GET":
        url = "https://5d8df0b3-9c09-4b9b-a632-6effe8874263-bluemix.cloudantnosqldb.appdomain.cloud/dealerships/dealer-get"
        # Get dealers from the URL
        dealerships = get_dealers_from_cf(url)
        # Concat all dealer's short name
        dealer_names = ' '.join([dealer.short_name for dealer in dealerships])
        # Return a list of dealer short name
        return HttpResponse(dealer_names)

# Create a `get_dealer_details` view to render the reviews of a dealer
def get_dealer_details(request, dealer_id):
    if request.method=="GET":
        url="https://us-south.functions.appdomain.cloud/api/v1/web/30411ce4-fef6-4c74-9728-cc95aa414e64/dealership-package/get-review"
        reviews=get_dealer_reviews_from_cf(url)
        review_details=' '.join([review.id for review in reviews])
        for review in review_details:
            print(review.sentiment)
        return HttpResponse(review_details)
    

# Create a `add_review` view to submit a review
def add_review(request, dealer_id):
    context={}
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['psw']
        user=authenticate(username=username,password=password)
        if user is not None:
            review["time"]=datetime.utcnow().isoformat()
            review["dealership"]=11
            review["review"]="This is a great car dealer"
            review["name"]="dealer1"

            json_payload["review"]=review
            review_response=post_request(url,json_payload, dealer_id=dealer_id)
            print(review_response)
            return HttpResponse(review_response)




