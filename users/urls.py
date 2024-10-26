from django.urls import path
from users import views
 
urlpatterns = [
    # path('registration/', views.registration, name="registration"),
    path('index', views.index, name="index"),
    path('about', views.about, name="about"),
    path('blog', views.blog, name="blog"),
    path('Products', views.Products, name="Products"),
    path('pricing', views.pricing, name="pricing"),
    path('portfolio', views.portfolio, name="portfolio"),
    path('gallery', views.gallery, name="gallery"),
    path('portfoliodetails', views.portfoliodetails, name="portfoliodetails"),
    path('blogdetails', views.blogdetails, name="blogdetails"),
    path('contact', views.contact, name="contact"),
    path('view/<int:id>/', views.view, name="view"),
    path('bookingaction', views.bookingaction, name="bookingaction"),
    path('paymentadv/<id>/<price>/<total_price>', views.paymentadv, name="paymentadv"),
    path('ad_paymentaction', views.ad_paymentaction, name="ad_paymentaction"),
    path('bookingconformed', views.bookingconformed, name="bookingconformed"),
    path('paymentbal/<id>/', views.paymentbal, name="paymentbal"),
    path('bal_paymentaction/<id>/', views.bal_paymentaction, name="bal_paymentaction"),
    
    
]