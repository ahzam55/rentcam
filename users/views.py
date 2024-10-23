from django.http import JsonResponse
from django.shortcuts import redirect, render
from users.models import *
from datetime import datetime
# Create your views here.

def index(request):
    
    return render(request, "users/index.html")

def about(request):
    
    return render(request, "users/about.html")

def blog(request):
    
    return render(request, "users/blog.html")

def services(request):
    product_details = product.objects.all()
    
    return render(request, "users/services.html",{"product_details": product_details})

def pricing(request):
    userid=request.session['loginid']
    booking_details=booking.objects.select_related("product").filter(login=userid)
    return render(request, "users/mybooking.html",{"booking_details": booking_details})

def portfolio(request):
    
    return render(request, "users/portfolio.html")

def gallery(request):
    
    return render(request, "users/gallery.html")

def portfoliodetails(request):
    
    return render(request, "users/portfolio-details.html")

def blogdetails(request):
    
    return render(request, "users/blog-details.html")

def bookingconformed(request):
    
    return render(request, "users/thankyou.html")

def contact(request):
    
    return render(request, "users/contact.html")

def paymentadv(request,id,price,total_price):
    remaining=float(total_price)-float(price)
    print(remaining)
    return render(request, "users/payment.html",{"total_price":total_price,"advance":price,"remaining":remaining,"rentholderid":id})

def view(request,id):
    product_details = product.objects.filter(id=id)
    
    
    return render(request, "users/view.html",{"product_details": product_details})

def bookingaction(request):
    if request.method=="POST":
        fromdate=request.POST.get('fromdate')
        print(fromdate)
        todate=request.POST.get('todate')
        print(todate)
        productid=request.POST.get('productid')
        print(productid)
        userid=request.session['loginid']
   
        product_data=product.objects.get(id=productid)
        rentholderid=product_data.login_id
    
        reg_obj = booking()
        reg_obj.from_date = fromdate
        reg_obj.to_date = todate
        reg_obj.product = product.objects.get(id=productid)
        reg_obj.requested_date = datetime.now()
        reg_obj.rentholder_id = rentholderid
        reg_obj.bill_id = 0
        reg_obj.login = login.objects.get(id=userid)
        reg_obj.booking_status = "requested"
        reg_obj.save()
        
        date_format = "%Y-%m-%d"
        from_date = datetime.strptime(fromdate, date_format)
        to_date = datetime.strptime(todate, date_format)

        # Calculate the difference between the two dates
        date_difference = to_date - from_date

        # Get the difference in days as a number
        noofdays = date_difference.days
        price=product_data.rent_price_perday
        total_price=noofdays*price
        advance=total_price*.10
        # reg_obj =bookingmaster()
        # reg_obj.total_price = noofdays * (data.id.rent_price_perday)
        # reg_obj.booking_date =  datetime.now()
        # reg_obj.booking_status =  "requested"
        # reg_obj.rentholder = rentholderid
        # reg_obj.save()
    
    return redirect("paymentadv", id=rentholderid, price=advance,total_price=total_price)


def ad_paymentaction(request):
    if request.method=="POST":
        totalprice=request.POST.get('totalprice')
        # print(totalprice)
        rentholderid=request.POST.get('rentholderid')
        # print(rentholderid)
        advance=request.POST.get('advance')
        # print(advance)
        remaining=request.POST.get('remaining')
        # print(remaining)
        userid = request.session['loginid']
    
        reg_obj =bookingmaster()
        reg_obj.total_price = totalprice
        reg_obj.booking_date =  datetime.now()
        reg_obj.booking_status =  "booked"
        reg_obj.rentholder = login.objects.get(id=rentholderid)
        reg_obj.save()
        
        pay_obj =payment()
        pay_obj.rentholder_id = rentholderid
        pay_obj.payment_date =  datetime.now()
        pay_obj.adv_amount =  advance
        pay_obj.bal_amount =  remaining
        pay_obj.bill_no =  reg_obj.id
        pay_obj.login = login.objects.get(id=userid)
        pay_obj.payment_status =  "booked"
        pay_obj.save()
        
        bill = 0
        booking_obj = booking.objects.get(bill_id=bill)
        
        booking_obj.booking_status = "booked"
        booking_obj.bill_id = reg_obj.id
        booking_obj.save()
    
    return redirect("bookingconformed")

