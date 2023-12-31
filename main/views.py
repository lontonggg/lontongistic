import datetime
import json
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, JsonResponse
from django.core import serializers
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages  
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from main.forms import ProductForm
from main.models import Item
from django.views.decorators.csrf import csrf_exempt

@login_required(login_url='/login')
def show_main(request):
    items = Item.objects.filter(user=request.user)
    items_total = items.count()
    
    context = {
        'app' : 'Lontongistic',
        'name': request.user.username,
        'class': 'PBP C',
        'items' : items,
        'items_total' : int(items_total),
        'last_login' : request.COOKIES['last_login']
    }

    return render(request, "main.html", context)

def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        product = form.save(commit=False)
        product.user = request.user
        product.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "create_product.html", context)

def show_xml(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def register(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main")) 
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

def increase_item_amount(request, id):
    item = get_object_or_404(Item, pk=id)
    item.amount += 1
    item.save()
    return HttpResponseRedirect(reverse('main:show_main'))

def decrease_item_amount(request, id):
    item = get_object_or_404(Item, pk=id)
    if item.amount > 0:
        item.amount -= 1
        if item.amount == 0:
            item.delete()
        else:
            item.save()
    
    return HttpResponseRedirect(reverse('main:show_main'))

def remove_item(request, id):
    item = get_object_or_404(Item, pk=id)
    item.delete()
    return HttpResponseRedirect(reverse('main:show_main'))

def get_item_json(request):
    product_item = Item.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize('json', product_item))

@csrf_exempt
def add_item_ajax(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        amount = request.POST.get("amount")
        category = request.POST.get("category")
        description = request.POST.get("description")
        user = request.user

        new_product = Item(name=name, amount=amount, category=category, description=description, user=user)
        new_product.save()


        return HttpResponse(b"CREATED", status=201)
    return HttpResponseNotFound()

@csrf_exempt
def delete_item_ajax(request, id):
    item = Item.objects.get(pk=id)
    item.delete()
    return HttpResponse(b"DELETED", status=201)

@csrf_exempt
def create_product_flutter(request):
    if request.method == 'POST':
        
        data = json.loads(request.body)

        new_product = Item.objects.create(
            user = request.user,
            name = data["name"],
            amount = int(data["amount"]),
            category = data["category"],
            description = data["description"]
        )
        new_product.save()

        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)
