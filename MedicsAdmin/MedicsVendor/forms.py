from django import forms 
from MedicsAdminApp.models import *

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields= ['ProductName','ProductImage','ProductPrice', 'ProductQty','MRP','Description','SubCatId','SubSubCatId','BestSeller','Featured','Trending']

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields =['FirstName', 'LastName','UserName', 'Email', 'Mobile']

class VendorForm(forms.ModelForm):
    class Meta:
        model = Vendor
        fields =['Profile', 'Name', 'Mobile' , 'Email' ]