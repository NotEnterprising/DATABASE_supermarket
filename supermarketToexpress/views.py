from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, HttpResponseRedirect, redirect

from students.models import Student
from supermarket.models import Supermarket
from .models import SupermarketToExpress
from .forms import CreateSupermarketToExpress, EditSupermarketToExpress


@login_required
def create_result(request):
    supermarkets = Supermarket.objects.all()
    if request.method == 'POST':
        # after visiting the second page
        if 'finish' in request.POST:
            form = CreateSupermarketToExpress(request.POST)
            if form.is_valid():
                express = form.cleaned_data['express']
                supermarkets = request.POST['supermarkets']
                results = []
                for supermarket in supermarkets.split(','):
                    sup = Supermarket.objects.get(pk=supermarket)
                    check = SupermarketToExpress.objects.filter(supermarket=sup, express=express).first()
                    if not check:
                        results.append(
                            SupermarketToExpress(
                                express=express,
                                supermarket=sup
                            )
                        )
                SupermarketToExpress.objects.bulk_create(results)
                return redirect('view-SupermarketToExpress')

        # after choosing students
        id_list = request.POST.getlist('supermarkets')
        if id_list:
            form = CreateSupermarketToExpress()
            supermarket_list = ','.join(id_list)
            return render(request, 'create_supermarketToexpress_page2.html',
                          {"supermarkets": supermarket_list, "form": form, "count": len(id_list)})
        else:
            messages.warning(request, "你没有选择任何超市")
    return render(request, 'create_supermarketToexpress.html', {"supermarkets": supermarkets})


@login_required
def edit_results(request):
    if request.method == 'POST':
        form = EditSupermarketToExpress(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '删除成功')
            return redirect('edit-SupermarketToExpress')
    else:
        results = SupermarketToExpress.objects.all()
        form = EditSupermarketToExpress(queryset=results)
    return render(request, 'edit_supermarketToexpress.html', {"formset": form})


@login_required
def all_results_view(request):
    results = SupermarketToExpress.objects.all()
    bulk = {}

    for result in results:
        expresss = []
        for express in results:
            if express.supermarket == result.supermarket:
                expresss.append(express.express)
        bulk[result.supermarket.id] = {
            "supermarket": result.supermarket,
            "expresss": expresss,
        }
    context = {
        "results": bulk
    }
    return render(request, 'all_supermarketToexpress.html', context)
