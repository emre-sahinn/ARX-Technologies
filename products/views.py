from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Product, Choice, ShoppingCart
from django.urls import reverse

def index(request):
    products_list = Product.objects.order_by("pk")

    print(products_list[0].product_text)
    context = {
        'products_list': products_list,
    }
    return render(request, 'products/index.html', context)


def about(request):
    return render(request, 'products/about.html', {})


def contact(request):
    return render(request, 'products/contact.html', {})


def detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    feature_list = product.choice_set.all()
    context = {
        'product': product,
        'feature_list': feature_list
    }
    return render(request, 'products/detail.html', context)

def payment(request, product_id):
    products_list = Product.objects.order_by("pk")
    context = {
        'products_list': products_list,
    }
    return render(request, 'products/index.html', context)

def results(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    new_order = ShoppingCart.objects.order_by('-pk')[0]
    print("Order Received:", new_order.product_name, "|", new_order.product_order)
    context = {
        'product': product,
         'user_order': new_order,
    }
    return render(request, 'products/payment.html', context)


def order(request, product_id):
    total_Price = 0
    product = get_object_or_404(Product, pk=product_id)
    order_features = []
    try:
        body = 0
        color = 0
        selected_choice = request.POST.getlist('choice')
        name = request.POST['username']
        address = request.POST['address_line']
        for i in selected_choice:
            print(product.choice_set.get(pk=i))
            if str(product.choice_set.get(pk=i)).startswith("Body") and product.choice_set.get(pk=i).feature_stock > 0:
                body += 1
            elif str(product.choice_set.get(pk=i)).startswith("Color") and product.choice_set.get(pk=i).feature_stock > 0:
                color += 1
        if (body > 1 or color > 1) or (body == 0 or color == 0) or name == '' or address == '':
            raise KeyError(Choice.DoesNotExist)
    except (KeyError, Choice.DoesNotExist):
        feature_list = product.choice_set.all()
        context = {
            'product': product,
            'feature_list': feature_list,
            'error_message': "Warning: Please select suitable features and fill the form.",
        }
        return render(request, 'products/detail.html', context)
    else:
        for i in selected_choice:
            if str(product.choice_set.get(pk=i)).startswith("Body") and product.choice_set.get(pk=i).feature_stock > 0:
                order_features.append(str(product.choice_set.get(pk=i)))
                total_Price += product.choice_set.get(pk=i).feature_price
                m1 = product.choice_set.get(pk=i)
                m1.feature_stock -= 1
                m1.save()
            elif str(product.choice_set.get(pk=i)).startswith("Color") and product.choice_set.get(pk=i).feature_stock > 0:
                order_features.append(str(product.choice_set.get(pk=i)))
                total_Price += product.choice_set.get(pk=i).feature_price
                m1 = product.choice_set.get(pk=i)
                m1.feature_stock -= 1
                m1.save()
        total_Price += product.product_price
        print("total price:", total_Price)
        new_order = ShoppingCart(product_name=product.product_text,
                                 product_order=", ".join([i for i in order_features]),
                                 total_price=total_Price,
                                 user_name=name,
                                 user_address=address
                                 )
        new_order.save()
        return HttpResponseRedirect(reverse('results', args=(product.id,)))
