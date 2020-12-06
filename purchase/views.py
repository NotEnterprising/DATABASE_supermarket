from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, HttpResponseRedirect, redirect

from commodity.models import Commodity
from customer.models import Customer
from purchase.forms import CreatePurchase, EditPurchase
from purchase.models import Purchase


# Create your views here.
@login_required
def create_purchase(request):
    commoditys = Commodity.objects.all()
    if request.method == 'POST':
        form = CreatePurchase(request.POST)
        commoditys = request.POST.getlist('commoditys')
        if list:
            results = []
            customer = Customer.objects.get(user_id=request.user.id)
            for commodity in commoditys:
                results.append(Purchase(commodity=commodity, customer=customer))
            Purchase.objects.bulk_create(results)
            return redirect('view-purchase')
        else:
            messages.warning(request, "你没有选择任何商品")
    return render(request, 'create_purchase.html', {"commoditys": commoditys})


@login_required
def edit_purchase(request):
    if request.method == 'POST':
        form = EditPurchase(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '购买成功')
            return redirect('edit-purchase')
    else:
        purchase = Purchase.objects.filter(customer_id=request.user.id)
        form = EditPurchase(queryset=purchase)
    return render(request, 'edit_purchase.html', {"formset": form})


@login_required
def all_results_view(request):
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
