from django.shortcuts import render
from .models import Food

# Create your views here.
def food(request):
    foods = Food.objects.all()
    return render(request, 'food.html', {'foods': foods})
    