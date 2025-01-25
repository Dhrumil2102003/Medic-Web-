from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
# from MedicsVendor.models import User
from django.core.mail import send_mail
import random
import sys
from MedicsVendor.forms import *
from.models import *
from django.contrib import messages
from Medics import settings

# from django.contrib import messages
# from django.core.mail import send_mail
# from Medics import settings
# from .models import *
# from .forms import *
# import sys
# import socket
# import random
# socket.getaddrinfo('localhost',443)

# Create your views here.

def index(request):
    if 'vendor_id' in request.session:
        id1=request.session['vendor_id']
        ad= Vendor.objects.get(VendorId=id1)
    else: 
        return redirect('/Vendor/login')
    user=len(User.objects.all())
    product=Product.objects.all().count()
    # a=Product.StoreOwner()
    # product=len(Product.objects.filter(a=venId))
    cat=len(Category.objects.all())
    store=len(Store.objects.filter(VendorId=id1))
    context={ 'user':user, 'product':product, 'cat':cat, 'store':store , 'ad':ad}
    return render(request, "Vendor/index.html", context)

def fof(request):
    return render(request, "Vendor/404.html")

def invoice(request):
    return render(request, "Vendor/invoice.html")

def newOrder(request):
    return render(request, "Vendor/new-order.html")

def orderDetail(request,id):
    if 'vendor_id' in request.session:
        id1=request.session['vendor_id']
        ad= User.objects.get(UserId=id1)
    else: 
        return redirect('/Vendor/login')
    order= Order.objects.get(OrderId=id)
    Pay = Payment.objects.get(OrderId=id)
    context = {'order':order, 'pay':Pay, 'ad':ad}
    return render(request, "Vendor/order-detail.html", context)

def orderHistory(request):
    if 'vendor_id' in request.session:
        id1=request.session['vendor_id']
        ad= Vendor.objects.get(VendorId=id1)
    else: 
        return redirect('/Vendor/login')
    store = Store.objects.get(VendorId=id1)
    # for i in store:
    order=Order.objects.filter(StoreId=store.StoreId)
        # print(i)
    # order = Order.objects.all()
    user=User.objects.all()
    pay=Payment.objects.all()
    pay_st=PaymentStatus.objects.all()
    return render(request, "Vendor/order-history.html", {'order':order,'ad':ad})
def userProfile(request):
    if 'vendor_id' in request.session:
        id1=request.session['vendor_id']
        ad= Vendor.objects.get(VendorId=id1)
    else: 
        return redirect('/Vendor/login')
    # order=len(Order.objects.filter(VendorId=ad.VendorId))
    return render(request,"Vendor/admin-profile.html",{'ad':ad})

def custProfile(request, id):
    if 'vendor_id' in request.session:
        id1=request.session['vendor_id']
        ad= Vendor.objects.get(VendorId=id1)
    else: 
        return redirect('/Vendor/login')
    user=User.objects.get(UserId=id)
    return HttpResponse("done")

def updateProfile(request,id):
    if 'vendor_id' in request.session:
        id1=request.session['vendor_id']
        ad= Vendor.objects.get(VendorId=id1)
    else: 
        return redirect('/Vendor/login')
    vendor = Vendor.objects.get(VendorId=id)
    form = VendorForm(request.POST, request.FILES, instance=vendor)
    if form.is_valid():
        try:
            form.save()
            return redirect("/Vendor/userProfile/")
        except:
            print("---------------", sys.exc_info())

    return render(request, "Vendor/admin-profile.html", {'user': vendor})

def insert_product(request):
    if 'vendor_id' in request.session:
        id1=request.session['vendor_id']
        ad= Vendor.objects.get(VendorId=id1)
    else: 
        return redirect('/Vendor/login')
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        print("---------", form.errors)
        if form.is_valid():
            try:
                form.save()
                # img_object = form.instance 
                return redirect("/Vendor/productList/")
            except:
                print("--------", sys.exc_info())
    else:
        form = ProductForm()
    return render(request, "Vendor/product-list.html", {'form': form, 'ad':ad})

def productAdd(request):
    if 'vendor_id' in request.session:
        id1=request.session['vendor_id']
        ad= Vendor.objects.get(VendorId=id1)
    else: 
        return redirect('/Admin/login')
    cat = Category.objects.all()
    scat = SubCategory.objects.all()
    sscat = SubSubCategory.objects.all()
    HC= HealthCondition.objects.all()
    st= Store.objects.filter(VendorId=id1)
    context = {'cat':cat,'scat':scat,'sscat':sscat,'HC':HC, 'st':st ,'ad':ad}
    return render(request, "Vendor/product-add.html",context)

def productDetail(request,id):
    if 'vendor_id' in request.session:
        id1=request.session['vendor_id']
        ad= Vendor.objects.get(VendorId=id1)
    else: 
        return redirect('/Vendor/login')
    pro=Product.objects.get(ProductId=id)
    context={'ad':ad, 'pro':pro}
    return render(request, "Vendor/product-detail.html", context)
    # return render(request, "Admin/product-detail.html")


def productList(request):
    if 'vendor_id' in request.session:
        id1=request.session['vendor_id']
        ad= Vendor.objects.get(VendorId=id1)
    else: 
        return redirect('/Vendor/login')
    product= Product.objects.all()
    return render(request, "Vendor/product-list.html" ,{'product' : product ,'ad':ad})

def insert_product(request):
    if 'vendor_id' in request.session:
        id1=request.session['vendor_id']
        ad= Vendor.objects.get(VendorId=id1)
    else: 
        return redirect('/Vendor/login')
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        print("---------", form.errors)
        if form.is_valid():
            try:
                form.save()
                # img_object = form.instance 
                return redirect("/Vendor/productList/")
            except:
                print("--------", sys.exc_info())
    else:
        form = ProductForm()
    return render(request, "Vendor/product-list.html", {'form': form, 'ad':ad})

def update_product(request,id):
    if 'vendor_id' in request.session:
        id1=request.session['vendor_id']
        ad= Vendor.objects.get(VendorId=id1)
    else: 
        return redirect('/Vendor/login')
    cat = Category.objects.all()
    scat = SubCategory.objects.all()
    sscat = SubSubCategory.objects.all()
    HC= HealthCondition.objects.all()
    st= Store.objects.filter(VendorId=id1)
    pro=Product.objects.get(ProductId=id)
    context = {'cat':cat,'scat':scat,'sscat':sscat,'HC':HC, 'st':st ,'ad':ad, 'pro':pro}
    form = ProductForm(request.POST, request.FILES, instance=pro)
    if form.is_valid():
        try:
            form.save()
            return redirect("/Vendor/productList/")
        except:
            print("---------------", sys.exc_info())
    return render(request, "Vendor/UpdateProduct.html", context)

def del_product(request, id):
    if 'vendor_id' in request.session:
        id1=request.session['vendor_id']
        ad= Vendor.objects.get(VendorId=id1)
    else: 
        return redirect('/Vendor/login')
    pro1 = Product.objects.get(ProductId=id)
    pro1.delete()
    return redirect("/Vendor/productList/")


def reviewList(request):
    if 'vendor_id' in request.session:
        id1=request.session['vendor_id']
        ad= Vendor.objects.get(VendorId=id1)
    else: 
        return redirect('/Vendor/login')
    review= FeedBack.objects.all()
    return render(request, "Vendor/review-list.html" ,{'ad':ad, 'review':review})

# def login(request):

#      if request.method == "POST":
#         email = request.POST["email"]
#         password = request.POST["password"]
#         val = User.objects.filter(Email=email, Password=password).count()
#         print("-------------------", email, "---------------------", password)
#         if val == 1:
#             data = User.objects.filter(Email=email, Password=password)
#             for item in data:
#                 request.session['id'] = item.UserId
#                 request.session['fname'] = item.FirstName
#                 request.session['lname'] = item.LastName
#                 request.session['email'] = item.Email
#                 # venId = request.session['id']
#                 venId=User.objects.get(Email=email, Password=password)
#                 if request.POST.get("remember"):
#                     response = redirect("Vendor/index.html")
#                     response.set_cookie("cookie_Admin_Email", request.POST["email"], 3600 * 24 * 365 * 20)
#                     response.set_cookie("cookie_Admin_Password", request.POST["password"], 3600 * 24 * 365 * 20)
#                     return response
#             return redirect('/Vendor/index/')
#         else:
#             messages.error(request, "Invalid Email or Password")
#             return redirect('Vendor/login.html')
#      else:
#         if request.COOKIES.get("cookie_Admin_Email"):
#             return render(request,"Vendor/index.html",{'admin_email_cookie1':request.COOKIES['cookie_admin_email'],'admin_password_cookie2':request.COOKIES['cookie_admin_password']})
#         else:
#             return render(request, "Vendor/sign-in.html")


def login(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        val = Vendor.objects.filter(Email=email, Password=password).count()
        print("-------------------", email, "---------------------", password, "========", val)
        if val == 1:
            udata = Vendor.objects.filter(Email=email, Password=password)
            for item in udata:
                request.session['vendor_email'] = item.Email
                request.session['vendor_pass'] = item.Password
                request.session['vendor_id'] = item.VendorId
                if request.POST.get("remember"):
                    response = redirect('/Vendor/index/')
                    response.set_cookie('A_vendor_email', request.POST['email'], 3600 * 24 * 365 * 2)
                    response.set_cookie('A_vendor_pass', request.POST['password'], 3600 * 24 * 365 * 2)
                    return response
            return redirect('/Vendor/index/')
        else:
            messages.error(request, "Invalid Email or password")
            return redirect('/Vendor/login/')
    else:
        if request.COOKIES.get("A_vendor_email"):
            return render(request, "Vendor/sign-in.html", {'vendor_email_cookie1': request.COOKIES['A_vendor_email'],
                                                          'vendor_password_cookie2': request.COOKIES['A_vendor_pass']})
        else:
            return render(request, "Vendor/sign-in.html")
        

def logout(request):
    try:
        del request.session['vendor_email']
        del request.session['vendor_pass']
        del request.session['vendor_id']
    except:
        pass

    return redirect('/Vendor/login')


# def register(request):
#     return render(request, "Vendor/sign-up.html")

def forgotPass(request):
    return render(request, "Vendor/forgotpassword.html")


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
        return render(request,'Vendor/set_password.html', {'e':e})


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
                return redirect("/Vendor/login")
            else:
                messages.error(request,"Invalid OTP")
                return render(request,"Vendor/set_password.html")
        else:
            messages.error(request,"New password and Confirm password does not match ")
            return render(request,"Vendor/set_password.html")
    else:
        return redirect("/Vendor/forgot_password")

from django.utils.dateparse import parse_date
def order_report1(request):
    if 'vendor_id' in request.session:
        id1=request.session['vendor_id']
        vd= Vendor.objects.get(VendorId=id1)
    else: 
        return redirect('/Vendor/login')
    store =Store.objects.filter(VendorId=id1)
    if request.method == "POST":
        s_d = request.POST.get('start_date')
        e_d = request.POST.get('end_date')
        start = parse_date(s_d)
        end = parse_date(e_d)
        
        print(store)
        order = Order.objects.filter(OrderDate__range=[start, end])
    else:
        order = Order.objects.all()
    return render(request, "Vendor/report1.html", {"order": order, 'vd':vd , 'store':store})


def order_report2(request):
    if 'vendor_id' in request.session:
        id1=request.session['vendor_id']
        vd= Vendor.objects.get(VendorId=id1)
    else: 
        return redirect('/Vendor/login')
    store=Store.objects.filter(VendorId=id1)
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
    return render(request, "Vendor/report2.html", {"order": order , 'store':store, 'vd':vd})
