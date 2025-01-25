from decimal import Decimal
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render, redirect
from MedicsAdminApp.models import User


class Cart(object):

    def __init__(self, request):
        self.request = request
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            # save an empty cart in the session
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, user, product, quantity=1, action=None):
        """
        Add a product to the cart or update its quantity.
        """
        id = product.ProductId
        userid = user.UserId
        newItem = True
        if str(product.ProductId) not in self.cart.keys():

            self.cart[product.ProductId] = {
                'userid': userid,
                'product_id': id,
                'name': product.ProductName,
                'quantity': 1,
                'price': str(product.ProductPrice),
                'image': product.ProductImage.url
            }
        else:
            newItem = True

            for key, value in self.cart.items():
                if key == str(product.ProductId):

                    value['quantity'] = value['quantity'] + 1
                    newItem = False
                    self.save()
                    break
            if newItem == True:

                self.cart[product.ProductId] = {
                    'userid': userid,
                    'product_id': product.ProductId,
                    'name': product.ProductName,
                    'quantity': 1,
                    'price': str(product.ProductPrice),
                    'image': product.ProductImage.url
                }

        self.save()

    def save(self):
        # update the session cart
        self.session[settings.CART_SESSION_ID] = self.cart
        # mark the session as "modified" to make sure it is saved
        self.session.modified = True

    def remove(self, product):
        """
        Remove a product from the cart.
        """
        product_id = str(product.ProductId)
        if product_id in self.cart:
            del self.cart[product_id]
            self.deletedId = product_id 
            self.save()

    def decrement(self, product):
        for key, value in self.cart.items():
            if key == str(product.ProductId):

                value['quantity'] = value['quantity'] - 1
                if(value['quantity'] < 1):
                    return redirect('cart:cart_detail')
                self.save()
                break
            else:
                print("Something Wrong")

    def clear(self):
        # empty cart
        self.session[settings.CART_SESSION_ID] = {}
        self.session.modified = True
