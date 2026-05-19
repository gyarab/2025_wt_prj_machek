from django.shortcuts import render
from django.http import JsonResponse
from .models import Polozka 


def api_playground(request):
    return render(request, 'myapp/api_playground.html')


def api_polozky(request):

    q = request.GET.get('q', '')


    qs = Polozka.objects.all()
    if q:
        qs = qs.filter(nazev__icontains=q)


    data = list(qs.values('id', 'nazev', 'popis'))  # ← uprav pole

    return JsonResponse({'polozky': data, 'pocet': len(data)})
