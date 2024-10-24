from django.urls import path
from rentholder import views
 
urlpatterns = [
    # path('registration/', views.registration, name="registration"),
    path('rentholderindex', views.rentholderindex, name="rentholderindex"),
    path('rentholderabout', views.rentholderabout, name="rentholderabout"),
    path('rentholderblog', views.rentholderblog, name="rentholderblog"),
    path('rentholderservices', views.rentholderservices, name="rentholderservices"),
    path('rentholderpricing', views.rentholderpricing, name="rentholderpricing"),
    path('portfolio', views.rentholderportfolio, name="rentholderportfolio"),
    path('rentholdergallery', views.rentholdergallery, name="rentholdergallery"),
    path('rentholderportfoliodetails', views.rentholderportfoliodetails, name="rentholderportfoliodetails"),
    path('rentholderblogdetails', views.rentholderblogdetails, name="rentholderblogdetails"),
    path('rentholdercontact', views.rentholdercontact, name="rentholdercontact"),
    path('productform', views.productform, name="productform"),
    path('productformaction', views.productformaction, name="productformaction"),
    path('booking_accept/<id>', views.booking_accept, name="booking_accept"),
    path('booking_reject/<id>', views.booking_reject, name="booking_reject"),
    
    
]