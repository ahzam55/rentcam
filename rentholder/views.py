from django.shortcuts import redirect, render
from django.shortcuts import render
from users.models import *

# Create your views here.
def rentholderindex(request):
    
    return render(request, "rentholder/index.html")

def rentholderabout(request):
    
    return render(request, "rentholder/about.html")

def rentholderblog(request):
    
    return render(request, "rentholder/blog.html")

def rentholderservices(request):
    
    return render(request, "rentholder/services.html")

def rentholderpricing(request):
    rentholderid=request.session['loginid']
    booked_products_list=booking.objects.select_related("product").filter(rentholder_id=rentholderid)
    
    booking_data = []
    for booked in booked_products_list:
        master_booking = bookingmaster.objects.get(id=booked.bill_id)
        # print(master_booking.id)
        booking_data.append({
            "id":master_booking.id,
            "product_image": booked.product.product_image,
            "product_name": booked.product.product_name,
            "from_date": booked.from_date,
            "to_date": booked.to_date,
            "booking_status": booked.booking_status,
            "total_price": master_booking.total_price
        })
        
    # print(booking_data)
    
    return render(request, "rentholder/pricing.html",{"booked_products_list": booking_data})

def bookinghistory(request):
    rentholderid=request.session['loginid']
    booked_products_list=booking.objects.select_related("product").filter(rentholder_id=rentholderid)
    booking_data = []
    for booked in booked_products_list:
        master_booking = bookingmaster.objects.get(id=booked.bill_id)
        booking_data.append({
            "product_image": booked.product.product_image,
            "product_name": booked.product.product_name,
            "from_date": booked.from_date,
            "to_date": booked.to_date,
            "booking_status": booked.booking_status,
            "total_price": master_booking.total_price
        })
        
    # print(booking_data)
    return render(request, "rentholder/bookinghistory.html",{"booking_data": booking_data})

def rentholderportfolio(request):
    
    return render(request, "rentholder/portfolio.html")

def rentholdergallery(request):
    
    return render(request, "rentholder/gallery.html")

def rentholderportfoliodetails(request):
    
    return render(request, "rentholder/portfolio-details.html")

def rentholderblogdetails(request):
    
    return render(request, "rentholder/blog-details.html")

def rentholdercontact(request):
    
    return render(request, "rentholder/contact.html")

def productform(request):
    Category_details = categories.objects.all()
    Brand_details = brand.objects.all()
    
    return render(request, "rentholder/form.html",{"Category_details": Category_details,"Brand_details": Brand_details})

def productformaction(request):
    if request.method=="POST":
        productname = request.POST.get('product')
        print(productname)
        Category = request.POST.get('Category')
        print(Category)
        Brand = request.POST.get('Brand')
        print(Brand)
        price = request.POST.get('price')
        print(price)
        description = request.POST.get('description')
        print(description)
        remarks = request.POST.get('remarks')
        print(remarks)
        productimage = request.FILES.get('productimage')
        print(productimage)
        login_id = request.session.get("loginid")
        print(login_id)


   
            
            
        reg_obj = product()
        
        reg_obj.product_name = productname
        reg_obj.category = categories.objects.get(id=Category  )
        reg_obj.brand = brand.objects.get(id=Brand)
        reg_obj.rent_price_perday = price
        reg_obj.description = description
        reg_obj.remarks = remarks
        reg_obj.product_image = productimage
        reg_obj.product_status = 'active'
        reg_obj.login = login.objects.get(id=login_id)
        reg_obj.save()
        
        return redirect('rentholderservices')
    
def booking_accept(request,id):
    if request.method == "GET":
        print(id)
        
        booking_obj = booking.objects.get(bill_id=id)
        booking_obj.booking_status ="rentholder accept your order"
        booking_obj.save()
    
    return redirect('rentholderpricing')

def booking_reject(request,id):
    if request.method == "GET":
        print(id)
        
        booking_obj = booking.objects.get(bill_id=id)
        booking_obj.booking_status ="rentholder reject your order"
        booking_obj.save()
    
    return redirect('rentholderpricing')

def booking_goneforrent(request,id):
    if request.method == "GET":
        print(id)
        
        booking_obj = booking.objects.get(bill_id=id)
        booking_obj.booking_status ="Gone for rent"
        booking_obj.save()
    
    return redirect('rentholderpricing')

def booking_itemavailable(request,id):
    if request.method == "GET":
        print(id)
        
        booking_obj = booking.objects.get(bill_id=id)
        booking_obj.booking_status ="item available"
        booking_obj.save()
    
    return redirect('rentholderpricing')