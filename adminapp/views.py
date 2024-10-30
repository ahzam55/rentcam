from django.http import JsonResponse
from django.shortcuts import redirect, render
from adminapp.models import *
from guest.models import *
from users.models import *
from django.db.models import Sum
from django.contrib import messages


# Create your views here.
def adminindex(request):
    user_count = user.objects.all().count()
    rent_count = rentholder.objects.all().count()
    totel_count = bookingmaster.objects.all().count()
    profit_count = payment.objects.all().count()
    payment_details = payment.objects.all()
    payment_data = []
    for data in payment_details:
        total_price=data.adv_amount+data.bal_amount
        payment_data.append({
            "bill" :data.bill_no,
            "payment_date":data.payment_date,
            "total_price": total_price,
            "payment_status": data.payment_status,
        })
        
    return render(request, "admin/index.html", {"usercount": user_count,"rent_count":rent_count,"totel_count":totel_count,"profit_count":profit_count,"payment_data":payment_data})

def statedistrict(request):
    state_details = state.objects.all()
    return render(request, "admin/statedistrict.html", {"state_details": state_details})

def paymentdetails(request):
    payment_details = payment.objects.all()
    total_amt = payment.objects.aggregate(Sum('adv_amount'))['adv_amount__sum']
    total_amtp = bookingmaster.objects.aggregate(Sum('total_price'))['total_price__sum']
    print(total_amt)
    payment_data = []
    for data in payment_details:
        total_price=data.adv_amount+data.bal_amount
        payment_data.append({
            "bill" :data.bill_no,
            "adv_amount" :data.adv_amount,
            "payment_date":data.payment_date,
            "total_price": total_price,
            "payment_status": data.payment_status,
        })
    return render(request, "admin/paymentdetails.html", {"payment_data": payment_data,"total_amt": total_amt,"total_amtp": total_amtp}) 

def category(request):
    return render(request, "admin/category.html") 

def bookingdetails(request):
    
    user_details = booking.objects.select_related("product","login")
    booking_data = []
    for booked in user_details:
        # print(booked.bill_id)
        master_booking = bookingmaster.objects.get(id=booked.bill_id)
        # print(master_booking.booking_date)
        rentholder_data=rentholder.objects.get(rentholder_login=booked.rentholder_id)
        print(rentholder_data.rentholder_name)
        booking_data.append({
            "user_name" :booked.login.username,
            "product_name": booked.product.product_name,
            "rentholder": rentholder_data.rentholder_name,
            "from_date": booked.from_date,
            "to_date": booked.to_date,
            "bill_id": booked.bill_id,
            "booking_date": master_booking.booking_date,
            "total_price": master_booking.total_price
        })
    
    return render(request, "admin/bookingdetails.html", {"booking_data": booking_data}) 


def tbl_category(request):
    Category_details = categories.objects.all()
    Brand_details = brand.objects.all()
    return render(request, "admin/tbl_category.html", {"Category_details": Category_details,"Brand_details": Brand_details}) 




def statedistrictedit(request,id):
    if request.method == "POST":
        stateid = request.POST.get('stateid')
        print(stateid)
        districtname = request.POST.get('districtname')
        print(districtname)
        
        
        reg_obj=district.objects.get(id=id)
        
        reg_obj.state = state.objects.get(id=stateid)
        reg_obj.districtname = districtname
        reg_obj.save()
        return redirect(tbl_statedistrict)
    else:
        statedistrictdata=district.objects.get(id=id)
        state_details = state.objects.all()
        return render(request, "admin/statedistrictedit.html",{"statedistrictdetails":statedistrictdata,"state_details": state_details})

def tbl_statedistrict(request):
    state_details=state.objects.all()
    district_details=district.objects.select_related("state").all()
    return render(request, "admin/tbl_statedistrict.html",{"district_details": district_details,"state_details": state_details})

def stateaction(request):
    if request.method=="POST":
        statename=request.POST.get('statename')
        print(statename)
        if state.objects.filter(statename=statename).exists():
                messages.success(request,'state Already Exist!')
                return render(request,"admin/statedistrict.html")
        reg_obj = state()
        
        reg_obj.statename = statename
        reg_obj.save()
        
        return render(request, "admin/statedistrict.html")
    
def districtaction(request):
    if request.method=="POST":
         stateid = request.POST.get('stateid')
         print(stateid)
         districtname = request.POST.get('districtname')
         print(districtname)
         if district.objects.filter(state=stateid,districtname=districtname).exists():
            messages.success(request,'state & district Already Exist!')
            return redirect("statedistrict")
         
                  
         reg_obj = district()
         
         reg_obj.state = state.objects.get(id=stateid)
         reg_obj.districtname = districtname
         reg_obj.save()
         
         return redirect("statedistrict")
     
def categoriesaction(request):
    if request.method=="POST":
        categoriesname = request.POST.get('categoriesname')
        print(categories)
        if categories.objects.filter(categoriesname=categoriesname).exists():
                messages.success(request,'category Already Exist!')
                return render(request,"admin/category.html")
            
            
        reg_obj = categories()
        reg_obj.categoriesname = categoriesname
        reg_obj.save()
        
        return render(request,"admin/category.html")
    
def brandaction(request):
    if request.method=="POST":
        brandid = request.POST.get('brand')
        print(brand)
        if brand.objects.filter(brand=brandid).exists():
                messages.warning(request,'brand Already Exist!')
                return render(request,"admin/category.html")
            
            
        reg_obj = brand()
        
        reg_obj.brand = brandid
        reg_obj.save()
        
        return render(request,"admin/category.html") 
    
def statedelete(request,id):
    statedata=state.objects.get(id=id)
    statedata.delete()
    return redirect(tbl_statedistrict)

def districtdelete(request,id):
    districtdata=district.objects.get(id=id)
    districtdata.delete()
    return redirect(tbl_statedistrict)

def categorydelete(request,id):
    categorydata=categories.objects.get(id=id)
    categorydata.delete()
    return redirect(tbl_category)

def branddelete(request,id):
    branddata=brand.objects.get(id=id)
    branddata.delete()
    return redirect(tbl_category)  

def categorieseditaction(request,id):
    if request.method == "POST":
       print(id)
       categoriesname = request.POST.get('categoriesname')
       print(categories)
        
        
       reg_obj=categories.objects.get(id=id)
        
       reg_obj.categoriesname = categoriesname
       reg_obj.save()
       return redirect(tbl_category)
    else:
        categories_details=categories.objects.get(id=id)
        return render(request, "admin/categoryedit.html",{"categories_details": categories_details})
    
def brandeditaction(request,id):
    if request.method == "POST":
       print(id)
       brandname = request.POST.get('brand')
       print(brandname)
        
        
       reg_obj=brand.objects.get(id=id)
        
       reg_obj.brand = brandname
       reg_obj.save()
       return redirect(tbl_category)
    else:
        brand_details=brand.objects.get(id=id)
        return render(request, "admin/brandedit.html",{"brand_details": brand_details})

    
      
    
         