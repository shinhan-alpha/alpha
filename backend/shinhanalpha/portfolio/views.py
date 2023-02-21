from django.shortcuts import render
from rest_framework import mixins, generics

from .serializers import PortfolioSerializer, PortfolioCreateSerializer

from .models import Portfolio, Dividend
# Create your views here.

class PortfolioListView(
    mixins.ListModelMixin, 
    mixins.CreateModelMixin,
    generics.GenericAPIView
):
    serializer_class = PortfolioSerializer

    def get_queryset(self):
        portfolio_id = self.kwargs.get('portfolio_id')
        if portfolio_id:
            return Portfolio.objects.filter(portfolio_id=portfolio_id) \
                .select_related('user', 'stock') \
                .stock_by('-id')
        return Portfolio.objects.none()

    def get(self,request, *args, **kwargs):
        return self.list(request, args, kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, args, kwargs)


class PortfolioCreateView(
    mixins.CreateModelMixin,
    generics.GenericAPIView
):  
    serializer_class = PortfolioCreateSerializer

    def get_queryset(self):
        portfolio_id = self.kwargs.get('portfolio_id')
        if portfolio_id:
            return Portfolio.objects.filter(portfolio_id=portfolio_id) \
                .select_related('user', 'stock') \
                .filter()
        return Portfolio.objects.none()
    
    def post(self, request, *args, **kwargs):
        return self.create(request, args, kwargs)

