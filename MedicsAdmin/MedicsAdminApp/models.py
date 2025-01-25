from django.db import models

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
# Create your models here.
class State(models.Model):
    StateId=models.AutoField(primary_key=True)
    StateName=models.CharField(max_length=25,null=False)
    
    class Meta:
        db_table = 'State'

class City(models.Model):
    CityId=models.AutoField(primary_key=True)
    CityName=models.CharField(max_length=25,null=False)
    StateId=models.ForeignKey(State,on_delete=models.CASCADE)

    class Meta:
        db_table = 'City'
    
class Area(models.Model):
    AreaId=models.AutoField(primary_key=True)
    AreaName=models.CharField(max_length=25,null=False)
    pinCode=models.CharField(null=False,max_length=6)
    CityId=models.ForeignKey(City,on_delete=models.CASCADE)

    class Meta:
        db_table = 'Area'
    

class Role(models.Model):
    RoleId=models.AutoField(primary_key=True)
    RoleName=models.CharField(max_length=15,null=False)

    class Meta:
        db_table='Role'
    
class Category(models.Model):
    CatId=models.AutoField(primary_key=True)
    CatName=models.CharField(max_length=20,null=False)

    class Meta:
        db_table='Category'

class SubCategory(models.Model):
    SubCatId=models.AutoField(primary_key=True)
    SubCatName=models.CharField(max_length=20,null=False)
    CatId=models.ForeignKey(Category,on_delete=models.CASCADE)

    class Meta:
        db_table='SubCategory'    

class SubSubCategory(models.Model):
    SubSubCatId=models.AutoField(primary_key=True)
    SubSubCatName=models.CharField(max_length=20,null=False)
    SubCatId=models.ForeignKey(SubCategory,on_delete=models.CASCADE)
    

    class Meta:
        db_table='SubSubCategory'
    
class HealthCondition(models.Model):
    HCId=models.AutoField(primary_key=True)
    HCName=models.CharField(max_length=45,null=False)

    class Meta:
        db_table='HealthCondition'
   
class OrderStatus(models.Model):
    OrderStatusId=models.AutoField(primary_key=True)
    Status=models.CharField(max_length=30,null=False)

    class Meta:
        db_table='OrderStatus'
    

class PaymentStatus(models.Model):
    PaymentStatusId=models.AutoField(primary_key=True)
    PaymentStatus=models.CharField(max_length=25,null=False)

    class Meta:
        db_table='PaymentStatus'

class PaymentType(models.Model):
    PaymentTypeId=models.AutoField(primary_key=True)
    PaymentType=models.CharField(max_length=30,null=False)

    class Meta:
        db_table='PaymentType'
   

class BlogCategory(models.Model):
    BlogId=models.AutoField(primary_key=True)
    BlogType=models.CharField(max_length=15,null=False)

    class Meta:
        db_table='BlogCategory'

class User(models.Model):
    UserId=models.AutoField(primary_key=True)
    UserName=models.CharField(max_length=25,null=False, unique=True)
    UserProfile=models.ImageField(upload_to="img/users" ,null=True)
    FirstName=models.CharField(max_length=15,null=False)
    LastName=models.CharField(max_length=15,null=False)
    DOB=models.DateField(null=False,default="")
    Gender=models.CharField(max_length=6,null=False)
    Email=models.EmailField(max_length=50,null=False, unique=True)  
    Mobile= models.BigIntegerField(null=False, unique=True)
    Password=models.CharField(max_length=25,null=False) 
    Address=models.CharField(max_length=200,null=False)
    AreaId=models.ForeignKey(Area,on_delete=models.CASCADE)
    RoleId=models.ForeignKey(Role,on_delete=models.CASCADE, default=2)
    otp=models.IntegerField(null=True)
    otp_used=models.IntegerField(null=True)


    class Meta:
        db_table='user'
    
    def toVendor(self):
        r=Role.objects.get(RoleName='Vendor')
        self.RoleId=r.RoleId

class Vendor(models.Model):
    VendorId= models.AutoField(primary_key=True)
    Name=models.CharField(max_length=25, null=False)
    Profile=models.ImageField(upload_to="img/vendor")
    Email=models.CharField(max_length=40,null=False, unique=True)
    Mobile=models.BigIntegerField(null=False, unique=True)
    Password=models.CharField(max_length=25,null=False)

    class Meta:
        db_table='Vendor'


class Store(models.Model):
    StoreId=models.AutoField(primary_key=True)
    StoreName=models.CharField(max_length=30,null=False)
    StoreAddress=models.CharField(max_length=150,null=False)
    LicenseNumber=models.IntegerField(null=False,default="" , unique=True)
    StoreMobile=models.BigIntegerField(default="")
    VendorId=models.ForeignKey(Vendor,on_delete=models.CASCADE)
    AreaId=models.ForeignKey(Area,on_delete=models.CASCADE)

    class Meta:
        db_table='Store'


class Product(models.Model):
    ProductId=models.AutoField(primary_key=True)
    ProductImage=models.ImageField(upload_to="img/products", default="media/img/users/1150615.jpg")
    ProductName=models.CharField(max_length=150,null=False)
    ProductPrice=models.DecimalField(max_digits=7,decimal_places=2,null=False)
    ProductQty=models.IntegerField(null=False,default="")
    Description=models.CharField(max_length=1000,default="")
    SubCatId=models.ForeignKey(SubCategory,on_delete=models.CASCADE)
    SubSubCatId=models.ForeignKey(SubSubCategory,on_delete=models.CASCADE)
    # StoreId=models.ForeignKey(Store,on_delete=models.CASCADE)
    # HCId=models.ForeignKey(HealthCondition,on_delete=models.CASCADE, null=True)
    BestSeller=models.BooleanField()
    Featured=models.BooleanField()
    Trending=models.BooleanField()
    date = models.DateField(auto_now_add=True)
    MRP= models.IntegerField(null=False)
    class Meta:
        db_table='Product'
    

class Order(models.Model):
    OrderId=models.AutoField(primary_key=True)
    UserId=models.ForeignKey(User,on_delete=models.CASCADE)
    OrderDate=models.DateField(null=False,auto_now_add=True)
    OrderStatusId=models.ForeignKey(OrderStatus,on_delete=models.CASCADE,default="1")
    Amount = models.IntegerField(null=False,default=1)
    StoreId=models.ForeignKey(Store,on_delete=models.CASCADE)
    

    class Meta:
        db_table='Order'

class OrderItem(models.Model):
    order= models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    class Meta:
        db_table='OrderItems'

class Payment(models.Model):
    PaymentId=models.AutoField(primary_key=True)
    PaymentAmount=models.IntegerField(null=False)
    PaymentDate=models.DateField(null=False,auto_now_add=True)
    PaymentTypeId=models.ForeignKey(PaymentType,on_delete=models.CASCADE)
    PaymentStatusId=models.ForeignKey(PaymentStatus,on_delete=models.CASCADE)
    OrderId=models.ForeignKey(Order,on_delete=models.CASCADE)
    class Meta:
        db_table='Payment'

        
class FeedBack(models.Model):
    FeedBackId=models.AutoField(primary_key=True)
    FeedBackDate=models.DateField()
    FeedBackDesc=models.CharField(max_length=250,null=False)
    UserId=models.ForeignKey(User,on_delete=models.CASCADE)
    ProductId=models.ForeignKey(Product,on_delete=models.CASCADE)

    class Meta:
        db_table='FeedBack'
   

class Medicine(models.Model):
    BatchId=models.AutoField(primary_key=True)
    Company=models.CharField(max_length=15,null=False)
    Name=models.CharField(max_length=20,null=False)
    MFG=models.DateField()
    EXPDate=models.DateField()
    Qty=models.IntegerField(null=False,default="")
    ProductId=models.ForeignKey(Product,on_delete=models.CASCADE)
    HCId=models.ForeignKey(HealthCondition,on_delete=models.CASCADE)

    class Meta:
        db_table='Medicine'
   


def UserCreateForm(UserCreationForm):
    email = forms.EmailField(required=True, label="Email",error_messages={"exists":"This Already Exists"})

    class Meta:
        model = User    
        fields=('UserName','Email', 'Password1', 'Password2')

    def save(self,commit=True):
        user=super(UserCreationForm,self).save(commit=False)
        user.email= self.cleaned_data['Email']
        if commit:
            user.save()
        return user
    def clean_email(self):
        if User.objects.filter(email=self.cleaned_data['Email']).exists():
            raise forms.ValidationError(self.fields['Email'].error_message["exists"])
        return self.cleaned_data['Email']
        