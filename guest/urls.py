from django.urls import path
from guest import views

urlpatterns = [
    path('signup', views.signup, name="signup"),
    path('signin', views.signin, name="signin"),
    path('getdistrict', views.getdistrict, name="getdistrict"),
    path('signupaction', views.signupaction, name="signupaction"),
    path('signinaction', views.signinaction, name="signinaction"),
    path('', views.guestindex, name="guestindex"),
    path('guestabout', views.guestabout, name="guestabout"),
    path('guestblog', views.guestblog, name="guestblog"),
    path('guestservices', views.guestservices, name="guestservices"),
    path('guestpricing', views.guestpricing, name="guestpricing"),
    path('portfolio', views.guestportfolio, name="guestportfolio"),
    path('guestgallery', views.guestgallery, name="guestgallery"),
    path('guestportfoliodetails', views.guestportfoliodetails, name="guestportfoliodetails"),
    path('guestblogdetails', views.guestblogdetails, name="guestblogdetails"),
    path('guestcontact', views.guestcontact, name="guestcontact"),
    
    
    
]