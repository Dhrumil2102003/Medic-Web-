from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.mail import send_mail
from Medics import settings
from .models import *
from .forms import *
import sys
import socket
import random
socket.getaddrinfo('localhost',443)
from django.http import HttpResponse
from django.views.generic import View

from Medics.utils import render_to_pdf

# Create your views here.

def index(request):
     if 'admin_id' in request.session:
        id1=request.session['admin_id']
        ad=User.objects.get(UserId=id1)
        user=len(User.objects.all())
        cat=len(Category.objects.all())
        store=len(Store.objects.all())
        product=len(Product.objects.all())
        order=Order.objects.all().count()
        vendors=Vendor.objects.all().count()
        context={'user':user, 'cat':cat, 'store':store, 'product':product, 'ad':ad, 'vendors':vendors, 'order':order }
        return render(request, "Admin/index.html", context)
     else:
         return redirect("/Admin/login/")

def fof(request):
    return render(request, "Admin/404.html")

# for admin
def adminProfile(request):
    if 'admin_id' in request.session:
        id1=request.session['admin_id']
        ad= User.objects.get(UserId=id1)
    else: 
        return redirect('/Admin/login')
    order=len(Order.objects.filter(UserId=id1))
    context={'order':order, 'ad':ad}
    return render(request, "Admin/admin-profile.html", context)

def update_admin(request,id):
    if 'admin_id' in request.session:
        id1=request.session['admin_id']
        ad= User.objects.get(UserId=id1)
    else: 
        return redirect('/Admin/login')
    admin=User.objects.get(UserId=id)
    context = {'ad':ad, 'admin':admin}
    form = AdminProfileForm(request.POST, request.FILES, instance=admin)
    
    if form.is_valid():
        try:
            form.save()
            return redirect("/Admin/adminProfile/")
        except:
            print("---------------", sys.exc_info())
    
    return render(request, "Admin/admin-profile.html", context)

# for vendor
def vendorProfile(request, id):
    if 'admin_id' in request.session:
        id1=request.session['admin_id']
        ad= User.objects.get(UserId=id1)
    else: 
        return redirect('/Admin/login')
    vendor = Vendor.objects.get(VendorId=id)
    store = Store.objects.filter(VendorId=id)
    context={'vendor':vendor, 'ad':ad , 'store':store}
    
    return render(request, "Admin/vendor-profile.html",context)


def storeDetail(request,id):
    if 'admin_id' in request.session:
        id1=request.session['admin_id']
        ad= User.objects.get(UserId=id1)
    else: 
        return redirect('/Admin/login')
    store=Store.objects.get(StoreId=id)
    return render(request, "Admin/store-detail.html",{'store':store})


def vendorList(request):
    if 'admin_id' in request.session:
        id1=request.session['admin_id']
        ad= User.objects.get(UserId=id1)
    else: 
        return redirect('/Admin/login')
    area=Area.objects.all()
    state=State.objects.all()
    city=City.objects.all()
    store=Store.objects.all()
    vendor=Vendor.objects.all()
    return render(request, "Admin/vendor-list.html",{'vendor':vendor, 'ad':ad, 'area':area, 'city':city, 'state':state , 'store':store})  

def insert_vendor(request):
    if 'admin_id' in request.session:
        id1=request.session['admin_id']
        ad= User.objects.get(UserId=id1)
    else: 
        return redirect('/Admin/login')
    if request.method == "POST":
        form = VendorForm(request.POST ,request.FILES)
        print("---------", form.errors)
        if form.is_valid():
            try:
                form.save()
                return redirect("/Admin/vendorList/")
            except:
                print("--------", sys.exc_info())
    else:
        form = VendorForm()
    return render(request, "Admin/vendor-list.html", {'form': form,"ad":ad})

def insert_store(request):
    if 'admin_id' in request.session:
        id1=request.session['admin_id']
        ad= User.objects.get(UserId=id1)
    else: 
        return redirect('/Admin/login')
    if request.method == "POST":
        form = StoreForm(request.POST)
        print("---------", form.errors)
        if form.is_valid():
            try:
                form.save()
                return redirect("/Admin/vendorList/")
            except:
                print("--------", sys.exc_info())
    else:
        form = VendorForm()
    return render(request, "Admin/vendor-list.html", {'form': form,"ad":ad})

# for users
def userList(request):
    if 'admin_id' in request.session:
        id1=request.session['admin_id']
        ad= User.objects.get(UserId=id1)
    else: 
        return redirect('/Admin/login')
    user =User.objects.all()
    return render(request, "Admin/user-list.html",{'user':user, 'ad' : ad } )

def userProfile(request, id):
    if 'admin_id' in request.session:
        id1=request.session['admin_id']
        ad= User.objects.get(UserId=id1)
    else: 
        return redirect('/Admin/login')
    order=len(Order.objects.filter(UserId=id1))
    user=User.objects.get(UserId=id)
    context={'order':order, 'ad':ad, 'user':user}
    return render(request, "Admin/user-profile.html", context)

def CustList(request):
    if 'admin_id' in request.session:
        id1=request.session['admin_id']
        ad= User.objects.get(UserId=id1)
    else: 
        return redirect('/Admin/login')
    user=User.objects.filter(RoleId=2)
    return render(request, "Admin/customerList.html",{'ad':ad, 'user':user}) 

# for category
def mainCategory(request):
    if 'admin_id' in request.session:
        id1=request.session['admin_id']
        ad= User.objects.get(UserId=id1)
    else: 
        return redirect('/Admin/login')
    cty = Category.objects.all()
    return render(request, "Admin/main-category.html",{'cty' : cty, 'ad':ad})

def insert_category(request):
    if 'admin_id' in request.session:
        id1=request.session['admin_id']
        ad= User.objects.get(UserId=id1)
    else: 
        return redirect('/Admin/login')
    if request.method == "POST":
        form = CategoryForm(request.POST)
        print("---------", form.errors)
        if form.is_valid():
            try:
                form.save()
                return redirect("/Admin/mainCategory/")
            except:
                print("--------", sys.exc_info())
    else:
        form = CategoryForm()
    return render(request, "Admin/main-category.html", {'form': form,'ad':ad})

def update_category(request, id):
    if 'admin_id' in request.session:
        id1=request.session['admin_id']
        ad= User.objects.get(UserId=id1)
    else: 
        return redirect('/Admin/login')
    cat = Category.objects.get(CatId=id)
    form = CategoryForm(request.POST, instance=cat)

    if form.is_valid():
        try:
            form.save()
            return redirect("/Admin/mainCategory/")
        except:
            print("---------------", sys.exc_info())

    return render(request, "Admin/UpdateCategory.html", {'cat': cat,'ad':ad})

def del_category(request, id):
    c1 = Category.objects.get(CatId=id)
    c1.delete()
    return redirect("/Admin/mainCategory/")

# for sub category
def subCategory(request):
    if 'admin_id' in request.session:
        id1=request.session['admin_id']
        ad= User.objects.get(UserId=id1)
    else: 
        return redirect('/Admin/login')
    SubCty= SubCategory.objects.all()
    cat=Category.objects.all()
    return render(request, "Admin/sub-category.html",{'SubCty':SubCty, 'cat':cat, 'ad':ad})

def insert_subcategory(request):
    if 'admin_id' in request.session:
        id1=request.session['admin_id']
        ad= User.objects.get(UserId=id1)
    else: 
        return redirect('/Admin/login')
    if request.method == "POST":
        form = SubCategoryForm(request.POST)
        print("---------", form.errors)
        if form.is_valid():
            try:
                form.save()
                return redirect("/Admin/subCategory/")
            except:
                print("--------", sys.exc_info())
    else:
        form = SubCategoryForm()
    return render(request, "Admin/sub-category.html", {'form': form,"ad":ad})

def update_subcategory(request, id):
    if 'admin_id' in request.session:
        id1=request.session['admin_id']
        ad= User.objects.get(UserId=id1)
    else: 
        return redirect('/Admin/login')
    scat = SubCategory.objects.get(SubCatId=id)
    form = SubCategoryForm(request.POST, instance=scat)
    cat=Category.objects.all()

    if form.is_valid():
        try:
            form.save()
            return redirect("/Admin/subCategory/")
        except:
            print("---------------", sys.exc_info())

    return render(request, "Admin/UpdateSubCategory.html", {'scat': scat, 'cat':cat,'ad':ad})

def del_subcategory(request, id):
    c1 = SubCategory.objects.get(SubCatId=id)
    c1.delete()
    return redirect("/Admin/subCategory/")

# for sub sub category
def subsubCategory(request):
    if 'admin_id' in request.session:
        id1=request.session['admin_id']
        ad= User.objects.get(UserId=id1)
    else: 
        return redirect('/Admin/login')
    SubCty= SubCategory.objects.all()
    SubSubCty= SubSubCategory.objects.all()
    return render(request, "Admin/sub-sub-category.html",{'SubSubCty':SubSubCty, 'SubCty':SubCty , 'ad':ad})

def insert_subsubcategory(request):
    if 'admin_id' in request.session:
        id1=request.session['admin_id']
        ad= User.objects.get(UserId=id1)
    else: 
        return redirect('/Admin/login')
    if request.method == "POST":
        form = SubSubCategoryForm(request.POST)
        print("---------", form.errors)
        if form.is_valid():
            try:
                form.save()
                return redirect("/Admin/subsubCategory/")
            except:
                print("--------", sys.exc_info())
    else:
        form = SubCategoryForm()
    return render(request, "Admin/sub-sub-category.html", {'form': form, 'ad':ad})

def update_subsubcategory(request, id):
    if 'admin_id' in request.session:
        id1=request.session['admin_id']
        ad= User.objects.get(UserId=id1)
    else: 
        return redirect('/Admin/login')
    sscat = SubSubCategory.objects.get(SubSubCatId=id)
    form = SubSubCategoryForm(request.POST, instance=sscat)
    scat=SubCategory.objects.all()

    if form.is_valid():
        try:
            form.save()
            return redirect("/Admin/subsubCategory/")
        except:
            print("---------------", sys.exc_info())

    return render(request, "Admin/UpdateSubSubCategory.html", {'sscat': sscat, 'scat':scat,'ad':ad})

def del_subsubcategory(request, id):
    c1 = SubSubCategory.objects.get(SubSubCatId=id)
    c1.delete()
    return redirect("/Admin/subsubCategory/")

# for products
def productDetail(request,id):
    if 'admin_id' in request.session:
        id1=request.session['admin_id']
        ad= User.objects.get(UserId=id1)
    else: 
        return redirect('/Admin/login')
    pro=Product.objects.get(ProductId=id)
    context={'ad':ad, 'pro':pro}
    return render(request, "Admin/product-detail.html", context)
    # return render(request, "Admin/product-detail.html")ss

def productList(request):
    if 'admin_id' in request.session:
        id1=request.session['admin_id']
        ad= User.objects.get(UserId=id1)
    else: 
        return redirect('/Admin/login')
    product = Product.objects.all()
    return render(request, "Admin/product-list.html" ,{'product' : product, 'ad':ad})

def del_product(request, id):
    pro1 = Product.objects.get(ProductId=id)
    pro1.delete()
    return redirect("/Admin/productList/")

# for orders
def orderHistory(request):
    if 'admin_id' in request.session:
        id1=request.session['admin_id']
        ad= User.objects.get(UserId=id1)
    else: 
        return redirect('/Admin/login')
    order=Order.objects.all().order_by('-OrderId')
    pay=Payment.objects.all().order_by('-OrderId')
    pay_st=PaymentStatus.objects.all()
    return render(request, "Admin/order-history.html", {'order':order,'ad':ad ,'pay':pay})

def orderDetail(request,id):
    if 'admin_id' in request.session:
        id1=request.session['admin_id']
        ad= User.objects.get(UserId=id1)
    else: 
        return redirect('/Admin/login')
    order= Order.objects.get(OrderId=id)
    Pay = Payment.objects.get(OrderId=id)
    context = {'order':order, 'pay':Pay, 'ad':ad}
    return render(request, "Admin/order-detail.html", context)

def invoice(request,id):
    if 'admin_id' in request.session:
        id1=request.session['admin_id']
        ad= User.objects.get(UserId=id1)
    else: 
        return redirect('/Admin/login')
    order= Order.objects.get(OrderId=id)
    Pay = Payment.objects.get(OrderId=id)
    return render(request, "Admin/invoice.html", {'ad':ad, 'order':order, 'Pay':Pay})

# for feedbacks
def reviewList(request):
    if 'admin_id' in request.session:
        id1=request.session['admin_id']
        ad= User.objects.get(UserId=id1)
    else: 
        return redirect('/Admin/login')
    feedback=FeedBack.objects.all().select_related('UserId')
    return render(request, "Admin/review-list.html",{'feedback':feedback, 'ad':ad})

# for login

def login(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        val = User.objects.filter(Email=email, Password=password, RoleId=1).count()
        print("-------------------", email, "---------------------", password, "========", val)
        if val == 1:
            udata = User.objects.filter(Email=email, Password=password, RoleId=1)
            for item in udata:
                request.session['admin_email'] = item.Email
                request.session['admin_pass'] = item.Password
                request.session['admin_id'] = item.UserId
                if request.POST.get("remember"):
                    response = redirect('/Admin/index/')
                    response.set_cookie('A_admin_email', request.POST['email'], 3600 * 24 * 365 * 2)
                    response.set_cookie('A_admin_pass', request.POST['password'], 3600 * 24 * 365 * 2)
                    return response
            return redirect('/Admin/index/')
        else:
            messages.error(request, "Invalid Email or password")
            return redirect('/Admin/login/')
    else:
        if request.COOKIES.get("A_admin_email"):
            return render(request, "Admin/sign-in.html", {'admin_email_cookie1': request.COOKIES['A_admin_email'],
                                                        'admin_password_cookie2': request.COOKIES['A_admin_pass']})
        else:
            return render(request, "Admin/sign-in.html")
        
def logout(request):
    try:
        del request.session['admin_email']
        del request.session['admin_pass']
        del request.session['admin_id']
    except:
        pass

    return redirect('/Admin/login')

def forgotPass(request):
    return render(request, "Admin/forgotpassword.html")

def send_otp(request):
    otp1 = random.randint(10000, 99999)
    e = request.POST['Email']
    request.session['temail']=e 
    obj = User.objects.filter(Email=e).count()
    if obj == 1:
        val = User.objects.filter(Email=e).update(otp=otp1 , otp_used=0)
        subject = 'OTP Verification'
        message = str(otp1)
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [e, ]
        send_mail(subject, message, email_from, recipient_list)
        return render(request,'Admin/set_password.html', {'e':e})

def set_password(request):
    if request.method == "POST":
        # e = dict.get('email')
        # request.session['temail']=e
        T_otp = request.POST['otp']
        T_pass = request.POST['password']
        T_cpass = request.POST['cpassword']
        # e = request.POST['email']
        # request.session['temail']=e
        if T_pass == T_cpass:
            e = request.session['temail']
            val = User.objects.filter(Email=e,otp = T_otp,otp_used = 0).count()
            if val == 1:
                User.objects.filter(Email = e).update(otp_used = 1,Password = T_pass)
                return redirect("/Admin/login")
            else:
                messages.error(request,"Invalid OTP")
                return render(request,"Admin/set_password.html")
        else:
            messages.error(request,"New password and Confirm password does not match ")
            return render(request,"Admin/set_password.html")
    else:
        return redirect("/Admin/forgot_password")

# for state
def state(request):
    st=State.objects.all()
    return render(request, 'Admin/state.html',{'st':st})

def insert_state(request):
    if 'admin_id' in request.session:
        id1=request.session['admin_id']
        ad= User.objects.get(UserId=id1)
    else: 
        return redirect('/Admin/login')
    if request.method == "POST":
        form = StateForm(request.POST)
        print("---------", form.errors)
        if form.is_valid():
            try:
                form.save()
                return redirect("/Admin/state/")
            except:
                print("--------", sys.exc_info())
    else:
        form = StateForm()
    return render(request, "/Admin/state.html", {'form': form, 'ad':ad})

def update_state(request, id):
    if 'admin_id' in request.session:
        id1=request.session['admin_id']
        ad= User.objects.get(UserId=id1)
    else: 
        return redirect('/Admin/login')
    state = State.objects.get(StateId=id)
    form = StateForm(request.POST, instance=state)
    if form.is_valid():
        try:
            form.save()
            return redirect("/Admin/state/")
        except:
            print("---------------", sys.exc_info())

    return render(request, "Admin/UpdateState.html", {'state': state, 'ad':ad})

def del_state(request, id):
    st1 = State.objects.get(StateId=id)
    st1.delete()
    return redirect("/Admin/state/")

# for city
def city(request):
    ct=City.objects.all()
    st = State.objects.all()
    return render(request, "Admin/city.html",{'ct':ct, 'st':st}) 

def insert_city(request):
    if 'admin_id' in request.session:
        id1=request.session['admin_id']
        ad= User.objects.get(UserId=id1)
    else: 
        return redirect('/Admin/login')
    if request.method == "POST":
        form = CityForm(request.POST)
        print("---------", form.errors)
        if form.is_valid():
            try:
                form.save()
                return redirect("/Admin/city/")
            except:
                print("--------", sys.exc_info())
    else:
        form = CityForm()
    return render(request, "Admin/city.html", {'form': form, 'ad':ad})

def update_city(request, id):
    if 'admin_id' in request.session:
        id1=request.session['admin_id']
        ad= User.objects.get(UserId=id1)
    else: 
        return redirect('/Admin/login')
    city = City.objects.get(CityId=id)
    form = CityForm(request.POST, instance=city)
    st = State.objects.all()

    if form.is_valid():
        try:
            form.save()
            return redirect("/Admin/city/")
        except:
            print("---------------", sys.exc_info())

    return render(request, "Admin/UpdateCity.html", {'city': city, 'st': st, 'ad':ad})

def del_city(request, id):
    ct1 = City.objects.get(CityId=id)
    ct1.delete()
    return redirect("/Admin/city/")
 
# for area
def area(request):
    if 'admin_id' in request.session:
        id1=request.session['admin_id']
        ad= User.objects.get(UserId=id1)
    else: 
        return redirect('/Admin/login')
    ar=Area.objects.all()
    cts = City.objects.all()
    return render(request, "Admin/area.html",{'ar':ar,'cts':cts, 'ad':ad})  

def insert_area(request):
    if 'admin_id' in request.session:
        id1=request.session['admin_id']
        ad= User.objects.get(UserId=id1)
    else: 
        return redirect('/Admin/login')
    if request.method == "POST":
        form = AreaForm(request.POST)
        print("---------", form.errors)
        if form.is_valid():
            try:
                form.save()
                return redirect("/Admin/area/")
            except:
                print("--------", sys.exc_info())
    else:
        form = AreaForm()
    return render(request, "Admin/area.html", {'form': form, 'ad':ad})

def update_area(request, id):
    if 'admin_id' in request.session:
        id1=request.session['admin_id']
        ad= User.objects.get(UserId=id1)
    else: 
        return redirect('/Admin/login')
    area = Area.objects.get(AreaId=id)
    form = AreaForm(request.POST, instance=area)
    ct = City.objects.all()

    if form.is_valid():
        try:
            form.save()
            return redirect("/Admin/area/")
        except:
            print("---------------", sys.exc_info())

    return render(request, "Admin/UpdateArea.html", {'area': area, 'ct': ct, 'ad':ad})

def del_area(request, id):
    ar1 = Area.objects.get(AreaId=id)
    ar1.delete()
    return redirect("/Admin/area/")

# for role
def role(request):
    rl=Role.objects.all()
    return render(request, "Admin/role.html",{'rl':rl}) 

def insert_role(request):
    if 'admin_id' in request.session:
        id1=request.session['admin_id']
        ad= User.objects.get(UserId=id1)
    else: 
        return redirect('/Admin/login')
    if request.method == "POST":
        form = RoleForm(request.POST)
        print("---------", form.errors)
        if form.is_valid():
            try:
                form.save()
                return redirect("/Admin/role/")
            except:
                print("--------", sys.exc_info())
    else:
        form = RoleForm()
    return render(request, "Admin/role.html", {'form': form,'ad':ad})

def update_role(request, id):
    if 'admin_id' in request.session:
        id1=request.session['admin_id']
        ad= User.objects.get(UserId=id1)
    else: 
        return redirect('/Admin/login')
    role = Role.objects.get(RoleId=id)
    form = RoleForm(request.POST, instance=role)

    if form.is_valid():
        try:
            form.save()
            return redirect("/Admin/role/")
        except:
            print("---------------", sys.exc_info())

    return render(request, "Admin/UpdateRole.html", {'role': role,'ad':ad})  

def del_role(request, id):
    if 'admin_id' in request.session:
        id1=request.session['admin_id']
        ad= User.objects.get(UserId=id1)
    else: 
        return redirect('/Admin/login')
    r1 = Role.objects.get(RoleId=id)
    r1.delete()
    return redirect("/Admin/role/")

# for health condition
def HC(request):
    hc=HealthCondition.objects.all()
    return render(request, 'Admin/hc.html',{'hc':hc})

def insert_HC(request):
    if 'admin_id' in request.session:
        id1=request.session['admin_id']
        ad= User.objects.get(UserId=id1)
    else: 
        return redirect('/Admin/login')
    if request.method == "POST":
        form = HCForm(request.POST)
        print("---------", form.errors)
        if form.is_valid():
            try:
                form.save()
                return redirect("/Admin/hc/")
            except:
                print("--------", sys.exc_info())
    else:
        form = HCForm()
    return render(request,"Admin/hc.html", {'form': form, 'ad':ad})

def update_HC(request, id):
    if 'admin_id' in request.session:
        id1=request.session['admin_id']
        ad= User.objects.get(UserId=id1)
    else: 
        return redirect('/Admin/login')
    hc=HealthCondition.objects.get(HCId=id)
    form = HCForm(request.POST, instance=hc)
    if form.is_valid():
        try:
            form.save()
            return redirect("/Admin/hc/")
        except:
            print("---------------", sys.exc_info())

    return render(request, "Admin/Updatehc.html", {'hc':hc, 'ad':ad})

def del_hc(request, id):
    hc1 = HealthCondition.objects.get(HCId=id)
    hc1.delete()
    return redirect("/Admin/hc/")

# from django.db import connection
# from rest_framework.views import APIView
# from rest_framework.response import Response
# class ChartData(APIView):
#     authentication_classes = []
#     permission_classes = []

#     def get(self, request, format=None):
#         # qs = Company.objects.all()

#         cursor = connection.cursor()
#         print('-----------------'),
#         cursor.execute('''select OrderId,Amount FROM Order''')
#         qs = cursor.fetchall()

#         labels = []
#         default_items = []

#         for item in qs:
#             labels.append(item[0])
#             default_items.append(item[1])

#         data = {
#             "labels": labels,
#             "default": default_items,
#         }
#         return Response(data)
from django.utils.dateparse import parse_date
def order_report1(request):
    if 'admin_id' in request.session:
        id1=request.session['admin_id']
        ad= User.objects.get(UserId=id1)
    else: 
        return redirect('/Admin/login')
    if request.method == "POST":
        s_d = request.POST.get('start_date')
        e_d = request.POST.get('end_date')
        start = parse_date(s_d)
        end = parse_date(e_d)
        order = Order.objects.filter(OrderDate__range=[start, end])
        # sql = "SELECT * FROM order_table o JOIN order_item i where o.order_id = i.order_id_id and o.order_date >= %s and o.order_date <= %s;"
        # ord = Order_item.objects.raw(sql,[s_d,e_d])
    else:
        order = Order.objects.all()
    return render(request, "Admin/report1.html", {"order": order, 'ad':ad})


def order_report2(request):
    if 'admin_id' in request.session:
        id1=request.session['admin_id']
        ad= User.objects.get(UserId=id1)
    else: 
        return redirect('/Admin/login')
    store=Store.objects.all()
    if request.method == "POST":
        storeid = request.POST.get('StoreId')
        print(storeid)
        order = Order.objects.filter(StoreId=storeid)
        # pdf = render_to_pdf('Admin/reprotTemplate.html', {'order':order})
        # return HttpResponse(pdf, content_type='application/pdf')
        # sql = "SELECT * FROM order_table o JOIN order_item i where o.order_id = i.order_id_id and o.order_date >= %s and o.order_date <= %s;"
        # ord = Order_item.objects.raw(sql,[s_d,e_d])
    else:
        order = Order.objects.all()
    return render(request, "Admin/report2.html", {"order": order , 'store':store, 'ad':ad})

# class GeneratePdf(View):
#     def get(self, request, *args, **kwargs):
#         data = {
#              'today': datetime.date.today(), 
#              'amount': 39.99,
#             'customer_name': 'Cooper Mann',
#             'order_id': 1233434,
#         }
#         pdf = render_to_pdf('Admin/reportTemplate.html', data)
#         return HttpResponse(pdf, content_type='application/pdf')

