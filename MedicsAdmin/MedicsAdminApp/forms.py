from django import forms
from .models import *
from parsley.decorators import parsleyfy

# class StateForm(forms.ModelForm):
#     class Meta:
#         model = State
#         fields= ['StateId', 'StateName']

class StateForm(forms.ModelForm):
    class Meta:
        model = State
        fields= ['StateName']

class HCForm(forms.ModelForm):
    class Meta:
        model = HealthCondition
        fields= ['HCName']

# class CityForm(forms.ModelForm):
#     class Meta:
#         model=City
#         fields=["CityId","CityName","StateId"]

class CityForm(forms.ModelForm):
    class Meta:
        model=City
        fields=["CityName","StateId"]

# class AreaForm(forms.ModelForm):
#     class Meta:
#         model = Area
#         fields=["AreaId","AreaName","pinCode","CityId"]

class AreaForm(forms.ModelForm):
    class Meta:
        model = Area
        fields=["AreaName","pinCode","CityId"]

# class RoleForm(forms.ModelForm):
#     class Meta:
#         model = Role
#         fields= ['RoleId', 'RoleName']

class RoleForm(forms.ModelForm):
    class Meta:
        model = Role
        fields= ['RoleName']

# class CategoryForm(forms.ModelForm):
#     class Meta:
#         model = Category
#         fields= ['CatId', 'CatName']

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields= ['CatName']

# class SubCategoryForm(forms.ModelForm):
#     class Meta:
#         model = SubCategory
#         fields= ['SubCatId', 'SubCatName','CatId']

class SubCategoryForm(forms.ModelForm):
    class Meta:
        model = SubCategory
        fields= ['SubCatName','CatId']

# class SubSubCategoryForm(forms.ModelForm):
#     class Meta:
#         model = SubSubCategory
#         fields= ['SubSubCatId', 'SubSubCatName','SubCatId']

class SubSubCategoryForm(forms.ModelForm):
    class Meta:
        model = SubSubCategory
        fields= ['SubSubCatName','SubCatId']

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields= ['ProductName','ProductImage','ProductPrice', 'ProductQty','Description','MRP','SubCatId','SubSubCatId','BestSeller','Featured','Trending']


# class UserImage(forms.ModelForm):  
#     class Meta:    
#         model = Product 
#         # It includes all the fields of model  
#         fields = ['ProductName', 'ProductImage']  


class StoreForm(forms.ModelForm):
    class Meta:
        model = Store
        fields= ['StoreName','StoreAddress', 'LicenseNumber', 'StoreMobile', 'VendorId', 'AreaId']


class VendorForm(forms.ModelForm):
    class Meta:
        model = Vendor
        fields= [ 'Name', 'Mobile', 'Email','Profile','Password']

class AdminProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields= ['UserName','UserProfile','FirstName', 'LastName', 'Email', 'Mobile']

@parsleyfy
class UserProfileForm(forms.ModelForm):
    class Meta:
        model=User
        fields = ['UserName', 'UserProfile', 'FirstName', 'LastName', 'Gender', 'Mobile', 'Email', 'Address', 'DOB', 'Password', 'AreaId']


class UpdateUserProfileForm(forms.ModelForm):
    class Meta:
        model=User
        fields = ['UserName', 'UserProfile', 'FirstName', 'LastName', 'Gender', 'Mobile', 'Email', 'Address', 'DOB', 'AreaId']

class SearchForm(forms.Form):
    search_query = forms.CharField(max_length=100)
