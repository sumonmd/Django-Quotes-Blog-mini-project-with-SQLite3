from django.shortcuts import render
from django.views.generic import ListView

from . models import QuoteCategory
from . models import Quote

# Create your views here.
class HomeView(ListView):
    template_name = "index.html"
    model = Quote

    def get_queryset(self):
        query_set = super().get_queryset()
        return query_set.select_related('quote_category')