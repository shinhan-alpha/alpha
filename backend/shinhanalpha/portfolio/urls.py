from django.urls import path
from . import views
urlpatterns = [
    path("/", views.PortfolioCreateView.as_view()),
]