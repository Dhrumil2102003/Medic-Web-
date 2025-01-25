from django.urls import path
from MedicsVendor import views

urlpatterns = [
    path('index/',views.index, name="index"),
    path('productAdd/', views.productAdd, name="productAdd"),
    path('productDetail/<int:id>', views.productDetail, name="productDetail"),
    path('productList/', views.productList, name="productList"),
    path('newOrder/', views.newOrder, name="newOrder"),
    path('orderDetail/', views.orderDetail, name="orderDetail"),
    path('orderHistory/', views.orderHistory, name="orderHistory"),
    path('invoice/', views.invoice, name="invoice"),
    path('reviewList/', views.reviewList, name="reviewList"),
    path('login/',views.login, name="login"),
    path('forgotPass/',views.forgotPass, name="forgotPass"),
    # path('register/',views.register, name="register"),
    path('send_otp/', views.send_otp, name="sendOtp"),
    path('404/',views.fof, name="404"),
    path('userProfile/',views.userProfile),
    path('custProfile/<int:id>',views.custProfile),
    path('updateProfile/<int:id>', views.updateProfile),
    path('d_pro/<int:id>',views.del_product,name="d-pro"),
    path('u_pro/<int:id>',views.update_product,name="i-pro"),
    path('i_pro/',views.insert_product,name='i_pro'),
    path('setPass/',views.set_password,name='set_pass'),
    path('report1/', views.order_report1, name="report1"),
    path('report2/', views.order_report2, name="report2"),
]