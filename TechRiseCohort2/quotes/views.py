from django.shortcuts import render
from .models import Quote
import random
def quote_list(request):
    quotes = Quote.objects.all()
    if quotes:
       quote = random.choice(quotes)
    else:
        quote = None
    return render(request, 'quotes/quotes_list.html', {'quote': quote})
# Create your views here.
