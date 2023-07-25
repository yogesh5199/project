from django.shortcuts import render,redirect
from .models import Cart
from .models import Pet
from django.http import JsonResponse

# Create your views here.
def cart_home(request):
   items=Cart.objects.filter(user=request.user)
   flag=items.exists()
   return render(request,'cart/home.html',{'items':items,'flag':flag})

def add_to_card(request,id):
    cart_id=request.session.session_key
    if cart_id == None:
        cart_id= request.session.create()

    pet=Pet.object.get(id=id)
    price=pet.price
    user=request.user

    Cart(cart_id=cart_id,pet=pet,user=user,totalprice=price).save()

    return redirect('/')        
def update_cart(request):
    p=request.POST.get('price')
    q=request.POST.get('qnt')
    print(request.post)
    id=request.POST.get('cid')
    totalprice=float(p)*int(q)
    Cart.objects.filter(id=id).update(quantity=q,totalprice=totalprice)
    total= Cart.object.filter(user=request.user).aggregate(sum('totalprice'))
    print(total)

    totalamount=total['totalprice__sum']
    Cart.amount=totalamount

    return JsonResponse({'status':True,'totalprice':Cart.amount})

def delete_cart(request,id):
        cart=Cart.object.get(id=id)
        cart.delete()
        return redirect('cart:cartpage')