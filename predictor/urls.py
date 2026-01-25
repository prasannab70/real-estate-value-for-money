from django.urls import path
from .views import value_for_money
urlpatterns = [ path("", value_for_money) ]
