from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from cirklepay.cirklepay import CIRKLEPAY
cirklepay = CIRKLEPAY()


import uuid

# Home page
def home(request):
    return render(request, 'home.html', {})


# Cirklepay checkout page
@csrf_exempt
def cirklepay_checkout(request):
    if request.method == 'POST':
        data = dict(zip(request.POST.keys(), request.POST.values()))
        data['txnid'] = cirklepay.generate_txnid()
        cirklepay_data = cirklepay.initiate_transaction(data)
        return render(request, 'cirklepay_checkout.html', {"posted": cirklepay_data})
    return render(request, 'cirklepay.html', {})
# cirklepay success return page
@csrf_exempt
def cirklepay_success(request):
    data = dict(zip(request.POST.keys(), request.POST.values()))
    return JsonResponse(data)
