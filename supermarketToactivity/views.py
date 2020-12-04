from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, HttpResponseRedirect, redirect

from students.models import Student
from supermarket.models import Supermarket
from .models import SupermarketToActivity
from .forms import CreateSupermarketToActivity, EditSupermarketToActivity


@login_required
def create_result(request):
    supermarkets = Supermarket.objects.all()
    if request.method == 'POST':
        # after visiting the second page
        if 'finish' in request.POST:
            form = CreateSupermarketToActivity(request.POST)
            if form.is_valid():
                activity = form.cleaned_data['activity']
                supermarkets = request.POST['supermarkets']
                results = []
                for supermarket in supermarkets.split(','):
                    sup = Supermarket.objects.get(pk=supermarket)
                    check = SupermarketToActivity.objects.filter(supermarket=sup, activity=activity).first()
                    if not check:
                        results.append(
                            SupermarketToActivity(
                                activity=activity,
                                supermarket=sup
                            )
                        )
                SupermarketToActivity.objects.bulk_create(results)
                return redirect('edit-SupermarketToActivity')

        # after choosing students
        id_list = request.POST.getlist('supermarkets')
        if id_list:
            form = CreateSupermarketToActivity()
            supermarket_list = ','.join(id_list)
            return render(request, 'create_supermarketToactivity_page2.html',
                          {"supermarkets": supermarket_list, "form": form, "count": len(id_list)})
        else:
            messages.warning(request, "You didnt select any student.")
    return render(request, 'create_supermarketToactivity.html', {"supermarkets": supermarkets})


@login_required
def edit_results(request):
    if request.method == 'POST':
        form = EditSupermarketToActivity(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Results successfully updated')
            return redirect('edit-SupermarketToActivity')
    else:
        results = SupermarketToActivity.objects.all()
        form = EditSupermarketToActivity(queryset=results)
    return render(request, 'edit_supermarketToactivity.html', {"formset": form})


@login_required
def all_results_view(request):
    results = SupermarketToActivity.objects.all()
    bulk = {}

    for result in results:
        activitys = []
        for activity in results:
            if activity.supermarket == result.supermarket:
                activitys.append(activity.activity)
        bulk[result.supermarket.id] = {
            "supermarket": result.supermarket,
            "activitys": activitys,
        }
    context = {
        "results": bulk
    }
    return render(request, 'all_supermarketToactivity.html', context)
