from gc import get_objects
import json
from django.shortcuts import render,redirect
from ecommerceapp.models import Contact,Menu,OrderUpdate,Orders
from django.contrib import messages
from django.http import JsonResponse
# Create your views here.
def index(request):
    return render(request,'index.html')

def contact(request):
    if request.method=="POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        desc=request.POST.get("desc")
        phonenumber=request.POST.get("pnumber")
        myquery= Contact(name=name,email=email,desc=desc,phonenumber=phonenumber)
        myquery.save()

        messages.info(request,"We will get by you soon, thanks for contacting us")
        return redirect('/contact/')
    
    return render(request,'contact.html')

def handleblog(request):

    food=Menu.objects.all()
    context = {"product":food}
    return render(request,"handleblog1.html",context)


def CheckOut(request):
    if not request.user.is_authenticated:
        messages.warning(request,"Login & Try Again")
        return redirect('/auth/login')

    if request.method=="POST":
        items_json = request.POST.get('itemsJson', '')
        name = request.POST.get('name', '')
        amount = request.POST.get('amt')
        email = request.POST.get('email', '')
        block = request.POST.get('block', '')
        room_num = request.POST.get('room_num','')
       
        reg= request.POST.get('','')
     
        phone = request.POST.get('phone', '')
        Order = Orders(items_json=items_json,name=name,amount=amount, email=email, block=block,room_num=room_num,reg=reg,phone=phone)
        print(amount)
        
        Order.save()
        update = OrderUpdate(order_id=Order.order_id,update_desc="the order has been placed")
        update.save()
        thank = True
        messages.info(request,"Order placed !!")

        # # PAYMENT INTEGRATION

        # id = Order.order_id
        # oid=str(id)+"ShopyCart"
        # param_dict = {

        #     'MID':keys.MID,
        #     'ORDER_ID': oid,
        #     'TXN_AMOUNT': str(amount),
        #     'CUST_ID': email,
        #     'INDUSTRY_TYPE_ID': 'Retail',
        #     'WEBSITE': 'WEBSTAGING',
        #     'CHANNEL_ID': 'WEB',
        #     'CALLBACK_URL': 'http://127.0.0.1:8000/handlerequest/',

        # }
        # param_dict['CHECKSUMHASH'] = Checksum.generate_checksum(param_dict, MERCHANT_KEY)
        # return render(request, 'paytm.html', {'param_dict': param_dict})
        
    return render(request,'index.html')


    



# def add_to_cart(request, product_id):
#     user = request.user
#     product = get_objects(product, pk=product_id)

#     # Check if the product is already in the cart
#     existing_cart_item = Cart.objects.filter(user=user, product=product).first()
    
#     if existing_cart_item:
#         # If the product is already in the cart, just update the quantity
#         existing_cart_item.quantity += 1
#         existing_cart_item.save()
#     else:
#         # If the product is not in the cart, create a new cart item
#         new_cart_item = Cart(user=user, product=product, quantity=1)
#         new_cart_item.save()

#     return redirect('cart.html')