from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'name': 'Reyhan Zada Virgiwibowo',
        'class': 'PBP C'
    }

    return render(request, "main.html", context)