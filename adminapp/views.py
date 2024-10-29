from django.http import JsonResponse
from django.shortcuts import redirect, render
from adminapp.models import *
from guest.models import *
from django.contrib import messages


# Create your views here.
def adminindex(request):
    user_count = user.objects.all().count()
    rent_count = rentholder.objects.all().count()
    
    return render(request, "admin/index.html", {"usercount": user_count,"rent_count":rent_count})

def statedistrict(request):
    state_details = state.objects.all()
    return render(request, "admin/statedistrict.html", {"state_details": state_details})

def category(request):
    return render(request, "admin/category.html") 

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

    
      
    
         