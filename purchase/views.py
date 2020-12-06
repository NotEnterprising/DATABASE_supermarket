from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, HttpResponseRedirect, redirect

from category.models import Category
from commodity.models import Commodity
from customer.models import Customer
from purchase.forms import CreatePurchase, EditPurchase
from purchase.models import Purchase

# Create your views here.
from supermarket.models import Supermarket


@login_required
def create_purchase(request):
    commoditysBefore = Commodity.objects.all()
    if request.method == 'POST':
        form = CreatePurchase(request.POST)
        commoditys = request.POST.getlist('commoditys')
        if commoditys:
            customer = Customer.objects.get(user_id=request.user.id)
            min = 0
            count = 0
            for commodity in commoditys:
                count = count + 1
                p = Purchase.objects.create(commodity_id=commodity, customer=customer)
                if min == 0:
                    min = p.id
            purchase = Purchase.objects.filter(customer_id=request.user.id)
            form = EditPurchase(queryset=purchase)
            max = min + count
            a = [x for x in range(min, max)]
            request.session['min'] = min
            return redirect('edit-purchase')
        else:
            messages.warning(request, "你没有选择任何商品")
    commoditys = []
    for c in commoditysBefore:
        if c.supermarket is not None:
            commoditys.append(c)
    return render(request, 'create_purchase.html', {"commoditys": commoditys})


@login_required
def edit_purchase(request):
    if request.method == 'POST':
        form = EditPurchase(request.POST)
        if form.is_valid():
            count = 0
            for i in form.cleaned_data:
                count = count + 1
                if i['num'] > i['id'].commodity.count:
                    messages.warning(request, "第" + str(count) + "个商品数量超过已有数量")
                    return render(request, 'edit_purchase.html', {"formset": form})
            total = 0
            for i in form.cleaned_data:
                total += i['num'] * i['id'].commodity.price
            level = Customer.objects.get(user_id=request.user.id).vip_level
            if level == 'one':
                total = total
            elif level == 'two':
                total = total * 0.9
            else:
                total = total * 0.8
            if total > Customer.objects.get(user_id=request.user.id).balance:
                messages.warning(request, "当前顾客余额不足")
                return render(request, 'edit_purchase.html', {"formset": form})
            balance = Customer.objects.get(user_id=request.user.id).balance
            Customer.objects.filter(user_id=request.user.id).update(balance=balance - total)
            for i in form.cleaned_data:
                i['id'].commodity.count = i['id'].commodity.count - i['num']
                i['id'].commodity.save()
            form.save()
            messages.success(request, '购买成功')
            return redirect('view-purchase')

    else:
        min = request.session['min']
        purchase = Purchase.objects.filter(id__gte=min)
        form = EditPurchase(queryset=purchase)
    return render(request, 'edit_purchase.html', {"formset": form})


@login_required
def results_view(request):
    purchases = Purchase.objects.all()
    commoditys = []
    for purchase in purchases:
        if purchase.customer.user_id == request.user.id:
            commoditys.append(purchase)

    customer = Customer.objects.get(user_id=request.user.id)
    context = {
        "purchases": commoditys,
        "customer": customer
    }
    return render(request, 'all_purchase.html', context)


def all_results_view(request):
    purchases = Purchase.objects.all()
    supermarkets = Supermarket.objects.all()
    categorys = Category.objects.all()
    dict = {}
    for supermarket in supermarkets:
        sup = {}
        sup['other'] = 0
        for category in categorys:
            sup['category'] = 0
            for purchase in purchases:
                if purchase.commodity.supermarket == supermarket and purchase.commodity.category == category:
                    sup['category'] = sup['category'] + purchase.commodity.price * purchase.num
                elif purchase.commodity.supermarket == supermarket and purchase.commodity.category is None:
                    sup['other'] = sup['other'] + purchase.commodity.price * purchase.num
        dict['supermarket'] = sup

    context = {
        "purchases": purchases,
        "dict": dict,
    }

    return render(request, 'all_purchase_admin.html', context)
