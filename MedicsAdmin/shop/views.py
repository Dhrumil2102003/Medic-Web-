from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from MedicsAdminApp.models import *
from MedicsAdminApp.forms import *
import sys
from django.contrib.auth import authenticate, login 
from MedicsAdminApp.models import UserCreateForm
from django.contrib.auth.decorators import login_required
from cart.cart import Cart
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from Paytm import Checksum
import random
from django.core.mail import send_mail
from Medics import settings

# Create your views here.
# 7043795534
def index(request):# Done
    Categories=Category.objects.all()
    SubCat = SubCategory.objects.all()
    SubSubCat=SubSubCategory.objects.all()
    bestseller = Product.objects.filter(BestSeller=1)[0:6]
    featured = Product.objects.filter(Featured=1)[0:6]
    trending = Product.objects.filter(Trending=1)[0:6]
    allbs=Product.objects.filter(BestSeller=1)
    allfea=Product.objects.filter(Featured=1)
    alltrend=Product.objects.filter(Trending=1)
    context={'bestseller':bestseller, 'trending':trending,'featured':featured,
             'allbs':allbs, 'allfea':allfea,'alltrend':alltrend, 
             'Categories':Categories, 'SubCat':SubCat, 'SubSubCat':SubSubCat}
    return render(request,'shop/index.html',context)
    #return HttpResponse("Index Shop")

def header(request):#deno
    Categories=Category.objects.all()
    SubCat = SubCategory.objects.all()
    SubSubCat=SubSubCategory.objects.all()
    bestseller = Product.objects.filter(BestSeller=1)[0:6]
    featured = Product.objects.filter(Featured=1)[0:6]
    trending = Product.objects.filter(Trending=1)[0:6]
    allbs=Product.objects.filter(BestSeller=1)
    allfea=Product.objects.filter(Featured=1)
    alltrend=Product.objects.filter(Trending=1)
    context={'bestseller':bestseller, 'trending':trending,'featured':featured,
             'allbs':allbs, 'allfea':allfea,'alltrend':alltrend, 
             'Categories':Categories, 'SubCat':SubCat, 'SubSubCat':SubSubCat}
    return render(request,'shop/header.html', context)

def ProductDetails(request, id):#deno
    if 'cust_id' in request.session:
        uid=request.session['cust_id']
        user= User.objects.get(UserId=uid)
        categories= Category.objects.all()
    else:
        return redirect("/login/")
    categories = Category.objects.all()
    product=Product.objects.filter(ProductId=id)
    feedbacks= FeedBack.objects.filter(ProductId=id)
    # product = Product.objects.all()
    context={'product':product, 'categories':categories, 'user':user, 'feedbacks':feedbacks}
    return render(request,'shop/product-details.html',context)

def addFeedback(request,id):
    pass


def about(request):#Done
    return render(request,'shop/about.html')

# def signup(request):
#     if request.method =='POST':
#         form = UserCreateForm(request.POST)
#         if form.is_valid():
#             new_user = form.save()
#             new_user=authenticate(
#                 Email = form.cleaned_data['Email'],
#                 Password = form.cleaned_data['Password1']
#             )
#             login(request, new_user)
#             return redirect("index")
#         else:
#             form = UserCreateForm()
#             context= {
#                 'form':form
#              }
#         return render(request, "shop/signup.html", context)

def client_signup(request):
    if 'client_id' not in request.session:
        ar = Area.objects.all()
        if request.method == "POST":
            form = UserProfileForm(request.POST, request.FILES)
            print("---------", form.errors)
            if form.is_valid():
                try:
                    form.save()
                    return redirect("/login/")
                except:
                    print("--------", sys.exc_info())
        else:
            form = UserProfileForm()
        return render(request, "shop/register.html", {'form': form, 'ar': ar})
    else:
        return redirect("/register/")
    
   
def login(request):
    if request.method == "POST":
        email = request.POST["Email"]
        password = request.POST["Password"]
        val = User.objects.filter(Email=email, Password=password, RoleId=2).count()
        print("-------------------", email, "---------------------", password, "========" , val)
        if val == 1:
            udata = User.objects.filter(Email=email, Password=password, RoleId=2)
            for item in udata:
                request.session['cust_email'] = item.Email
                request.session['cust_pass'] = item.Password
                request.session['cust_id'] = item.UserId
                if request.POST.get("remember"):
                    response = redirect('index')
                    response.set_cookie('C_cust_email', request.POST['email'], 3600 * 24 * 365 * 2)
                    response.set_cookie('C_cust_pass', request.POST['password'], 3600 * 24 * 365 * 2)
                    return response
            return redirect('index')
        else:
            messages.error(request, "Invalid Email or password")
            return redirect('/login/')
    else:
        if request.COOKIES.get("C_cust_email"):
            return render(request, "shop/login.html", {'cust_email_cookie1': request.COOKIES['C_cust_email'],
                                                        'cust_password_cookie2': request.COOKIES['C_cust_pass']})
        else:
            return render(request, "shop/login.html")

def shopbycat(request, id):
    if 'cust_id' in request.session:
        uid=request.session['cust_id']
        user= User.objects.get(UserId=uid)
        categories= Category.objects.all()
    else:
        return redirect("/login/")
    sscat = SubSubCategory.objects.all()[0:10]
    product = Product.objects.filter(SubSubCatId=id)
    for i in product:
        print(i)
    context = {
        'product':product,
        'sscat':sscat,
        'categories':categories,
        'user':user
    }
    return render(request, "shop/shop.html" , context)
def account(request):#Done
    return render(request,'shop/profile.html')

def blockGrid(request):#Done
    return render(request,'shop/blog-grid.html')

def cart(request):#Done
    return render(request,'shop/cart.html')

# def checkout(request):#Deno
#     return render(request,'shop/checkout.html')

def contact(request):#Done
    return render(request,'shop/contact.html')

def faq(request):#Done
    return render(request,'shop/faq.html')

def location(request):#Done
    return render(request,'shop/locations.html')

def orderTracking(request):#Done
    return render(request,'shop/order-tracking.html')

# def register(request):#Done
#     if request.method=="POST":
#         Fname=request.POST.get('Fname','')
#         Uname=request.POST.get('Uname','')
#         Lname=request.POST.get('Lname','')
#         email=request.POST.get('email','')
#         mobile=request.POST.get('mobile','')
#         password=request.POST.get('password','')
#         confirmpassword=request.POST.get('confirmpassword','')
#         register=User(Fname=Fname,Lname=Lname,email=email,password=password,confirmpassword=confirmpassword,Uname=Uname,mobile=mobile)
#         register.save()
#     return render(request,'shop/register.html')

# def register(request):
#     if 'cust_id' not in request.session:
#         ar = Area.objects.all()
#         if request.method == "POST":
#             form = UserProfileForm(request.POST)
#             print("---------", form.errors)
#             if form.is_valid():
#                 try:
#                     form.save()
#                     return redirect("/login/")
#                 except:
#                     print("--------", sys.exc_info())
#         else:
#             form = UserProfileForm()
#         return render(request, "shop/register.html", {'form': form, 'ar': ar})
#     else:
#         return render(request, "shop/index.html")

def orderDetails(request,id):
    if 'cust_id' in request.session:
        uid=request.session['cust_id']
        categories= Category.objects.all()
    else:
        return redirect("/login/")
    order=Order.objects.get(OrderId=id)
    oitems = OrderItem.objects.filter(order=id)
    # pay = Payment.objects.get(OrderId=id)
    context = {'order':order ,'categories':categories , 'oitems':oitems}
    # print(oitems.product)
    return render(request,'shop/orderDetails.html',context)

def invoice(request,id):
    if 'cust_id' in request.session:
        uid=request.session['cust_id']
        categories= Category.objects.all()
    else:
        return redirect("/login/")
    order=Order.objects.get(OrderId=id)
    user=User.objects.get(UserId=uid)
    oitems = OrderItem.objects.filter(order=id)
    context = {'order':order,'categories':categories,'oitems':oitems,'user':user}
    return render(request,"shop/invoice.html",context)

def Shop(request):
    if 'cust_id' in request.session:
        uid=request.session['cust_id']
        user= User.objects.get(UserId=uid)
        categories= Category.objects.all()
    else:
        return redirect("/login/")
    sscat = SubSubCategory.objects.all()[0:10]
    trend= request.GET.get('trending')
    best= request.GET.get('bestSeller')
    fea= request.GET.get('featured')
    if trend:
        product = Product.objects.filter(trending=1)
    elif best:
        product = Product.objects.filter(bestSeller=1)
    elif fea:
        product = Product.objects.filter(featured=1)
    else:
        product = Product.objects.all()
    context={
        'product':product ,
        'categories':categories,
        'sscat':sscat,
    }
    return render(request,'shop/shop.html',context)

def userorder(request):
    if 'cust_id' in request.session:
        uid=request.session['cust_id']
        categories= Category.objects.all()
    else:
        return redirect("/login/")
    order = Order.objects.filter(UserId =uid ).order_by('-OrderId')
    context={'categories':categories , 'order':order}
    return render(request, 'shop/userorder.html', context)

def wishlist(request):#Done
    return render(request,'shop/wishlist.html')

def teamDetails(request):
    return render(request,'shop/team-details.html')

def team(request):#Done
    return render(request,'shop/team.html')

def fourzerofour(request):#Done
    return render(request,'shop/404.html')

def appointment(request):#Done
    return render(request,'shop/appointment.html')

def blog(request):
    return render(request,'shop/blog.html')

def comingSoon(request):
    return render(request,'shop/coming-soon.html')

def service(request):
    return render(request,'shop/service.html')

def serviceDetails(request):
    return render(request,'shop/service-details.html')


def comingSoon(request):
    return render(request,'shop/coming-soon.html')
from django.shortcuts import render

# Create your views here.

# def search(request):
#     # query = request.POST('search')
#     form = SearchForm()
#     results = []

#     if request.method == 'POST':
#         form = SearchForm(request.POST)
#         if form.is_valid():
#             search_query = form.cleaned_data['search']
#             results=Product.objects.filter(ProductName=search_query)
#             # Perform search query using your preferred search method and update 'results' list

#     return render(request, 'shop/search.html', {'form': form, 'results': results})

def search(request):
    if 'cust_id' in request.session:
        uid=request.session['cust_id']
        user= User.objects.get(UserId=uid)
        categories= Category.objects.all()
    else:
        return redirect("/login/")
    query = request.POST['query']
    product = Product.objects.filter(ProductName__icontains=query)
    for i in product:
        print(i)
    context = {
        'product':product,
        'categories':categories,
        'user':user
    }
    return render(request, "shop/search.html" , context)


def forgotpass(request):
    return render(request, 'shop/forgotpassword.html')

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
        return render(request,'shop/set_password.html', {'e':e})
    
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
                return redirect("/login/")
            else:
                messages.error(request,"Invalid OTP")
                return render(request,"shop/set_password.html")
        else:
            messages.error(request,"New password and Confirm password does not match ")
            return render(request,"shop/set_password.html")
    else:
        return redirect("/forgot_password/")

def myprofile(request):
    if 'cust_id' in request.session:
        id=request.session['cust_id']
        user= User.objects.get(UserId=id)
        categories= Category.objects.all()
    else:
        return redirect("/login/")
    print(user.UserName)
    area=Area.objects.all()
    return render(request,'shop/profile.html' , {'user':user, 'categories':categories, 'area':area})

def update_profile(request,id):
    if 'cust_id' in request.session:
        id1=request.session['cust_id']
        ad= User.objects.get(UserId=id1)
    else: 
        return redirect('/login/')
    user=User.objects.get(UserId=id)
    categories = Category.objects.all()
    context = {'ad':ad, 'user':user, 'categories':categories}
    form = UpdateUserProfileForm(request.POST, request.FILES, instance=user)
    if form.is_valid():
        try:
            form.save()
            return redirect("/myprofile/")
        except:
            print("---------------", sys.exc_info())
    
    return render(request, "shop/profile.html", context)


# @login_required(login_url="/login//")
def cart_add(request, id):
    if 'cust_id' in request.session:
        uid=request.session['cust_id']
        user = User.objects.get(UserId=uid)
    else: 
        return redirect('/login/')
    cart = Cart(request)
    product = Product.objects.get(ProductId=id)
    cart.add(product=product,user=user)
    print(request.session['cart'])
    ct=request.session.get('cart')
    cartTotal= 0
    for i in ct:
        quan = ct[i]['quantity']
        price = (float(ct[i]['price']))
        subtotal = quan*price

        cartTotal += subtotal    
    request.session['cartTotal'] = cartTotal
    return redirect("index")

# @login_required(login_url="/login//")
def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(ProductId=id)
    cart.remove(product)
    if len(request.session.get('cart').items()) < 1:
        request.session['cartTotal'] = 0
    else:
        ct=request.session.get('cart')
        cartTotal= 0
        for i in ct:
            quan = ct[i]['quantity']
            price = (float(ct[i]['price']))
            subtotal = quan*price

            cartTotal += subtotal    
        request.session['cartTotal'] = cartTotal
    return redirect("cart_detail")


# @login_required(login_url="/login//")
def item_increment(request, id):
    if 'cust_id' in request.session:
        uid=request.session['cust_id']
        user = User.objects.get(UserId=uid)
    else: 
        return redirect('/login/')
    cart = Cart(request)
    product = Product.objects.get(ProductId=id)
    cart.add(product=product, user=user)
    print(request.session['cart'])
    ct=request.session.get('cart')
    cartTotal= 0
    for i in ct:
        quan = ct[i]['quantity']
        price = (float(ct[i]['price']))
        subtotal = quan*price

        cartTotal += subtotal    
    request.session['cartTotal'] = cartTotal
    return redirect("cart_detail")


# @login_required(login_url="/login//")
def item_decrement(request, id):
    if 'cust_id' in request.session:
        uid=request.session['cust_id']
        user = User.objects.get(UserId=uid)
    else: 
        return redirect('/login/')
    cart = Cart(request)
    product = Product.objects.get(ProductId=id)
    cart.decrement(product=product)
    print(request.session['cart'])
    cartTotal= request.session.get('cartTotal')
    cartTotal = cartTotal - float(product.ProductPrice)  
    print(cartTotal)
    request.session['cartTotal'] = cartTotal
    
    return redirect("cart_detail")


# @login_required(login_url="/login//")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    request.session['cartTotal'] = 0
    return redirect("cart_detail")


# @login_required(login_url="/login//")
def cart_detail(request):
    if 'cust_id' in request.session:
        id1=request.session['cust_id']
        ad= User.objects.get(UserId=id1)
    else: 
        return redirect('/login/')
    categories = Category.objects.all()
    context = {'ad':ad, 'categories':categories}
    return render(request, 'shop/cart_details.html', context)

def checkout(request):
    if 'cust_id' in request.session:
        id1=request.session['cust_id']
        user= User.objects.get(UserId=id1)
    else: 
        return redirect('/login/')
    categories = Category.objects.all()
    amount = request.session.get('cartTotal')+50
    client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))
    payment = client.order.create({'amount': (request.session.get('cartTotal')+50)*100, 'currency': 'INR','payment_capture': '1'})
    print(payment)
    return render(request, "shop/checkout.html" , {'categories':categories , 'user':user , 'amount':amount, 'payment':payment})

def place_order(request):
    if 'cust_id' in request.session:
        id1=request.session['cust_id']
        user= User.objects.get(UserId=id1)
    else: 
        return redirect('/login/')
    categories = Category.objects.all()
    product = Product.objects.all()
    cart=request.session.get('cart')
    print(cart)
    store= Store.objects.get(AreaId=user.AreaId)
    orderTotal= (request.session['cartTotal'] + 50)
    ord=Order(
            UserId =User(user.UserId),
            StoreId =Store(store.StoreId),
            Amount=orderTotal
        )
    ord.save()
    for i in cart:
        quan = cart[i]['quantity']
        price = (float(cart[i]['price']))
        prod = cart[i]['product_id']
        subtotal = quan * price
        oitem = OrderItem( order= Order(ord.OrderId) , product = Product(prod), quantity = quan)
        oitem.save()
        print(subtotal)
    request.session['tempcart'] = cart 
    request.session['cart'] = {}
    request.session['cartTotal'] = 0
    email = user.Email
    if request.method=="POST":
        # if paytype=="COD":
        # Change is Payment table : 
        pay =Payment(
        PaymentAmount= orderTotal,
        OrderId= Order(ord.OrderId),
        PaymentTypeId= PaymentType('1'),
        PaymentStatusId=PaymentStatus('1')
        )
        pay.save()
        oitem = OrderItem.objects.filter(order=ord.OrderId)
        print(ord)
        context={ 'categories':categories , 'ord':ord , 'oitem':oitem, 'pay':pay}
        return render(request, "shop/place-order.html" ,context)

def logout(request):
    try:
        del request.session['cust_email']
        del request.session['cust_pass']
        del request.session['cust_id']
    except:
        pass

    return redirect('/login/')
import razorpay
# def ch(request):
#     if request.method == 'POST':
#         amount= 100
#         currency= 'INR'
#         client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))
#         payment = client.order.create({'amount': amount, 'currency': 'INR','payment_capture': '1'})
#     return render (request,'checkout.html',  {'payment':payment})