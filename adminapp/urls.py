from django.urls import path
from adminapp import views
 
urlpatterns = [
    # path('registration/', views.registration, name="registration"),
    path('adminindex', views.adminindex, name="adminindex"),
    path('statedistrict', views.statedistrict, name="statedistrict"),
    path('category', views.category, name="category"),
    # path('product', views.product, name="product"),
    path('stateaction', views.stateaction, name="stateaction"),
    path('districtaction', views.districtaction, name="districtaction"),
    path('categoriesaction', views.categoriesaction, name="categoriesaction"),
    path('brandaction', views.brandaction, name="brandaction"),
    path('tbl_category', views.tbl_category, name="tbl_category"),
    path('tbl_statedistrict', views.tbl_statedistrict, name="tbl_statedistrict"),
    path('statedelete/<int:id>/', views.statedelete, name="statedelete"),
    path('districtdelete/<int:id>/', views.districtdelete, name="districtdelete"),
    path('statedistrictedit/<int:id>/', views.statedistrictedit, name="statedistrictedit"),
    path('categorydelete/<int:id>/', views.categorydelete, name="categorydelete"),
    path('branddelete/<int:id>/', views.branddelete, name="branddelete"),
    path('categorieseditaction/<int:id>/', views.categorieseditaction, name="categorieseditaction"),
    path('brandeditaction/<int:id>/', views.brandeditaction, name="brandeditaction"),
    path('bookingdetails', views.bookingdetails, name="bookingdetails"),
    path('paymentdetails', views.paymentdetails, name="paymentdetails"),
    
    
    
]