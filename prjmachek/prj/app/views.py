from django.shortcuts import render
from django.http import JsonResponse
from .models import Book


def api_playground(request):
    return render(request, 'myapp/api_playground.html')


def api_books(request):
    q = request.GET.get('q', '')

    qs = Book.objects.select_related('author').all()
    if q:
        qs = qs.filter(title__icontains=q)

    data = list(qs.values('id', 'title', 'published_date', 'author__name'))

    return JsonResponse({'polozky': data, 'pocet': len(data)})
