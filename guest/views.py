import datetime
from django.http import JsonResponse
from django.shortcuts import redirect, render
from adminapp.models import *
from guest.models import *
from django.contrib import messages

# Create your views here.

def signup(request):
    state_details = state.objects.all()
    
    return render(request, "guest/signup.html", {"state_details": state_details}) 

def signin(request):
    return render(request, "guest/signin.html")

def guestindex(request):
    
    return render(request, "guest/index.html")

def guestabout(request):
    
    return render(request, "guest/about.html")

def guestblog(request):
    
    return render(request, "guest/blog.html")

def guestservices(request):
    
    return render(request, "guest/services.html")

def guestpricing(request):
    
    return render(request, "guest/pricing.html")

def guestportfolio(request):
    
    return render(request, "guest/portfolio.html")

def guestgallery(request):
    
    return render(request, "guest/gallery.html")

def guestportfoliodetails(request):
    
    return render(request, "guest/portfolio-details.html")

def guestblogdetails(request):
    
    return render(request, "guest/blog-details.html")

def guestcontact(request):
    
    return render(request, "guest/contact.html")


def getdistrict(request):
    if request.method == 'POST':
        stateid = request.POST.get('stateid')

        if stateid:
            district_details = district.objects.filter(state_id=stateid).values('id', 'districtname')
            return JsonResponse(list(district_details), safe=False)
        
        return JsonResponse({'error': 'No state ID provided'}, status=400)
    
    state_details = state.objects.all()
    return render(request, "users/form.html", {"state_details": state_details})

def signupaction (request):
    if request.method=="POST":
        uname=request.POST.get('uname')
        print(uname)
        email=request.POST.get('email')
        print(email)
        mobnumber=request.POST.get('mobnumber')
        print(mobnumber)
        stateid=request.POST.get('stateid')
        print(stateid)
        districtid=request.POST.get('districtid')
        print(districtid)
        addres = request.POST.get('addres')
        print(addres)
        proofimage = request.FILES.get('proofimage')
        print(proofimage)
        pincode = request.POST.get('pincode')
        print(pincode)
        profileimage=request.FILES.get('profileimage')
        print(profileimage)
        psw=request.POST.get('psw')
        print(psw)
        role=request.POST.get('rentoruser')
        print(role)
        if role == "Rentholder":
            print("Processing Rentholder")
            if rentholder.objects.filter(rentholder_email=email, rentholder_contact=mobnumber).exists():
                # Rentholder already exists
                messages.success(request, 'Rentholder Already Exists!')
                return render(request, "guest/signup.html")  # return to signup page
            
            # Create new Login entry for rentholder
            login_obj = login()
            login_obj.username = email
            login_obj.password = psw  
            login_obj.role = 'RENTHOLDER'  
            login_obj.status = 'active'  
            login_obj.save()

            # Create new Rentholder entry
            rentholder_obj = rentholder()
            rentholder_obj.rentholder_name = uname
            rentholder_obj.rentholder_email = email
            rentholder_obj.rentholder_contact = mobnumber
            rentholder_obj.rentholder_address = addres
            rentholder_obj.rentholder_state = state.objects.get(id=stateid)
            rentholder_obj.rentholder_district = district.objects.get(id=districtid)
            rentholder_obj.rentholder_proof = proofimage
            rentholder_obj.rentholder_pincode = pincode
            rentholder_obj.rentholder_imagefile = profileimage
            rentholder_obj.rentholder_registerdate = datetime.date.today()
            rentholder_obj.rentholder_login = login_obj  # Associate rentholder with login
            rentholder_obj.save()

            # Redirect to signin for Rentholder
            return redirect('signin')

        elif role == "User":
            print("Processing User")
            if user.objects.filter(email_id=email, contact_no=mobnumber).exists():
                # User already exists
                messages.success(request, 'User Already Exists!')
                return redirect('signup')

            # Create new Login entry for user
            login_obj = login()
            login_obj.username = email
            login_obj.password = psw  
            login_obj.role = 'USER'  
            login_obj.status = 'active'  
            login_obj.save()

            # Create new User entry
            user_obj = user()
            user_obj.username = uname
            user_obj.email_id = email
            user_obj.contact_no = mobnumber
            user_obj.address = addres
            user_obj.state = state.objects.get(id=stateid)
            user_obj.district = district.objects.get(id=districtid)
            user_obj.proof = proofimage
            user_obj.pincode = pincode
            user_obj.imagefile = profileimage
            user_obj.register_date = datetime.date.today()
            user_obj.save()

            # Redirect to signin for User
            return redirect('signin')
    
    
    
    
def signinaction (request):
    if request.method=="POST":
        email=request.POST.get('uname')
        print(email)
        psw=request.POST.get('psw')
        print(psw)
        
         # Check if the user with given username and password exists
        if login.objects.filter(username=email, password=psw).exists():
             # Fetch the login object
            loginobj = login.objects.get(username=email)
            print(loginobj.status)
            # Check role and status
            if loginobj.role == "USER" and loginobj.status == "active":
                print(loginobj.role)
                # Set session variables for login
                request.session['username'] = loginobj.username
                request.session['loginid'] = loginobj.id
                return redirect('index')
            
            elif loginobj.role == "RENTHOLDER" and loginobj.status == "active":
                print(loginobj.role)
                # Set session variables for login
                request.session['username'] = loginobj.username
                request.session['loginid'] = loginobj.id
                return redirect('rentholderindex')
            
            elif loginobj.role == "admin" and loginobj.status == "active":
                print(loginobj.role)
                # Set session variables for login
                request.session['username'] = loginobj.username
                request.session['loginid'] = loginobj.id
                return redirect('adminindex')
            else:
                # If role is not guest or status is not active
                messages.success(request,'Invalid role or inactive account!')
                return redirect(signin)
        else:
            # If username or password is incorrect
            messages.success(request,'Invalid username or password!')
            return redirect(signin)
        
        
        
       
        
       
        