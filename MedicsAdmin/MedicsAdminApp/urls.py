from django.urls import path
from MedicsAdminApp import views

urlpatterns = [
    path('index/',views.index, name="index"),
    path('404/',views.fof, name="404"),

    # for Admin
    path('adminProfile/', views.adminProfile, name="adminProfile"),
    path('u_profile/<int:id>',views.update_admin,name='u_profile'),

    # for vendor
    path('vendorList/', views.vendorList, name="vendorList"),
    path('vendorProfile/<int:id>',views.vendorProfile, name="vendorProfile"),
    path('i_vendor/',views.insert_vendor,name='i_vendor'),
    path('i_store/',views.insert_store,name='i_store'),    
    path('storeDetail/<int:id>',views.storeDetail,name='storeDetail'),



    # for users
    path('userList/', views.userList, name="userList"),
    path('custList/', views.CustList, name="vendorList"),
    path('userProfile/<int:id>', views.userProfile, name="userProfile"),

    # for category
    path('mainCategory/', views.mainCategory, name="mainCategory"),
    path('i_cat/',views.insert_category,name='i_cat'),
    path('u_cat/<int:id>', views.update_category),
    path('d_cat/<int:id>',views.del_category,name="d_cat"),

    # for sub category
    path('subCategory/', views.subCategory, name="subCategory"),
    path('i_scat/',views.insert_subcategory,name='i_scat'),
    path('u_scat/<int:id>', views.update_subcategory),
    path('d_scat/<int:id>',views.del_subcategory,name="d_scat"),

    # for sub sub category
    path('subsubCategory/', views.subsubCategory, name="subsubCategory"),
    path('i_sscat/',views.insert_subsubcategory,name='i_scat'),
    path('u_sscat/<int:id>', views.update_subsubcategory),
    path('d_sscat/<int:id>',views.del_subsubcategory,name="d_scat"),

    # for products
    path('d_pro/<int:id>',views.del_product,name='d-pro'),
    path('productDetail/<int:id>', views.productDetail, name="productDetail"),
    path('productList/', views.productList, name="productList"),

    # for orders
    path('orderDetail/<int:id>', views.orderDetail, name="orderDetail"),
    path('orderHistory/', views.orderHistory, name="orderHistory"),
    path('invoice/<int:id>', views.invoice, name="invoice"),
    
    # for feedbacks
    path('reviewList/', views.reviewList, name="reviewList"),

    # for login
    path('login/',views.login, name="login"),
    path('logout/',views.logout, name="logout"),
    path('forgotPass/',views.forgotPass, name="forgotPass"),
    path('send_otp/', views.send_otp, name="sendOtp"),
    path('set_pass/',views.set_password,name='setPass'),

    # for state
    path('state/',views.state,name="state"),
    path('i_state/',views.insert_state,name='i_state',),
    path('u_state/<int:id>', views.update_state),
    path('d_state/<int:id>',views.del_state,name="d_state"),
    
    # for city
    path('city/',views.city,name="city"),
    path('i_city/',views.insert_city,name='i_city'),
    path('u_city/<int:id>', views.update_city),
    path('d_city/<int:id>',views.del_city,name="d_city"),
  
    #for area    
    path('area/',views.area,name="area"),
    path('i_area/',views.insert_area,name='i_area'),
    path('d_area/<int:id>',views.del_area,name="d_area"),
    path('u_area/<int:id>',views.update_area),

    # for role
    path('role/',views.role,name="role"),
    path('i_role/',views.insert_role,name='i_role'),
    path('u_role/<int:id>',views.update_role),
    path('d_role/<int:id>',views.del_role,name="d_role"),

    # for health condition
    path('hc/',views.HC,name="hc"),
    path('i_hc/',views.insert_HC,name='i_hc',),
    path('u_hc/<int:id>', views.update_HC),
    path('d_hc/<int:id>',views.del_hc,name="d_hc"),

    path('report1/', views.order_report1, name="report1"),
    path('report2/', views.order_report2, name="report2"),

]